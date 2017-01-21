def listOfDirSound():
    import os
    import glob

    basePath = 'trainning sound/'
    doorPath = basePath + 'door'
    hornPath = basePath + 'horn'
    motoPath = basePath + 'moto'
    trainDirSet = [doorPath, hornPath, motoPath]
    startPath = os.getcwd()

    pool = []
    for path in trainDirSet:
        os.chdir(path)
        for wav in glob.glob('*.wav'):
            data = path + '/' + wav
            pool.append(data)
        os.chdir(startPath)
    return pool

def exportMetaData():
    from pydub import AudioSegment
    import pandas as pd

    meta = []
    for filepath in listOfDirSound():
        wav = AudioSegment.from_wav(filepath)
        pathSpilt = filepath.split(r'/')
        type = pathSpilt[1]
        filename = pathSpilt[2]
        note = {
            'type': type,
            'filename': filename,
            'duration_ms': len(wav),
            'loudness_dB': wav.dBFS,
            'channels': wav.channels,
            'sampleWidth': wav.sample_width,
            'frameRate': wav.frame_rate,
            'maxdB': wav.max_dBFS,
        }
        meta.append(note)

    df = pd.DataFrame(meta)
    df.to_csv('trainning sound/allsounds.csv')

exportMetaData()