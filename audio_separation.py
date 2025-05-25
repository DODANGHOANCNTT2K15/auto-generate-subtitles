from moviepy import VideoFileClip
from tqdm import tqdm
import time

def extract_audio(video_path, output_path):
    try:
        print(f"Đang xử lý video: {video_path}")
        
        # Tạo thanh tiến trình tổng thể
        with tqdm(total=100, desc="Trích xuất âm thanh") as pbar:
            # Đọc video
            pbar.update(20)
            video = VideoFileClip(video_path)
            
            # Tách audio
            pbar.update(40)
            audio = video.audio
            
            # Lưu file audio
            pbar.update(30)
            audio.write_audiofile(output_path, codec='mp3', logger=None)
            
            # Đóng các file
            audio.close()
            video.close()
            pbar.update(10)
            
        print(f"\nĐã lưu âm thanh vào: {output_path}")
        return True
        
    except Exception as e:
        print(f"Lỗi: {str(e)}")
        return False

if __name__ == "__main__":
    video_file = r"01 Cướp Biển Vùng Caribê- Lời Nguyền Của Tàu Ngọc Trai Đen - Pirates of the Caribbean- The Curse of the Black Pearl Full HD Vietsub online - BluPhim.mp4"  
    audio_file = "output.mp3"      
    extract_audio(video_file, audio_file)