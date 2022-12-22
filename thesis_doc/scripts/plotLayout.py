import os

import tecplot as tec

def plotLayout(
    filename,
    layout,
    fileline,
    outname,
):

    os.system('sed -i \"' + str(fileline) + 's#.*#\$\!VarSet |LFDSFN1| = \'\"' + filename + '\"\'#\" ' + layout)

    print("Loading " + filename)
    tec.load_layout(layout)
    
    print("Saving image to " + outname)
    tec.export.save_png(outname, width=1024)
