from moviepy.editor import AudioFileClip,VideoFileClip
from sqlalchemy import true
from pydub import AudioSegment
from scipy.io import wavfile
import wave


#从视频中提取音频
def extract_Audio(video_path,audio_path):
    audio = AudioFileClip(video_path)
    audio.write_audiofile(audio_path)

def audio_capture(audio_path,out_path,starttime,endtime):
    s = wavfile.read(audio_path)
    f = wave.open(audio_path)
    SampleRate = f.getframerate()
    # print(SampleRate)
    wavfile.write(out_path,SampleRate,s[1][starttime:endtime*SampleRate])
    # wavfile.write(out_path,SampleRate,s[1][5:15*SampleRate])



if __name__ == '__main__':
    video_path = "H:/depression_system/video/42022-04-29_video.mp4"
    audio_path = 'H:/depression_system/audio/12022-04-29_video_capture.wav'
    # extract_Audio(video_path,audio_path)
    # out_path = 'H:/depression_system/audio/12022-04-29_video.wav'
    # audio_capture(audio_path,out_path,1,5)

