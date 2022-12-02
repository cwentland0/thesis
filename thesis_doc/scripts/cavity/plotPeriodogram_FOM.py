import numpy as np
from scipy.signal import welch, periodogram, butter, filtfilt

import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.ticker as plticker
import matplotlib.gridspec as gridspec
from matplotlib.ticker import AutoMinorLocator
import os

mpl.rc('font', family='serif', size='10')
mpl.rc('axes', labelsize='x-large')
mpl.rc('figure', facecolor='w')
mpl.rc('text', usetex=False)
mpl.rc('text.latex',preamble=r'\usepackage{amsmath}')

##### START USER INPUTS #####

dataBase = "/home/chris/Research/Papers/thesis/thesis_doc/data/cavity"
dataDirs = [
            "FOM",
]

plotSignal = False
plotPSD = True
plotFFT = False

plotLegend = False
legendLabels = []

plotColors = ["k"]

pointMonNum = 8
startChunkList = [101]
endChunkList = [200]

varNames = ["Static_Pressure"]

pressFactor = 1.0

tBounds = [None, None]

minFreq    = 100.0  # lower limit for plotting PSD
cutoffFreq = 20000.0  # cutoff frequency for Butterworth filter

psdType = "welch"
window = [25000]
percOverlap = 0.75
plotSPL = True

setPSDLims = True
psdlims = [-20, 80]

plotModeLines = True
#modeLineFreqs = [587.86, 1371.66, 2155.47, 2939.28]
modeLineFreqs = [725.2, 1692.1, 2659.1]
modeLineColor = "red"

outfile = "psd_fom_100ms"
outdir = "/home/chris/Research/Papers/thesis/thesis_doc/Chapters/CavityAndCVRC/Images/cavity"

##### END USER INPUTS #####

imageDir = os.path.join(dataBase, "Images")
if not os.path.isdir(imageDir):
    os.mkdir(imageDir)


pressFactorSq = np.square(pressFactor)
if pressFactor == 1.0:
    pressScale = "Pa"
elif pressFactor == 1e3:
    pressScale = "kPa"
elif pressFactor == 1e6:
    pressScale = "MPa"
else:
    raise ValueError("Invalid pressFactor: " + str(pressFactor))

pressIdx = varNames.index("Static_Pressure") + 1

fileSuff = ""
for var in varNames:
    fileSuff += "_" + var

numPlots = plotSignal + plotPSD + plotFFT
fig, axes = plt.subplots(nrows=numPlots, ncols=1, figsize=(12,8))

