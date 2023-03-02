# run pip install pillow to install
from PIL import Image
import math
import sys

def flip(image,question_identity):
    width, height = image.size
    r, g, b = image.getpixel((50, 50))
    new_image = Image.new("RGB", (image.size), "white")
    print("Dear " +question_identity+ ", would you like to flip your image vertically or horizontally?")
    print("Your options are: Horizontal/Vertical")
    flip_question = input("")
    if flip_question.lower() == "horizontal":
        horizontal = image.transpose(Image.FLIP_LEFT_RIGHT)
        horizontal.show()
    if flip_question.lower() == "vertical":
        vertical = image.transpose(Image.FLIP_TOP_BOTTOM)
        vertical.show()

def shrink(image,question_identity):
    width, height = image.size
    r, g, b = image.getpixel((50, 50))
    new_image = Image.new("RGB", (image.size), "white")
    shrink_question = int(input(+question_identity+ "by how much would you like to shrink your image\n"))
    shrunk_width = int(width // shrink_question)
    shrunk_height = int(height // shrink_question)
    shrunk_image = ((shrunk_width, shrunk_height))
    for new_width in range(1, shrunk_width):
        for new_height in range(1, shrunk_height):
            new_image[new_width, new_height] = image[50 + new_width, 50 + new_height]
            new_image.save('new.jpg',new_image)
            new_image.show()

def hide(image,question_identity):
    width, height = image.size
    r, g, b = image.getpixel((50, 50))
    new_image = Image.new("RGB", (image.size), "white")
    choice_of_hide = input(+question_identity+ "Do you want to hide an image or a message?\n")
    if choice_of_hide == "message":
        secret_message = input("what is your secret message?\n")
        split_message = ([*secret_message])
        for character in split_message:
            for x in range(width):
                for y in range(height):
                    r,g,b = image.getpixel((x,y))
                    r = (bin(r)[2:6])
                    g = (bin(g)[2:6])
                    b = b
                    unfiltered_binary_character = bin(ord(character))
                    first_half_filtered_binary_character = ((unfiltered_binary_character)[2:6])
                    second_half_filtered_binary_character = ((unfiltered_binary_character)[7:10])
                    hidden_r = int(r + first_half_filtered_binary_character)
                    hidden_g = int(g + second_half_filtered_binary_character)
                    new_image.putpixel((x,y), (hidden_r,hidden_g,b))
                    #print(hidden_r)
                    #print(hidden_g)
                    #x+1
                    #y+1
        if character == split_message[-1]:
            for x in range(width):
                for y in range(height):
                    r,g,b = image.getpixel((x,y))
                    new_image.putpixel((x,y), (r,g,b))
        new_image.show()
    if choice_of_hide == "image" or "phot":


def main():
    # Open image
    image = Image.open('jump.jpeg')

    # Show image
    #image.show()

    # get the height and width
    width, height = image.size

    # get the rgb values of a pixel at a certain coordinate
    r, g, b = image.getpixel((50, 50))
    
    # create a new image of the same size as the original
    new_image = Image.new("RGB", (image.size), "white")


    # place a pixel from the original image into the new image
    new_image.putpixel((50, 50), (r, g, b))


    question_identity = input("How would you like to be addressed?\n")
    print("Would you like to Flip, Shrink, or Hide your photo?")
    print("Your options are: Flip/Shrink/Hide")
    question = input("")
    if question.lower() == "flip":
        flip(image,question_identity)
    if question.lower() == "shrink":
        shrink(image,question_identity)
    if question.lower() == "hide":
        hide(image,question_identity)

if __name__ == "__main__":
    main()