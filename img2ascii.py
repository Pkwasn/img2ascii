from PIL import Image

#Adjust noaiv value when changing ASCII number of ascii characters

ASCII_CHARS = ['@','#','%','$','?','*','+','~',':',';',' ']
#ASCII_CHARS = ['@','#',"%",'$','&','?','W','G','P'] #Alernative ASCII Chars

HEIGHT_MODIFIER = .8
NEW_WIDTH = 150
NOAIV = 25

def resize_image(image, new_width):
    """Resizes image while maintaining aspect ratio"""

    width, height = image.size
    aspect_ratio = height/float(width)
    new_height = int(new_width * aspect_ratio * HEIGHT_MODIFIER)

    return image.resize((new_width, new_height))

def grayscale_image(image):
    """Convert Image to grayscale"""
    return image.convert('L')

def pixel_to_ascii(image):
    """For every pixel in image.getdata(), add a ascii character of 
    corresponding pixel_intesity. Under normal operation,
    the image will already be resized

    noaiv = number of ascii intensity values """
    pixels = list(image.getdata())
    
    ascii_pixels = ''
    for pixel_intensity in pixels:
        ascii_pixels += ASCII_CHARS[pixel_intensity//NOAIV]

    return ''.join(ascii_pixels)

def main(path):
    '''Opens image, checking for exceptions. Then manipulates
    image using helper methods from above. Finally, writes the
    completed image to a file named: "ascii.txt" '''
    try:
        image = Image.open(path)
    except Exception:
        print(f'Unable to find image in {path}')
        return

    image = resize_image(image, NEW_WIDTH)
    image = grayscale_image(image)

    pixels = pixel_to_ascii(image)
        
    #Puts the image together by looping through the text and creating
    #a new line at every NEW_WIDTH (which is the total length of a row)
    new_image = ''
    for chars in range(0, len(pixels), NEW_WIDTH):
        new_image += pixels[chars:chars+NEW_WIDTH] + '\n'
    
    f = open('ascii.txt','w')
    f.write(new_image)
    f.close()

if __name__ == '__main__':
    import sys

    path = sys.argv[1]
    main(path)
