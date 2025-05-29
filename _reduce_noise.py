import librosa
import noisereduce as nr
import soundfile as sf 

def reduce_noise(input_path, output_path):
    """Giảm nhiễu nền của file âm thanh và xuất ra file mới."""
    try:
        print("📥 Đang tải file âm thanh...")
        y, sr = librosa.load(input_path)
        print("🔧 Đang xử lý giảm nhiễu...")
        reduced_noise = nr.reduce_noise(y=y, sr=sr)
        print(f"💾 Đang lưu file sau khi giảm nhiễu tại: {output_path}")
        sf.write(output_path, reduced_noise, sr)
        print("✅ Đã lưu xong.")
        return output_path
    except Exception as e:
        print(f"❌ Lỗi khi giảm nhiễu: {str(e)}")
        return None
