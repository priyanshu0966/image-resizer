import os
from PIL import Image

# ==== CONFIGURATION ====
input_folder = r"C:\Users\labhp\Desktop\input_images"      # Copy your folder path where you have saved the images.
output_folder = "resized_images"   # Folder to save resized images
new_width = 800                    # Desired width
new_height = 600                   # Desired height
convert_format = "JPEG"            # Change format: "JPEG", "PNG", etc.
# ========================

# Create output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Loop through files in input folder
for filename in os.listdir(input_folder):
    if filename.lower().endswith((".png", ".jpg", ".jpeg", ".bmp", ".gif")):
        img_path = os.path.join(input_folder, filename)

        # Open image
        img = Image.open(img_path)

        # Resize image
        img_resized = img.resize((new_width, new_height))

        # Create output file path
        name, _ = os.path.splitext(filename)
        output_file = f"{name}.{convert_format.lower()}"
        output_path = os.path.join(output_folder, output_file)

        # Save image
        img_resized.save(output_path, convert_format)
        print(f"✅ Resized and saved: {output_path}")

print("🎉 All images resized successfully!")
