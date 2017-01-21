from pyAudioAnalysis import audioAnalysis

basePath = 'trainning sound/test/nonOverlay2.wav'

#audioAnalysis.segmentclassifyFileWrapper(basePath,'SVMa','svm')

from pyAudioAnalysis import audioSegmentation as aS
[flagsInd, classesAll, acc, CM] = aS.mtFileClassification(basePath, "SVMa", "svm", True, 'trainning sound/test/nonOverlay2.csv')