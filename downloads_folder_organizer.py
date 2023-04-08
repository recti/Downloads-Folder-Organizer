import os
import sys
import time
import shutil
import re



## banner 
def print_slow(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.05)
print_slow("Bismillah, let's make today amazing!")

# Define the path to your downloads folder
downloads_folder = os.path.expanduser("~/Downloads")

## Delete images from downloads_folder
##for filename in os.listdir(downloads_folder):
##   if filename.endswith((".jpg", ".jpeg", ".png", ".gif", ".bmp")):
##        file_path = os.path.join(downloads_folder, filename)
##        os.remove(file_path)
##        print(f"Deleted {filename} from {downloads_folder}")


# Define the destination directories for different file types
document_dir = os.path.join(downloads_folder, "Documents")
image_dir = os.path.join(downloads_folder, "Images")
video_dir = os.path.join(downloads_folder, "Videos")
executable_dir = os.path.join(downloads_folder, "Executables")
excel_dir = os.path.join(downloads_folder, "ExcelFiles")
zip_dir = os.path.join(downloads_folder, "ZipFiles")
personal_dir = os.path.join(downloads_folder, "PersonalFiles")
books_dir  =  os.path.join(downloads_folder, "Books")

# Create the destination directories if they don't exist
for directory in [document_dir, image_dir, video_dir, executable_dir, excel_dir, zip_dir, personal_dir]:
    if not os.path.exists(directory):
        os.makedirs(directory)

# Define a list of file extensions for different types of files
document_ext = [".doc", ".docx", ".pdf", ".ppt", ".pptx", ".xls", ".xlsx", ".txt"]
image_ext = [".jpg", ".jpeg", ".png", ".gif", ".bmp"]
video_ext = [".mp4", ".avi", ".mkv", ".wmv", ".flv", ".mov"]
executable_ext = [".exe", ".msi", ".dmg"]
excel_ext = [".xls", ".xlsx",".csv"]
zip_ext = [".zip", ".rar"]
book_ext =[".epub"]

# Define a list of keywords for personal files
personal_keywords = ["anass", "nasser", "cv", "resume", "facture", "jan", "january", "feb", "february", "mar", "march", 
                  "apr", "april", "may", "jun", "june", "jul", "july", "aug", "august", "sep", "september", 
                  "oct", "october", "nov", "november", "dec", "december"]

# Loop over all the files in the downloads folder
for filename in os.listdir(downloads_folder):
    # Ignore any files that start with a dot (hidden files)
    if filename.startswith("."):
        continue

    # Get the file extension
    file_ext = os.path.splitext(filename)[-1].lower()

    # Move the file to the appropriate directory based on its extension
    try:
        if file_ext in document_ext:
            shutil.move(os.path.join(downloads_folder, filename), os.path.join(document_dir, filename))
            print(f"Moved {filename} to Documents directory.")
        elif file_ext in image_ext:
            shutil.move(os.path.join(downloads_folder, filename), os.path.join(image_dir, filename))
            print(f"Moved {filename} to Images directory.")
        elif file_ext in video_ext:
            shutil.move(os.path.join(downloads_folder, filename), os.path.join(video_dir, filename))
            print(f"Moved {filename} to Videos directory.")
        elif file_ext in executable_ext:
            shutil.move(os.path.join(downloads_folder, filename), os.path.join(executable_dir, filename))
            print(f"Moved {filename} to Executables directory.")
        elif file_ext in excel_ext:
            shutil.move(os.path.join(downloads_folder, filename), os.path.join(excel_dir, filename))
            print(f"Moved {filename} to ExcelFiles directory.")
        elif file_ext in zip_ext:
            shutil.move(os.path.join(downloads_folder, filename), os.path.join(zip_dir, filename))
            print(f"Moved {filename} to ZipFiles directory.")
        elif file_ext in book_ext:
            shutil.move(os.path.join(downloads_folder, filename), os.path.join(books_dir, filename))
            print(f"Moved {filename} to Books directory.")
        else:
            # Check if the file contains any of the personal keywords
            for keyword in personal_keywords:
                if re.search(keyword, filename, re.IGNORECASE) or re.search(keyword, os.path.splitext(filename)[0], re.IGNORECASE):
                    shutil.move(os.path.join(downloads_folder, filename), os.path.join(personal_dir, filename))
                    print(f"Moved {filename} to PersonalFiles directory.")

    except FileNotFoundError:
        print(f"File {filename} not found in {downloads_folder}. Skipping...") 