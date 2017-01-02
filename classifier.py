from pyAudioAnalysis import audioTrainTest as aT
import glob, os, random

basePath = 'trainning sound/'
doorPath = basePath + 'door'
hornPath = basePath + 'horn'
motoPath = basePath + 'moto'

startPath = os.getcwd()

trainDirSet = [doorPath, hornPath, motoPath] 

#listOfDirs, mtWin, mtStep, stWin, stStep, classifierType, modelName, computeBEAT=False, perTrain=0.90
aT.featureAndTrain(trainDirSet, 1.0, 1.0, aT.shortTermWindow, aT.shortTermStep, "svm", "abc", computeBEAT=False, perTrain=0.90)

#aT.featureAndTrain(["classifierData/music","classifierData/speech"], 1.0, 1.0, aT.shortTermWindow, aT.shortTermStep, "svm", "svmSMtemp", False)

#%%
pool = []
for path in trainDirSet:
    os.chdir(path)
    for wav in glob.glob('*.wav'):
        data = path+'/'+wav
        pool.append(data)
    os.chdir(startPath)

#%%
for i in range(3):
    test = random.choice(pool)
    print "classifying {}".format(test)
    print aT.fileClassification(test, "abc","svm")