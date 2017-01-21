#from past import autotranslate
from pyAudioAnalysis import audioTrainTest as aT

import glob, os, random


basePath = 'trainning sound/'
doorPath = basePath + 'door'
hornPath = basePath + 'horn'
motoPath = basePath + 'moto'
silentPath = basePath + 'silent'
trainDirSet = [doorPath, hornPath, motoPath,]
startPath = os.getcwd()

#Test History
# modelname - desc
#1. abcd - test and train using same sample

# series a - Jan 10, 2017
# train/test 70/30
#2. SVMa - support vector machine
#3. GBa - gradientboosting
#4. RFa - randomforest
#5. KNNa - knn
#6. ETa - extratrees


#listOfDirs, mtWin, mtStep, stWin, stStep, classifierType, modelName, computeBEAT=False, perTrain=0.90
aT.featureAndTrain(trainDirSet, 0.5, 0.5, aT.shortTermWindow, aT.shortTermStep, "svm", "SVMa", computeBEAT=False, perTrain=0.90)

#aT.featureAndTrain(["classifierData/music","classifierData/speech"], 1.0, 1.0, aT.shortTermWindow, aT.shortTermStep, "svm", "svmSMtemp", False)



    
    

#%%
def testAccuracy():
    basePath = 'testing sound/'
    doorPath = basePath + 'door'
    hornPath = basePath + 'horn'
    motoPath = basePath + 'moto'
    #silentPath = basePath + 'silent'
    testDirSet = [doorPath, hornPath, motoPath,]

    pool = []
    for path in testDirSet:
        os.chdir(path)
        for wav in glob.glob('*.wav'):
            data = path+'/'+wav
            pool.append(data)
        os.chdir(startPath)

    #%%
    for i in range(3):
        test = random.choice(pool)
        print ("classifying {}".format(test))
        print (aT.fileClassification(test, "abcd","svm"))