import os
import shutil
from tkinter import filedialog, Tk
from pathlib import Path

# Initialize Tkinter
root = Tk()
root.withdraw()  # Hide the main window

# Ask the user to select the directory to sort
source_path = filedialog.askdirectory(title="Select the directory you want to sort")

# Check if a directory was selected
if not source_path:
    print("No directory was selected. Cancelling this operation.")
    exit()

source_path = Path(source_path)

# Iterate over all items in the selected directory
for a_file in source_path.iterdir():
    if a_file.is_dir():
        print(f'{a_file} is a directory. Not moved.')
        continue  # Skip directories

    # Determine the target directory based on file extension
    extension = a_file.suffix or 'ZZZ_Miscellaneous'
    target_path = source_path / extension

    # Create the target directory if it does not exist
    if not target_path.exists():
        target_path.mkdir()
        print(f'Created directory {target_path}')
    
    # Determine the destination path for the file
    destination = target_path / a_file.name
    
    # Check if the file already exists in the target directory
    if destination.exists():
        print(f'{a_file} already exists in {target_path}. Not moved.')
    else:
        # Move the file to the target directory
        shutil.move(str(a_file), str(destination))
        print(f'Moved file {a_file} to {destination}')

        
        
    
    

