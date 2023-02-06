# run pip install pillow to install
from PIL import Image
import math

def main():
    # Open image
    image = Image.open('jump.jpeg')

    # Show image
    image.show()

    # get the height and width
    width, height = image.size

    # get the rgb values of a pixel at a certain coordinate
    r, g, b = image.getpixel((50, 50))
    
    # create a new image of the same size as the original
    new_image = Image.new("RGB", (image.size), "white")

    # place a pixel from the original image into the new image
    new_image.putpixel((50, 50), (r, g, b))

    for x in range(width):
        for y in range(height):
            r,g,b = image.getpixel((x,y))
            new_image.putpixel((x,y), (math.floor(r/2), math.floor(g/2), math.floor(b/2)))

    # open the new image
    new_image.show()


if __name__ == "__main__":
    main()