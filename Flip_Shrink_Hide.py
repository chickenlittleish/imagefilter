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
    shrink_question = int(input(question_identity+ ", by how much would you like to shrink your image\n"))
    shrunk_width = int(width // shrink_question)
    shrunk_height = int(height // shrink_question)
    shrunk_image = ((shrunk_width, shrunk_height))
    for new_width in range(1, shrunk_width):
        for new_height in range(1, shrunk_height):
            new_image[new_width, new_height] = image[50 + new_width, 50 + new_height]
            new_image.save('new.jpg',new_image)
            new_image.show()

def hide(image,question_identity):
    #gets width and height based on image we give
    width, height = image.size
    #creates a blank new image
    #(the RGB tells it it's in RGB format(in color basically),
    #the image size tells it it's the same image size as the original image,
    # the white tells it the image is pure white before we put the pixels)
    new_image2 = Image.new("RGB", (image.size), "white")
    new_image_3 = Image.new("RGB", (image.size), "white")
    #asks the user if they want to hide a message or an image
    choice_of_hide = input(question_identity+ " Do you want to hide an image or a message?\n")
    #if they choose to hide a message, it will run the program for hiding a message
    if choice_of_hide == "message":
        #it will ask for a message to hide
        secret_message = input("what is your secret message?\n")
        #it splits the message into indvidual characters using the unpack method
        split_message = ([*secret_message])
        #gets the width
        for x in range(width):
            #gets the height
            for y in range(height):
                #gets the character for that pixel(width and height)
                for character in split_message:
                    #gets the RGB vales of that pixel
                    r,g,b = image.getpixel((x,y))
                    #makes the R value of RGB into binary and only keeps the first 4 which hold the most value in binary(As the first 4 values are the largest numbers in binary)
                    r = (bin(r)[2:6])
                    #makes the G value of RGB into binary and only keeps the first 4
                    g = (bin(g)[2:6])
                    #do nothing with the B value of RGB as we'll explain later
                    b = b
                    #convert the character into binary(so 8 values)
                    unfiltered_binary_character = bin(ord(character))
                    #split the character's binary sequence into the 4 first binary values
                    first_half_filtered_binary_character = ((unfiltered_binary_character)[2:6])
                    #split the character's binary sequence into the 4 last binary values
                    second_half_filtered_binary_character = ((unfiltered_binary_character)[7:10])
                    #add the first 4 binary values to the binary values of R(as we have 4 left after keeping only the first 4 values)
                    hidden_r = int(r + first_half_filtered_binary_character)
                    #add the last 4 binary values to the binary values of G(as we have 4 left after keeping only the first 4 values)
                    hidden_g = int(g + second_half_filtered_binary_character)
                    #we don't need blue(b/B) as the binary sequence of the character only has 8 values so we only need 8 spaces which are provided by R and G
                    #place the new RGB values in the new image in the same position
                    new_image2.putpixel((x,y), (hidden_r,hidden_g,b))
                    #if we reach the final character(which is -1)
                    if character == split_message[-1]:
                        #get the width
                        for x in range(width):
                            #get the height
                            for y in range(height):
                                #get the RGB value of that pixel(width and heigh)
                                r,g,b = image.getpixel((x,y))
                                #place those RGB values in the same position in the new image
                                new_image2.putpixel((x,y), (r,g,b))
                        #print/show the new image
                        new_image2.show()
                        #exit the system
                        sys.exit()
    if choice_of_hide == "image" or "photo":
        print("What is your secret image/photo?")
        print("Choices are:\nhorse.jpg\nbuster.png\nhyena.jpg\nkitty.png\nlatestart.jpg\nnightbee.png\nowlbear.jpg\nphilip.jpg\nthanksgiving.jpg")
        secret_image = input("What is your secret image/photo?(Choose from the list)\n")
        image2 = Image.open(secret_image)
        image2.show()
        width2, height2 = image2.size
        for x in range(width):
            for y in range(height):
                for x2 in range(width2):
                    for y2 in range(height2):
                        r,g,b = image.getpixel((x,y))
                        r2,g2,b2 = image2.getpixel((x2,y2))
                        r = (bin(r)[2:6])
                        g = (bin(g)[2:6])
                        b = (bin(b)[2:6])
                        r2 = (bin(r2)[2:6])
                        g2 = (bin(g2)[2:6])
                        b2 = (bin(b2)[2:6])
                        hidden_r = int(r + r2)
                        hidden_g = int(g + g2)
                        hidden_b = int(b + b2)
                        new_image_3.putpixel((x,y), (hidden_r,hidden_g,hidden_b))
                        if str(x2) == (str(width2)[-1]) and str(y2) == (str(height2)[-1]):
                            for x in range(width):
                                for y in range(height):
                                    r,g,b = image.getpixel((x,y))
                                    new_image_3.putpixel((x,y), (r,g,b))
                            new_image_3.show()
                            sys.exit()


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