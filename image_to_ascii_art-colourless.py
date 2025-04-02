from PIL import Image

# Ascii characters arranged from dark to light
ASCII_CHARS = "@%#*+=:. "
ASCII_CHARS = "WQOJCPI. "

def resize_image(image, new_width=100):
    """
    Resizes the image while maintaining the original aspect ratio
    Args:
        image (PIL.image): original image
        new_width (int): desired width 
    Returns:
        new_image (PIL.image): Resized image
    """
    width,height = image.size
    aspect_ratio = height/width
    new_height = int(new_width*aspect_ratio*0.55)
    new_image = image.resize((new_width,new_height))
    return new_image

def pixels_to_ascii(image):
    """
    Maps each pixel to an Ascii character based on intensity
    Args:
        image (PIL.image): Grayscale image
    Returns:
        str (string): Ascii string representing the image
    """

    pixels = image.getdata() # Gets pixel brightness between 0-255
    ascii_str = ""
    for pixel in pixels:
        ascii_char = ASCII_CHARS[pixel//25] # 10 ascii chars: 256/10~25
        ascii_str+=ascii_char
    return ascii_str

def image_to_ascii(path,new_width = 50):
    """
    Converts an image file to ascii art
    Args:
        path (str): path to image file
        new_width (int): Width of ascii output
    """
    try:
        image = Image.open(path)
    except Exception as e:
        print(e)
        return 
    
    image = resize_image(image, new_width)
    image = image.convert("L")
    ascii_str = pixels_to_ascii(image)
    img_width = image.width
    ascii_image = "\n".join(ascii_str[i:i + img_width] for i in range(0, len(ascii_str), img_width))
    print(ascii_image)


image_to_ascii("Virat.png", new_width=100)