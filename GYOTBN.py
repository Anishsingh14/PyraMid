#Based_on_Numpy_Fundamentals

import os
import numpy as np
from PIL import Image

def generate_thumbnail():
    print("GYOTBN - GET YOUR OWN THUMBNAIL")
    
    # PROVIDE THE FILE PATH
    file_path = input("Enter the path to your image file (e.g., photo.jpg): ").strip()
    
    if not os.path.exists(file_path):
        print("Error: File not found! Please check the path and try again.")
        return

    # IMAGE LOADING INTO A NUMPY ARRAY
    try:
        img = Image.open(file_path)
        img_array = np.array(img)
        print(f"\nImage loaded successfully!")
        print(f"Original Dimensions (Height, Width, Channels): {img_array.shape}")
    except Exception as e:
        print(f"Error in loading image: {e}")
        return

    # IMAGE SLICING FOR THUMBNAIL
    height, width = img_array.shape[0], img_array.shape[1]
    min_dim = min(height, width)
    
    # Calcualting the center bounding box co-ordinates
    start_y = (height - min_dim) // 2
    start_x = (width - min_dim) // 2
    
    # Cropping the central region using array slicing
    cropped_array = img_array[start_y:start_y + min_dim, start_x:start_x + min_dim]

    
    # Skipping pixels uniformly for Downsampling the array
    scale_factor = max(1, min_dim // 200)  # Target ~200x200 px
    thumbnail_array = cropped_array[::scale_factor, ::scale_factor]

    # SAVE YOUR PERSONALIZED OUTPUT
    output_img = Image.fromarray(thumbnail_array)
    output_filename = "personalized_thumbnail.png"
    output_img.save(output_filename)

    print(f"\nSuccess! Thumbnail Generated : {thumbnail_array.shape}")
    print(f"Saved output as: {os.path.abspath(output_filename)}")

if __name__ == "__main__":
    generate_thumbnail()
