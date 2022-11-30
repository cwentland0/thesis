import os
from math import sqrt

import numpy as np
import tecplot as tec
from tecplot.constant import PlotType, SliceSurface, TextBox, Units, AnchorAlignment

def calcHats(p1, h, m):

    h /= 2

    x1 = p1[0]; y1 = p1[1]
    if (m == 0):
        dx = h
    else:
        dx = sqrt(h**2 / (1.0 + 1/m**2))

    dy = sqrt(h**2 - dx**2)

    p2 = (x1 + dx, y1 + dy)
    p3 = (x1 - dx, y1 - dy)

    return [p2, p3]

def plotContourOrSlices(
        case_dir,
        iter_start,
        iter_end,
        iter_skip,
        var_name,
        colormap,
        colormap_bounds,
        num_colormap_levels,
        frame_height,
        frame_width,
        output_dir,
        meshfile=None,
        slice_axis=None,
        slice_origin=None,
        axes_off=True,
        show_legend=False,
        legend_spacing=1.2,
        legend_level_skip=1,
        vertical_legend=False,
        legend_position=(0, 100),
        var_name_legend="ADD LEGEND NAME",
        font_name="Times",
        font_size=17.0,
        add_line=False,
        line_coords=None,
        line_thickness=2,
        add_hats=True,
        hat_length=0.005,
        zoom=False,
        zoom_lims=None,
        fig_width=512,
        file_header=None,
    ):


    file_list = []
    if meshfile is not None:
        file_list += [meshfile]

    # some logic checks and additional calculations
    assert len(colormap_bounds) == 2
    colormap_levels = np.linspace(colormap_bounds[0], colormap_bounds[1], num=num_colormap_levels)

    # loop over dataset snapshots
    iter_range = range(iter_start, iter_end + 1, iter_skip)
    num_iters = len(iter_range)
    for iter_idx, iter_num in enumerate(iter_range):

        print("Processing snapshot "+str(iter_num))

        # load dataset
        file_name = os.path.join(case_dir, "gemsma_cmb_"+str(iter_num)+".szplt")
        file_list_in = file_list + [file_name]
        if (file_list_in[-1][-6:] == ".szplt"):
            dataset = tec.data.load_tecplot_szl(file_list_in, read_data_option=2)
        elif (file_list_in[-1][-4:] == ".plt"):
            dataset = tec.data.load_tecplot(file_list_in, read_data_option=2)
        else:
            raise ValueError("Invalid file extension")
        tZone = dataset.zone(0)
        num_dims = tZone.rank

        if num_dims == 3:
            if (slice_axis is None) or (slice_origin is None):
                raise ValueError("Did not pass slice_axis or slice_origin")

        # get some relevant objects
        tFrame = tec.active_frame()
        if num_dims == 2:
            tPlot = tFrame.plot(PlotType.Cartesian2D)
        else:
            tPlot = tFrame.plot(PlotType.Cartesian3D)

        tPlot.show_contour = True
        if num_dims == 3:
            tPlot.show_slices = True
            tSlice = tPlot.slice(0)
            tSlice.contour.show = True

        tContour = tPlot.contour(0)
        tLegend = tContour.legend

        if num_dims == 3:
            # slice settings
            if (slice_axis == "x"):
                tSlice.orientation = SliceSurface.XPlanes
                tPlot.view.psi = 90
                tPlot.view.theta = -90
                tSlice.origin = (slice_origin, tSlice.origin[1], tSlice.origin[2])
            elif (slice_axis == "y"):
                tSlice.orientation = SliceSurface.YPlanes
                tPlot.view.psi = 90
                tPlot.view.theta = 0
                tSlice.origin = (tSlice.origin[0], slice_origin, tSlice.origin[2])
            elif (slice_axis == "z"):
                if (num_dims == 3):
                    tSlice.orientation = SliceSurface.ZPlanes
                    tPlot.view.psi = 0
                    tPlot.view.theta = 0
                    tSlice.origin = (tSlice.origin[0], tSlice.origin[1], slice_origin)
                else:
                    raise ValueError("No z-dimension for 2-dimensional data")
            else:
                raise ValueError("Invalid slice_axis input")

            tSlice.edge.show = True
        else:
            if axes_off:
                tPlot.axes.x_axis.show = False
                tPlot.axes.y_axis.show = False
            tPlot.show_edge = True

        # contour settings
        tContour.variable = dataset.variable(var_name) 	# set plot variable
        tContour.colormap_name = colormap
        tContour.levels.reset_levels(colormap_levels)

        # frame settings
        tFrame.show_border = False
        tFrame.height = frame_height
        tFrame.width = frame_width

        # legend settings
        if show_legend:
            tLegend.box.box_type = TextBox.None_
            tLegend.row_spacing = legend_spacing
            tLegend.label_step = legend_level_skip
            tLegend.overlay_bar_grid = False

            # change font
            tLegend.number_font.typeface = font_name
            tLegend.number_font.size_units = Units.Point
            tLegend.number_font.size = font_size
            tLegend.number_font.bold = True
            tLegend.header_font.typeface = font_name
            tLegend.header_font.size_units = Units.Point
            tLegend.header_font.size = font_size
            tLegend.header_font.bold = True

            # set orientation/position of legend
            tLegend.vertical = vertical_legend
            tLegend.anchor_alignment = AnchorAlignment.TopLeft
            tLegend.position = legend_position

            dataset.variable(var_name).name = var_name_legend # rename variable
        else:
            tLegend.show = False

        # miscellaneous
        tPlot.axes.viewport.left = 5
        tPlot.axes.viewport.right = 95
        tPlot.axes.viewport.top = 95
        tPlot.axes.viewport.bottom = 5
        if num_dims == 3:
            tPlot.axes.orientation_axis.show = False
        tec.macro.execute_command('$!WorkspaceView FitAllFrames')
        tPlot.view.fit()
        if zoom:
            if zoom_lims is None:
                raise ValueError("Did not pass zoom_lims")
            tPlot.view.zoom(zoom_lims[0][0], zoom_lims[1][0], zoom_lims[0][1], zoom_lims[1][1])

        if add_line:
            if line_coords is None:
                raise ValueError("Did not pass line_coords")
            tLine = tFrame.add_polyline(line_coords)
            tLine.line_thickness = line_thickness
            if add_hats:
                # determine slope
                m = -(line_coords[1][0] - line_coords[0][0]) / (line_coords[1][1] - line_coords[0][1])
                hat1 = calcHats(line_coords[0], hat_length, m)
                hat2 = calcHats(line_coords[1], hat_length, m)
                tLine2 = tFrame.add_polyline(hat1)
                tLine2.line_thickness = line_thickness
                tLine3 = tFrame.add_polyline(hat2)
                tLine3.line_thickness = line_thickness

        # save to image
        if file_header is None:
            if num_dims == 2:
                file_header = "fig_" + var_name
            else:
                file_header = "fig_" + slice_axis + "_" + var_name
        if num_iters > 1:
            file_header += "_" + str(iter_num)
        if zoom:
            file_header += "_zoom"

        out_file = file_header + ".png"
        out_file = os.path.join(output_dir,  out_file)
        tec.export.save_png(out_file, width=fig_width)