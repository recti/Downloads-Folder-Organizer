import os
import sys
import time
import shutil
import re
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(message)s")

# Constants
DOWNLOADS_FOLDER = os.path.expanduser("~/Downloads")
FILE_CATEGORIES = {
    "Documents": [".doc", ".docx", ".pdf", ".ppt", ".pptx", ".xls", ".xlsx", ".txt"],
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Videos": [".mp4", ".avi", ".mkv", ".wmv", ".flv", ".mov"],
    "Executables": [".exe", ".msi", ".dmg"],
    "ExcelFiles": [".xls", ".xlsx", ".csv"],
    "ZipFiles": [".zip", ".rar"],
    "Books": [".epub"],
}
PERSONAL_KEYWORDS = [
    "anass", "nasser", "cv", "resume", "facture", "jan", "january", "feb", "february", 
    "mar", "march", "apr", "april", "may", "jun", "june", "jul", "july", "aug", 
    "august", "sep", "september", "oct", "october", "nov", "november", "dec", "december"
]

# Banner animation
def print_slow(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.05)
    print()

# Create directories if they don't exist
def create_directories():
    for directory in FILE_CATEGORIES.keys():
        dir_path = os.path.join(DOWNLOADS_FOLDER, directory)
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)
            logging.info(f"Created directory: {dir_path}")

# Move files to appropriate directories
def organize_files():
    for filename in os.listdir(DOWNLOADS_FOLDER):
        # Skip hidden files
        if filename.startswith("."):
            continue

        file_path = os.path.join(DOWNLOADS_FOLDER, filename)
        file_ext = os.path.splitext(filename)[-1].lower()
        file_name_without_ext = os.path.splitext(filename)[0].lower()

        # Move files based on extension
        moved = False
        for category, extensions in FILE_CATEGORIES.items():
            if file_ext in extensions:
                dest_dir = os.path.join(DOWNLOADS_FOLDER, category)
                shutil.move(file_path, os.path.join(dest_dir, filename))
                logging.info(f"Moved {filename} to {category} directory.")
                moved = True
                break

        # Move personal files based on keywords
        if not moved:
            for keyword in PERSONAL_KEYWORDS:
                if re.search(keyword, filename, re.IGNORECASE) or re.search(keyword, file_name_without_ext, re.IGNORECASE):
                    dest_dir = os.path.join(DOWNLOADS_FOLDER, "PersonalFiles")
                    if not os.path.exists(dest_dir):
                        os.makedirs(dest_dir)
                    shutil.move(file_path, os.path.join(dest_dir, filename))
                    logging.info(f"Moved {filename} to PersonalFiles directory.")
                    moved = True
                    break

        if not moved:
            logging.warning(f"No category found for {filename}. Skipping...")

# Main function
def main():
    print_slow("Bismillah, let's make today amazing!")
    create_directories()
    organize_files()

if __name__ == "__main__":
    main()