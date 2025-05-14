import speech_recognition as sr
from moviepy.editor import VideoFileClip,AudioFileClip, ComposeAudioClip
class MovieManager:
    def get_war_audio(self,mp4_file,war_file):
        vc = VideoFileClip(mp4_file)
        ac = vc. audio
        ac.write_audiofile(war_file,code='pum_sl6le')
        ac.close()
        vc.close()
    def audio_to_text(self,audio,file):
        r = sr.Recognizer()
        with sr.AudioFile(audio,file) as source:
            audio=r.record(source)
        try:
            text:r.recognize_google(audio)
            return text
        except:
            return'unknow'