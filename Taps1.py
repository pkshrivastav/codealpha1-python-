import os
import shutil
from PIL import Image  # Import the Image module from PIL

# Define a mapping of file extensions to folder names
FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff"],
    "Documents": [".pdf", ".doc", ".docx", ".txt", ".xls", ".xlsx", ".ppt", ".pptx"],
    "Music": [".mp3", ".wav", ".aac", ".flac"],
    "Videos": [".mp4", ".avi", ".mov", ".mkv", ".flv"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Scripts": [".py", ".js", ".java", ".html", ".css"]
}

MAIN_DIRECTORY = r"C:\Users\princ\python\python\pypro\pkks"

def organize_files(directory):
    if not os.path.exists(directory):
        print(f"Directory '{directory}' does not exist.")
        return

    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if os.path.isdir(file_path):
            continue

        _, file_extension = os.path.splitext(filename)
        file_extension = file_extension.lower()

        destination_folder = None
        for folder, extensions in FILE_TYPES.items():
            if file_extension in extensions:
                destination_folder = os.path.join(directory, folder)
                break

        if not destination_folder:
            destination_folder = os.path.join(directory, "Others")

        if not os.path.exists(destination_folder):
            os.makedirs(destination_folder)

        try:
            shutil.move(file_path, destination_folder)
            print(f"Moved: {filename} -> {destination_folder}")
        except Exception as e:
            print(f"Error moving file {filename}: {e}")

    print("File organization complete.")

def display_image(image_path):
    # Open and display the image
    with Image.open(image_path) as img:
        img.show()

if __name__ == "__main__":
    organize_files(MAIN_DIRECTORY)
    
    # Example: Display the first image in the Images folder
    images_folder = os.path.join(MAIN_DIRECTORY, "Images")
    if os.path.exists(images_folder):
        for image_file in os.listdir(images_folder):
            image_path = os.path.join(images_folder, image_file)
            display_image(image_path)  # Display the image
            break  # Display only the first image found
