import librosa
import soundfile as sf
import noisereduce as nr
from tqdm import tqdm
import numpy as np

def clean_audio(input_path, output_path):
    try:
        # Hiển thị thanh tiến trình khi đọc file
        print(f"Đang đọc file {input_path}...")
        with tqdm(total=100, desc="Đọc file") as pbar:
            audio_data, sample_rate = librosa.load(input_path, sr=None)
            pbar.update(100)
        
        # Hiển thị tiến trình giảm nhiễu
        print("\nĐang làm sạch audio...")
        chunks = np.array_split(audio_data, 100)  # Chia thành 100 phần
        cleaned_chunks = []
        
        with tqdm(total=len(chunks), desc="Giảm nhiễu") as pbar:
            for chunk in chunks:
                reduced_chunk = nr.reduce_noise(
                    y=chunk,
                    sr=sample_rate,
                    prop_decrease=1.0,
                    stationary=True
                )
                cleaned_chunks.append(reduced_chunk)
                pbar.update(1)
        
        reduced_noise = np.concatenate(cleaned_chunks)
        
        # Hiển thị tiến trình chuẩn hóa
        print("\nĐang chuẩn hóa âm lượng...")
        with tqdm(total=100, desc="Chuẩn hóa") as pbar:
            normalized_audio = librosa.util.normalize(reduced_noise)
            pbar.update(100)
        
        # Hiển thị tiến trình lưu file
        print(f"\nĐang lưu file {output_path}...")
        with tqdm(total=100, desc="Lưu file") as pbar:
            sf.write(output_path, normalized_audio, sample_rate)
            pbar.update(100)
        
        print("\nHoàn thành!")
        return True
        
    except Exception as e:
        print(f"Lỗi: {str(e)}")
        return False

if __name__ == "__main__":
    input_path = "output.mp3"
    output_path = "output_cleaned.wav"
    clean_audio(input_path, output_path)