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

    question_identity = input("How would you like to be addressed?\n")
    print("Would you like to Flip, Shrink, or Hide your photo?")
    print("Your options are: Flip/Shrink/Hide")
    question = input("")
    if question.lower() == "flip":
        print("Dear " +question_identity+ ", would you like to flip your image vertically or horizontally?")
        print("Your options are: Horizontal/Vertical")
        flip_question = input("")
        if flip_question.lower() == "horizontal":
            horizontal = image.transpose(Image.FLIP_LEFT_RIGHT)
            horizontal.show()
        if flip_question.lower() == "vertical":
            vertical = image.transpose(Image.FLIP_TOP_BOTTOM)
            vertical.show()
    if question.lower() == "shrink":
        shrink_question = int(input("by how much would you like to shrink your image\n"))
        shrunk_width = width // shrink_question
        shrunk_height = height // shrink_question
        shrunk_image = ((shrunk_width, shrunk_height))
        shrunk_image.save('my_new_favorite_image.jpg')
        shrunk_image.show()
    #if question.lower() == "hide":

if __name__ == "__main__":
    main()

