# run pip install pillow to install
from PIL import Image
import math
import sys

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
    new_image2 = Image.new("RGB", (image.size), "white")


    # place a pixel from the original image into the new image
    new_image.putpixel((50, 50), (r, g, b))
    new_image2.putpixel((50, 50), (r, g, b))

    grayscale_question = input("Would you like to grayscale your photo?\n")
    if grayscale_question[0] == "y":
        grayscale_type = input("do you want to use method 1 or 2?\n")
        if grayscale_type == "1" or "method 1":
            for x in range(width):
                for y in range(height):
                    r,g,b = image.getpixel((x,y))
                    new_image.putpixel((x,y), (math.floor(r+g+b/3)))
            new_image.show()
        if grayscale_type == "2" or "method 2": 
            for x in range(width):
                for y in range(height):
                    r,g,b = image.getpixel((x,y))
                    new_image2.putpixel((x,y), (math.floor(r/3), math.floor(g/3), math.floor(b/3)))
            new_image2.show()
    if grayscale_question[0] == "n":
            sys.exit()

if __name__ == "__main__":
    main()

