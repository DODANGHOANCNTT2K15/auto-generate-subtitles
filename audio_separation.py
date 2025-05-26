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
    
if __name__ == "__main__":
    video_path = "01 Cướp Biển Vùng Caribê- Lời Nguyền Của Tàu Ngọc Trai Đen - Pirates of the Caribbean- The Curse of the Black Pearl Full HD Vietsub online - BluPhim.mp4"
    output_audio_path = "output.wav"
    extrack_audio_from_video(video_path, output_audio_path)