from PIL import Image, ImageOps

# Load the image
image_path = "./chicago.jpg"
image = Image.open(image_path)

# Invert the image
inverted_image = ImageOps.invert(image.convert("RGB"))

# Save the inverted image
inverted_image_path = "./chicago.jpg"
inverted_image.save(inverted_image_path)

inverted_image_path
