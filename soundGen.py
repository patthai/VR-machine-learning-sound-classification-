#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  2 15:39:40 2017

@author: heim
"""
import pydub

from general import listOfDirSound




def generateSoundOfManyMixed(filename):
    from pydub import AudioSegment
    import random as rnd
    import pandas as pd

    gen_sound = AudioSegment.empty()
    sounds = listOfDirSound()
    metaData = []

    for i in range(10):
        duration = 1 * 1000 * rnd.random()
        slient_lessThan_1_sec = AudioSegment.silent(duration=duration)
        note = {
            "sound": "silent",
            "duration_ms": duration
        }
        metaData.append(note)

        choice = rnd.choice(sounds)
        wav = AudioSegment.from_wav(choice)
        gen_sound = gen_sound + slient_lessThan_1_sec + wav
        note = {
            "sound": choice,
            "duration_ms": len(wav)
        }
        metaData.append(note)

    metaDataDF = pd.DataFrame(metaData)
    metaDataDF.to_csv(filename[:-3]+'csv')
    gen_sound.export(filename,'wav')

def generateSilent():
    from pydub import AudioSegment
    import random as rnd
    import pandas as pd


    for i in range(20):
        duration = 3 * 1000 * rnd.random()
        slient_lessThan_1_sec = AudioSegment.silent(duration=duration)
        slient_lessThan_1_sec.export('trainning sound/silent/silent_{}.wav'.format(i), 'wav')



if __name__ == '__main__':
    #generateSoundOfManyMixed('trainning sound/test/nonOverlay2.wav')
    generateSilent()