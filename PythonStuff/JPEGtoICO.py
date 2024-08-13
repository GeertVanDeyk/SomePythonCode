from PIL import Image
from tkinter import filedialog, Tk
import os
from pathlib import Path

def convert_jpg_to_ico(jpg_path, ico_path, icon_sizes=[(16, 16), (32, 32), (48, 48), (64, 64), (128, 128), (256, 256)]):
    """
    Convert a JPG image to ICO format.

    :param jpg_path: Path to the source JPG file.
    :param ico_path: Path to save the output ICO file.
    :param icon_sizes: List of sizes for the ICO file.
    """
    img = Image.open(jpg_path)
    img.save(ico_path, format='ICO', sizes=icon_sizes)

if __name__ == '__main__':
# Initialize Tkinter
    root = Tk()
    root.withdraw()  # Hide the main window
# Ask the user to select the directory to sort
    source_path = str(filedialog.Open(title="Select the picture you want to turn into an icon"))  
    source_path = Path(source_path)    
    # Get the directory of the original file
    original_dir = os.path.dirname(source_path)
    
    # Create the 'ico' subdirectory if it doesn't exist
    ico_dir = os.path.join(original_dir, 'ico')
    os.makedirs(ico_dir, exist_ok=True)
    
    # Construct the path for the .ico file within the 'ico' subdirectory
    base_name = os.path.basename(source_path)
    name_without_ext = os.path.splitext(base_name)[0]
    target_path = Path(os.path.join(ico_dir, f"{name_without_ext}.ico")) 
    
# Example usage:
    jpg_path = source_path  # Replace with your JPG file path
    ico_path = target_path  # Replace with your desired ICO file path

    convert_jpg_to_ico(jpg_path, ico_path)