# loop over time series
for plotIdx, dataDir in enumerate(dataDirs):

    print("Processing data from " + dataDir)

    dataPath = os.path.join(dataBase, dataDir, "PointResults")

    # collect data for this time series
    signalData = np.empty((0,0))
    try:
        for chunkIdx, chunk in enumerate(range(startChunkList[plotIdx], endChunkList[plotIdx] + 1)):
            inFile = "point_mon_" + str(pointMonNum) + fileSuff + "." + str(chunk) + ".npy"
            inFile = os.path.join(dataPath, inFile)
            dataIn = np.load(inFile)[:, [0, pressIdx]]
            if chunkIdx == 0:
                signalData = dataIn
            else:
                signalData = np.concatenate((signalData, dataIn), axis=0)
    except FileNotFoundError:
        if chunkIdx > 0:
            print("Simulation apparently exploded...")
        else:
            raise FileNotFoundError("Couldn't find even one probe monitor file, check that you converted to NPY")

    # extract time window
    try:
        if tBounds[0] is None:
            startIdx = None
        else:
            startIdx = np.argmax(signalData[:, 0] >= tBounds[0])

        if tBounds[1] is None:
            endIdx = None
        else:
            endIdx = signalData.shape[0] - np.argmax(signalData[::-1, 0] <= tBounds[1])

        signalData = signalData[startIdx:endIdx, :]
    except:
        pass
        print("No time bounds set...")


    tVals = signalData[:, 0]
    pressSignal = signalData[:, 1]

    # signal MUST be uniformly sampled
    tDiff = np.diff(tVals)
    assert np.allclose(tDiff[0], tDiff), "Signal is not uniformly sampled!"
    dt = tDiff[0]

    fs = 1.0 / dt               # sampling frequency
    nSamps  = pressSignal.shape[0]  # number of samples
    binSize = fs / nSamps   # number of frequency bins
    print("Number of samples: " + str(nSamps))
    print("Bin size: " + str(binSize))

    # filter signal
    if plotPSD or plotFFT:
        w = cutoffFreq / (fs / 2)
        print("w: "+ str(w))
        b, a = butter(5, w, 'lowpass')
        pressSignal_filt = filtfilt(b, a, pressSignal)

    # compute periodogram and FFT of signal
    if plotPSD:
        if psdType == "periodogram":
            f, Pxx = periodogram(pressSignal_filt, fs)
        elif psdType == "welch":
            f, Pxx = welch(pressSignal_filt, fs, nperseg=window[plotIdx], noverlap=window[plotIdx] * percOverlap)
        else:
            raise ValueError("Invalid psdType: " + psdType)
        freqLimIdx = np.argmax(f > cutoffFreq)

    if plotFFT:
        fft = np.fft.fft(pressSignal_filt)
        fft = 2.0 / nSamps * np.abs(fft)

    axIdx = 0

    # plot filtered signal
    if plotSignal:
        if numPlots == 1:
            ax = axes
        else:
            ax = axes[axIdx]
        axIdx += 1
        ax.plot(tVals, pressSignal / pressFactor, plotColors[plotIdx])
        #ax.plot(tVals, pressSignal_filt / pressFactor, plotColors[plotIdx])
        ax.yaxis.set_minor_locator(AutoMinorLocator())
        ax.set_xlabel('Time (s)')
        ax.set_ylabel('Pressure (' + pressScale + ')')

    # plot PSD
    if plotPSD:
        if numPlots == 1:
            ax = axes
        else:
            ax = axes[axIdx]
        axIdx += 1
        if plotSPL:
            psd = 20 * np.log10( np.sqrt(Pxx[1:freqLimIdx]) / 2e-5 )
            psd_label = r'SPL (dB/$\sqrt{Hz}$)'
            ax.semilogx(f[1:freqLimIdx], psd, plotColors[plotIdx])
        else:
            psd = Pxx[1:freqLimIdx] / pressFactorSq
            psd_label = r'PSD ($' + pressScale + '^2$/Hz)'
            ax.loglog(f[1:freqLimIdx], psd, plotColors[plotIdx])
        ax.set_xlim([minFreq, cutoffFreq])
        if setPSDLims:
            ax.set_ylim(psdlims)
        else:
            ax.autoscale(enable=True, axis='y', tight=True)
        plt.tick_params(axis='y', which='minor')
        ax.set_xlabel('Frequency (Hz)')
        ax.set_ylabel(psd_label)
        if plotModeLines:
            for freq in modeLineFreqs:
                ax.axvline(x=freq, color=modeLineColor, linestyle="--")

    # plot FFT
    if plotFFT:
        if numPlots == 1:
            ax = axes
        else:
            ax = axes[axIdx]
        ax.semilogx(f[1:freqLimIdx], fft[1:freqLimIdx] * 2.0 / pressFactor, plotColors[plotIdx])
        ax.set_xlim([minFreq, cutoffFreq])
        ax.autoscale(enable=True, axis='y', tight=True)
        ax.yaxis.set_minor_locator(AutoMinorLocator())
        ax.set_xlabel('Frequency (Hz)')
        ax.set_ylabel('P2P Amplitude (' + pressScale + ')')

# add legend, if requested
if plotLegend:
    if numPlots == 1:
        ax = axes
    else:
        ax = axes[0]
    ax.legend(legendLabels, loc='upper right', framealpha=1)

fig.tight_layout()

fileOut = os.path.join(outdir, outfile + ".png")
print("Saving image to " + fileOut)
plt.savefig(fileOut)
