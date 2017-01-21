import glob, os, random, math, shutil
from unipath import Path, FILES, DIRS
import unipath

basePath = 'trainning sound/'
doorPath = basePath + 'door'
hornPath = basePath + 'horn'
motoPath = basePath + 'moto'
silentPath = basePath + 'silent'
trainDirSet = [doorPath, hornPath, motoPath,]
startPath = os.getcwd()

pool_test = []
for path in trainDirSet:
    os.chdir(path)
    pool2 = []
    for wav in glob.glob('*.wav'):
        data = path+'/'+wav
        pool2.append(data)
    n = len(pool2)
    random.shuffle(pool2)
    n_train = int(math.ceil(n*.7))
    train = pool2[:n_train]
    test = pool2[n_train:]
    pool_test.append(test)
    os.chdir(startPath)

print pool_test