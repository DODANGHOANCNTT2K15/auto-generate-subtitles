from moviepy import VideoFileClip

def extract_audio_from_video(video_path, output_audio_path):
    try:
        if not video_path:
            print("❌ Đường dẫn video không hợp lệ.")
            return
        print(f"Đang trích xuất âm thanh từ video: {video_path}...")
        video = VideoFileClip(video_path)
        audio = video.audio
        audio.write_audiofile(output_audio_path, codec='pcm_s16le', fps=16000)
        print(f"Đã lưu âm thanh tại: {output_audio_path}")
        audio.close()
        video.close()
    except Exception as e:
        print(f"Lỗi khi trích xuất âm thanh: {str(e)}")