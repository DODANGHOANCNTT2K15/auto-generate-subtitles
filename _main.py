import time
from _speech_to_text import transcribe_with_whisper
from _audio_separation import extract_audio_from_video

if __name__ == "__main__":
    start_total = time.time() 
    
    video_path = r"input_video.mp4"
    output_audio = "output_enhanced.wav"
    extract_audio_from_video(video_path, output_audio)
    input_audio = "output_enhanced.wav"
    language = input("🌐 Nhập mã ngôn ngữ (en, ja): ").strip().lower()
    output_srt = "subtitles_whisper.srt"
    model_size = "base"  

    transcribe_with_whisper(input_audio, output_srt, language_code=language, model_size=model_size)
    
    end_total = time.time()
    total_time = end_total - start_total
    hours = int(total_time // 3600)
    minutes = int((total_time % 3600) // 60)
    seconds = int(total_time % 60)
    
    print(f"\n🎯 Tổng thời gian chạy: {hours:02d}:{minutes:02d}:{seconds:02d}")