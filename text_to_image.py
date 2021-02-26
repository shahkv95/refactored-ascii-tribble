from PIL import Image, ImageDraw       # PIL - Python Imaging Library
import os                   # provides functionalities to be carried upon directories

# Name of the file to be created
image_name = "new_image.png"

# Create the image
create_image = Image.new(mode = "RGB", size = (200,70), color = "red")      # creates new image with given mode, size and color

# Save the image
create_image.save(image_name)

# Open the image
os.system(image_name)
