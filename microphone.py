import pyaudio
import wave
import pendulum
from pydub import AudioSegment
import os
import re

googleDriveDir = "./googledriveDir"

class microphone:

    def record1min(self):
        CHUNK = 1024
        FORMAT = pyaudio.paInt16
        CHANNELS = 2
        RATE = 44100
        RECORD_SECONDS = 60

        WAVE_OUTPUT_FILENAME = "recs/record {}.wav".format(pendulum.now().to_datetime_string())

        p = pyaudio.PyAudio()

        stream = p.open(format=FORMAT,
                        channels=CHANNELS,
                        rate=RATE,
                        input=True,
                        frames_per_buffer=CHUNK)

        print("* recording")

        frames = []

        for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
            data = stream.read(CHUNK)
            frames.append(data)

        print("* done recording")

        stream.stop_stream()
        stream.close()
        p.terminate()

        wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(p.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b''.join(frames))
        wf.close()

    def convertToFlac(self):
        os.chdir("recs")
        for file in os.listdir():
            hours = pendulum.today().diff(pendulum.from_format(re.search(r"(\d+-\d+-\d+)", file).group(1), "%Y-%m-%d"),
                                          False).in_hours()
            is_not_today_file = hours < 0
            if is_not_today_file:
                #test if
                rec = AudioSegment.from_wav(file)
                os.remove(file)
                os.chdir("..")
                oldPath = os.getcwd()
                os.chdir(googleDriveDir)
                rec.export(file[:-4]+".mp3", format="mp3")
                os.chdir(oldPath)


if __name__ == '__main__':
    mic = microphone()
    mic.convertToFlac()