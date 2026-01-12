import os
import shutil

FOLDER_PATH = "files"

FILE_TYPES = {
    "Images": [".jpg", ".png", ".jpeg"],
    "Documents": [".pdf", ".docx", ".txt"],
    "Videos": [".mp4", ".mov"],
    "Others": []
}

def organise_files():
    for file_name in os.listdir(FOLDER_PATH):
        file_path = os.path.join(FOLDER_PATH, file_name)

        if os.path.isfile(file_path):
            moved = False
            for folder, extensions in FILE_TYPES.items():
                if any(file_name.lower().endswith(ext) for ext in extensions):
                    os.makedirs(folder, exist_ok=True)
                    shutil.move(file_path, os.path.join(folder, file_name))
                    moved = True
                    break

            if not moved:
                os.makedirs("Others", exist_ok=True)
                shutil.move(file_path, os.path.join("Others", file_name))

if __name__ == "__main__":
    organise_files()
