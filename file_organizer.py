import os
import shutil

SOURCE_FOLDER = "downloads"

FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".txt"],
    "Videos": [".mp4", ".avi", ".mkv"],
    "Archives": [".zip", ".rar"]
}

def organize_files():
    if not os.path.exists(SOURCE_FOLDER):
        print("Folder not found.")
        return

    for filename in os.listdir(SOURCE_FOLDER):
        file_path = os.path.join(SOURCE_FOLDER, filename)

        if os.path.isfile(file_path):
            moved = False

            for folder, extensions in FILE_TYPES.items():
                if any(filename.lower().endswith(ext) for ext in extensions):

                    target_folder = os.path.join(SOURCE_FOLDER, folder)
                    os.makedirs(target_folder, exist_ok=True)

                    shutil.move(
                        file_path,
                        os.path.join(target_folder, filename)
                    )

                    moved = True
                    break

            if not moved:
                other_folder = os.path.join(SOURCE_FOLDER, "Others")
                os.makedirs(other_folder, exist_ok=True)

                shutil.move(
                    file_path,
                    os.path.join(other_folder, filename)
                )

    print("Files organized successfully.")

organize_files()
