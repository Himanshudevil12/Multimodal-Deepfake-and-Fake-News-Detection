import cv2
import os
import glob

def extract_bridge_frame():
    # Search for ANY mp4 file anywhere inside data/processed/videos/
    search_path = os.path.join('data', 'processed', 'videos', '**', '*.mp4')
    videos = glob.glob(search_path, recursive=True)
    
    if not videos:
        print("❌ ERROR: No .mp4 files found.")
        print("Check if they are in: data/processed/videos/")
        return

    print(f"📦 Found {len(videos)} videos. Extracting from: {os.path.basename(videos[0])}")
    
    # Extract the first frame
    cap = cv2.VideoCapture(videos[0])
    ret, frame = cap.read()
    
    if ret:
        save_path = 'data/processed/videos/sample_frame.jpg'
        cv2.imwrite(save_path, frame)
        print(f"✅ SUCCESS: Frame saved to {save_path}")
    else:
        print("❌ ERROR: Could not read the video file.")
    cap.release()

if __name__ == "__main__":
    extract_bridge_frame()