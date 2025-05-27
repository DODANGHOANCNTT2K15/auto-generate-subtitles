from moviepy import VideoFileClip

def extrack_audio_from_video(video_path, output_audio_path):
    try:
        print(f"Đang trích xuất âm thanh từ video: {video_path}...")
        video = VideoFileClip(video_path)
        audio = video.audio
        audio.write_audiofile(output_audio_path, codec='pcm_s16le', fps=44100, nbytes=2, buffersize=2000)
        print(f"Đã lưu âm thanh tại: {output_audio_path}")
    except Exception as e:
        print(f"Lỗi khi trích xuất âm thanh: {str(e)}")