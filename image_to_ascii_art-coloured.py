"""
Code that generates coloured ascii art 
"""
from PIL import Image

# Ascii characters arranged from dark to light
ASCII_CHARS = "@%#*+=:. "

def resize_image(image, new_width=100):
    width, height = image.size
    aspect_ratio = height / width
    new_height = int(new_width * aspect_ratio * 0.55)
    new_image = image.resize((new_width, new_height))
    return new_image

def pixels_to_ascii(img):
    for y in range(img.height):
        for x in range(img.width):
            r, g, b = img.getpixel((x, y))
            brightness = int((r + g + b) / 3)
            index = min(brightness // 32, len(ASCII_CHARS) - 1)
            ascii_char = ASCII_CHARS[index]
            print(f"\033[38;2;{r};{g};{b}m{ascii_char}\033[0m", end="")
        print()

def image_to_ascii(path, new_width=50):
    try:
        image = Image.open(path)
    except Exception as e:
        print(e)
        return 

    image = resize_image(image, new_width)
    image = image.convert("RGB")
    pixels_to_ascii(image)

image_to_ascii("image.png", new_width=100)
