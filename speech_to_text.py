import whisper
import srt
from datetime import timedelta
from tqdm import tqdm
import os
import torch
import time  

# Bản đồ mã ngôn ngữ
language_map = {
    "vi": "vi",
    "en": "en",
    "ja": "ja",
    "ko": "ko",
    "zh": "zh",
    "fr": "fr",
    "de": "de"
}

def transcribe_with_whisper(audio_path, output_srt, language_code="en", model_size="medium"):
    try:
        if not os.path.exists(audio_path):
            print(f"❌ File {audio_path} không tồn tại.")

        max_threads = os.cpu_count()
        torch.set_num_threads(max_threads)
        print(f"⚙️  Đang sử dụng {max_threads} luồng CPU...")

        lang = language_map.get(language_code.lower(), "en")

        print(f"🧠 Đang tải mô hình Whisper: {model_size}")
        model = whisper.load_model(model_size)

        print(f"🔊 Đang nhận diện từ: {audio_path} ({lang})...")
        result = model.transcribe(
            audio_path,
            language=lang,
            verbose=False,
        )

        subtitles = []
        print("📝 Đang tạo phụ đề SRT...")
        for i, segment in tqdm(enumerate(result["segments"]), total=len(result["segments"]), desc="Tạo SRT"):
            start = timedelta(seconds=segment["start"])
            end = timedelta(seconds=segment["end"])
            text = segment["text"].strip()
            sub = srt.Subtitle(index=i + 1, start=start, end=end, content=text)
            subtitles.append(sub)

        with open(output_srt, "w", encoding="utf-8") as f:
            f.write(srt.compose(subtitles))

        print(f"✅ Đã lưu file phụ đề: {output_srt}")
        
    except Exception as e:
        print(f"❌ Lỗi khi xử lý: {str(e)}")

if __name__ == "__main__":
    start_total = time.time() 
    
    input_audio = "output_enhanced.wav"
    language = input("🌐 Nhập mã ngôn ngữ (vi, en, ja, ko, zh, fr, de): ").strip().lower()
    output_srt = "subtitles_whisper.srt"
    model_size = "base"  

    transcribe_with_whisper(input_audio, output_srt, language_code=language, model_size=model_size)
    
    end_total = time.time()
    total_time = end_total - start_total
    hours = int(total_time // 3600)
    minutes = int((total_time % 3600) // 60)
    seconds = int(total_time % 60)
    
    print(f"\n🎯 Tổng thời gian chạy: {hours:02d}:{minutes:02d}:{seconds:02d}")
