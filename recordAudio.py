
import pyaudio
import wave


WAVE_OUTPUT_FILENAME = "filename.wav"
def recordAudioFile(self):
    FORMAT = pyaudio.paInt16
    CHANNELS = 2
    RATE = 44100
    CHUNK = 1024
    RECORD_SECONDS = 5

    audio = pyaudio.PyAudio()


    stream = audio.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)
    print("recording audio...")

    frames = []
    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)

    print("recording finished...  Thank You!!!")

    #stop recording
    stream.start_stream()
    stream.close()
    audio.terminate()

    #saving file
    waveFile = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    waveFile.setnchannels(CHANNELS)
    waveFile.setsampwidth(audio.get_sample_size(FORMAT))
    waveFile.writeframes(b''.join(frames))
    waveFile.close()



recordAudioFile()