import zipfile
import os
import glob

def extract_datasets():
    raw_path = 'data/raw/'
    processed_path = 'data/processed/'
    
    # This looks for ANY zip file in the raw folder
    zip_files = glob.glob(os.path.join(raw_path, "*.zip"))
    
    if not zip_files:
        print(f"❌ Still no zip files found in {raw_path}. Please move your datasets here!")
        return

    for zip_path in zip_files:
        # Determine if it's video or text based on filename
        folder_name = "videos/" if "video" in zip_path.lower() or "deep" in zip_path.lower() else "text/"
        target_dir = os.path.join(processed_path, folder_name)
        
        if not os.path.exists(target_dir): os.makedirs(target_dir)
        
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(target_dir)
            print(f"✅ Successfully extracted {os.path.basename(zip_path)} to {target_dir}")

if __name__ == "__main__":
    extract_datasets()