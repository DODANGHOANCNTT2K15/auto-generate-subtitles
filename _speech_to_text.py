import whisper
import srt
from datetime import timedelta
from tqdm import tqdm
import os
import torch
from _normalize_audio import normalize_audio
from _reduce_noise import reduce_noise

language_map = {
    "en": "en",
    "ja": "ja",
}

def transcribe_with_whisper(audio_path, output_srt, language_code="en", model_size="base"):
    """Nhận diện giọng nói và tạo phụ đề SRT từ file âm thanh."""
    try:
        if not os.path.exists(audio_path):
            print(f"❌ File âm thanh {audio_path} không tồn tại.")
            return
        
        # Tạo tên file tạm
        base_name = os.path.splitext(os.path.basename(audio_path))[0]
        normalized_path = f"temp_normalized_{base_name}.wav"
        denoised_path = f"temp_denoised_{base_name}.wav"

        # Tiền xử lý âm thanh
        print("🔊 Tiền xử lý âm thanh...")

        normalized_audio_path = normalize_audio(audio_path, normalized_path)
        if not normalized_audio_path:
            return

        denoised_audio_path = reduce_noise(normalized_audio_path, denoised_path)
        if not denoised_audio_path:
            return

        print("✅ Tiền xử lý hoàn tất.")
        
        # Cấu hình mô hình
        max_threads = os.cpu_count()
        torch.set_num_threads(max_threads)
        print(f"⚙️ Đang sử dụng {max_threads} luồng CPU...")
        lang = language_map.get(language_code.lower(), "en")
        print(f"🧠 Đang tải mô hình Whisper: {model_size}")
        model = whisper.load_model(model_size)

        # Nhận diện
        print(f"🔊 Đang nhận diện từ: {denoised_audio_path} ({lang})...")
        result = model.transcribe(
            denoised_audio_path,
            language=lang,
            verbose=False,
            temperature=0.6,
            beam_size=10,
            word_timestamps=True,
        )

        # Ghi phụ đề
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
        
        # Xóa file tạm
        for temp_file in [normalized_audio_path, denoised_audio_path, audio_path]:
            if os.path.exists(temp_file):
                os.remove(temp_file)

    except Exception as e:
        print(f"❌ Lỗi khi xử lý: {str(e)}")
