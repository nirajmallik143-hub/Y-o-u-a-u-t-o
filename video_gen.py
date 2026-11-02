import os
from gtts import gTTS
from moviepy.editor import TextClip, AudioFileClip, ColorClip, CompositeVideoClip

def create_video(script_text, output_filename="output.mp4", is_short=True):
    # 1. Generate Voiceover
    tts = gTTS(text=script_text, lang='en', tld='us')
    audio_path = "voice.mp3"
    tts.save(audio_path)
    audio = AudioFileClip(audio_path)
    
    # 2. Set dimensions based on format (Shorts = 9:16, Long = 16:9)
    if is_short:
        size = (1080, 1920)
    else:
        size = (1920, 1080)
        
    # 3. Create Background & Text Overlay (Headless-friendly setup)
    bg = ColorClip(size=size, color=(20, 20, 20), duration=audio.duration)
    
    txt_clip = TextClip(
        script_text[:100] + "...", 
        fontsize=50, 
        color='white', 
        size=size, 
        method='caption'
    ).set_duration(audio.duration)
    
    video = CompositeVideoClip([bg, txt_clip]).set_audio(audio)
    video.write_videofile(output_filename, fps=24, codec='libx264', audio_codec='aac')
    print(f"Video rendered: {output_filename}")

if __name__ == "__main__":
    create_video("Did you know that your brain hides memories until you least expect it?", "test.mp4", True)
