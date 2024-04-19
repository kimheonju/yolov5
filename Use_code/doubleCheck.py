import os
import hashlib
from PIL import Image

def dhash(image, hash_size=8):
    resized = image.resize((hash_size + 1, hash_size))
    diff = []
    for row in range(hash_size):
        for col in range(hash_size):
            pixel_left = resized.getpixel((col, row))
            pixel_right = resized.getpixel((col + 1, row))
            diff.append(pixel_left > pixel_right)
    return hashlib.md5(bytes(map(int, diff))).hexdigest()

def find_duplicates(directory):
    hashes = {}
    for foldername, subfolders, filenames in os.walk(directory):
        for filename in filenames:
            filepath = os.path.join(foldername, filename)
            try:
                with Image.open(filepath) as img:
                    h = dhash(img)
                    if h in hashes:
                        hashes[h].append(filepath)
                    else:
                        hashes[h] = [filepath]
            except Exception as e:
                print(f"Error with {filepath}: {e}")
    
    for k, v in hashes.items():
        if len(v) > 1:
            for filepath in v[1:]:
                os.remove(filepath)
                print(f"Removed duplicate: {filepath}")

# Example Usage
find_duplicates("C:/Users/khj/Desktop/goose")
