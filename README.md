🖼️ Image Resizer Tool (Batch Mode)
Overview
A Python tool to resize and optionally convert all images in a folder automatically.
Built using Pillow (PIL) for image processing and os for file handling.

Features
📂 Process multiple images at once from a given folder
✂ Resize to any width & height
🔄 Optional format conversion (e.g., PNG → JPEG)
💾 Saves resized images to a separate output folder

Requirements
Python 3.x
Pillow library

Install dependencies:
pip install pillow

Usage
1️⃣ Prepare Folders
Create a folder named input_images and place all the images you want to resize inside it.
put the path of the folder(input_images) to the input_folder variable.
The script will create resized_images automatically to store the output.

2️⃣ Run the Script
python image_resizer_batch.py
