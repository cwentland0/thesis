import numpy as np
import os

# extract timing benchmarks from wall_time.dat
# whether these are preprocessor or solver benchmarks depends on textToFind
def extractWalltimeStats(fileIn, textToFind):

    foundFlag = False
    timeVals = np.zeros((3,4), dtype=np.float64)

    entryCount = 0
    with open(fileIn) as f:
        for lineNum, line in enumerate(f,1):
            if textToFind in line:
                foundLine = lineNum
                foundFlag = True

            if (foundFlag and (lineNum != foundLine)):
                if (((lineNum - foundLine) % 5) != 1): # don't include headers
                    for t in line.split():
                        try:
                            timeVals[int(entryCount/4), entryCount % 4] = float(t)
                            entryCount += 1
                        except:
                            pass

    return timeVals

# specific calling function to get solver benchmarks
def extractSolverWalltimeStats(fileIn):

    textToFind = "********** SOLVER BENCHMARKS **********"
    timeVals = extractWalltimeStats(fileIn, textToFind)
    return timeVals

# specific calling function to get preprocessor benchmarks
def extractPreprocWalltimeStats(fileIn):

    textToFind = "********** PREPROCESSOR BENCHMARKS **********"
    timeVals = extractWalltimeStats(fileIn, textToFind)
    return timeVals

# get partition data from partitionOutput.out
def extractPartitionData(fileIn):

    partitionIBlankCounts = [None]*3
    partitionSizes = []
    partitionStats = [None]*4

    with open(fileIn) as f:
        for lineNum, line in enumerate(f, 1):
            lineSplit = line.split()
            # get total mesh type counts
            if "Number directly sampled cells" in line:
                partitionIBlankCounts[0] = int(lineSplit[-1])
            elif "Number flux sampled cells" in line:
                partitionIBlankCounts[1] = int(lineSplit[-1])
            elif "Number gradient sampled cells" in line:
                partitionIBlankCounts[2] = int(lineSplit[-1])
            elif "Number subsampling graph edges" in line:
                numGraphEdges = int(lineSplit[-1])
            elif "total communications" in line:
                numComms = int(lineSplit[-1])
            elif "Partition" in line:
                # check if it's a partition size
                try:
                    partNum = int(lineSplit[1])
                    partitionSizes.append(int(lineSplit[-1]))
                except:
                    if (lineSplit[1] == "cell"):
                        if (lineSplit[2] == "max:"):
                            partitionStats[0] = int(lineSplit[-1])
                        if (lineSplit[2] == "min:"):
                            partitionStats[1] = int(lineSplit[-1])
                        if (lineSplit[2] == "avg:"):
                            partitionStats[2] = float(lineSplit[-1])
                        if (lineSplit[2] == "std:"):
                            partitionStats[3] = float(lineSplit[-1])

    partitionSizes = partitionSizes[:-1]

    return partitionIBlankCounts, partitionStats, numGraphEdges, numComms

# get number of communications directly from ASCII mesh files
def extractCommsFromASCIIMesh(meshDir, meshName, numParts):

    recvNum = 0
    sendNum = 0
    for fileIdx in range(numParts):
        meshFile = os.path.join(meshDir, meshName+"."+str(fileIdx+1))
        with open(meshFile) as f:
            for lineNum, line in enumerate(f):
                if ((lineNum == 0) or (lineNum == 1)):
                    pass
                elif (lineNum == 2):
                    _, recvIn = line.split()
                    recvNum += int(recvIn)
                elif (lineNum == 3):
                    _, sendIn = line.split()
                    sendNum += int(sendIn)
                else:
                    break

    assert(recvNum == sendNum)
    return sendNum

# get integrated error values
def extractIntError(caseDir, iterStart, iterEnd, iterSkip, varNames, vsRaw=True, velMag=True):

    errFileName = "errVals_int_"+str(iterStart)+"_"+str(iterEnd)+"_"+str(iterSkip)
    if vsRaw:
        errFileName += "_raw"
    if velMag:
        errFileName += "_velMag"
    errFileName += ".dat"
    fileIn = os.path.join(caseDir, errFileName)

    # if single string, convert to list
    if (type(varNames) == str):
        varNames = [varNames]

    # load data from file
    errDataMat = np.loadtxt(fileIn, dtype={'names':('labels','values'),'formats':('|S30',np.float)})

    errVals = np.zeros(len(varNames), dtype=np.float64)
    for idx in range(errDataMat.shape[0]):
        varName = errDataMat[idx][0].decode('UTF-8')
        if varName in varNames:
            insertIdx = varNames.index(varName)
            errVals[insertIdx] = errDataMat[idx][1]

    return errVals



