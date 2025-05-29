from pydub import AudioSegment

def normalize_audio(input_path, output_path):
    """Chuẩn hóa âm lượng của file âm thanh và xuất ra file mới."""
    try:
        audio = AudioSegment.from_file(input_path)
        normalized_audio = audio.normalize()
        normalized_audio.export(output_path, format="wav")
        print(f"✅ Đã lưu file âm thanh chuẩn hóa tại: {output_path}")
        return output_path
    except Exception as e:
        print(f"❌ Lỗi khi chuẩn hóa âm thanh: {str(e)}")
        return None