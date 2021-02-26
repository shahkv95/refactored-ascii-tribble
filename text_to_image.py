from PIL import Image, ImageDraw                  # PIL - Python Imaging Library
import os                                         # provides functionalities to be carried upon directories

def main():

    # Name of the file to be created
    image_name = "new_image.png"

    # Create the image
    create_image = Image.new(mode = "RGB", size = (250,100), color = "blue")      # creates new image with given mode, size and color

    # Save the image
    create_image.save(image_name)

    # Open the image
    current_directory = os.getcwd()
    image_address = current_directory +"/" + image_name
    print(current_directory +"/" + image_name)
    opening_image = Image.open(image_address)
    opening_image.show()


if __name__ == "__main__":
    main()