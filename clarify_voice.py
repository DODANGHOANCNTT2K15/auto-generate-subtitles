import librosa
import soundfile as sf
import noisereduce as nr
import numpy as np
from scipy.signal import butter, filtfilt
from tqdm import tqdm

def enhance_voice(input_path, output_path, sr=None):
    try:
        print("🎤 Đang xử lý âm thanh...")
        
        # Đọc file âm thanh
        print("📂 Đang đọc file audio...")
        audio, sample_rate = librosa.load(input_path, sr=sr)
        
        # Giảm nhiễu
        print("🔇 Đang giảm nhiễu...")
        reduced_noise = nr.reduce_noise(
            y=audio,
            sr=sample_rate,
            stationary=True,
            prop_decrease=1.0
        )
        
        # Tăng cường giọng nói (frequency range 100-8000 Hz)
        print("🔊 Đang tăng cường giọng nói...")
        def butter_bandpass(lowcut, highcut, fs, order=5):
            nyq = 0.5 * fs
            low = lowcut / nyq
            high = highcut / nyq
            b, a = butter(order, [low, high], btype='band')
            return b, a

        # Lọc dải tần
        lowcut = 100.0
        highcut = 8000.0
        b, a = butter_bandpass(lowcut, highcut, sample_rate)
        enhanced = filtfilt(b, a, reduced_noise)
        
        # Chuẩn hóa âm lượng
        print("📊 Đang chuẩn hóa âm lượng...")
        normalized = librosa.util.normalize(enhanced)
        
        # Tăng độ rõ của giọng nói
        print("💪 Đang tăng cường độ rõ...")
        enhanced_audio = librosa.effects.preemphasis(normalized)
        
        # Lưu file đã xử lý
        print("💾 Đang lưu file...")
        sf.write(output_path, enhanced_audio, sample_rate)
        
        print(f"✅ Đã lưu file âm thanh đã xử lý tại: {output_path}")
        return True
        
    except Exception as e:
        print(f"❌ Lỗi: {str(e)}")
        return False

if __name__ == "__main__":
    input_file = "output.wav"  # File âm thanh đầu vào
    output_file = "output_enhanced.wav"  # File âm thanh đã xử lý
    
    enhance_voice(input_file, output_file)