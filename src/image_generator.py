"""

"""

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFilter


def image_generate_pipeline(icon_image):
    challenger_format = open_images()
    back_im = back_image_generate(challenger_format, icon_image.resize((500, 500)))
    im = mask_image(challenger_format, back_im)

    return im

def open_images():
    challenger_format = Image.open('./images/challenger.jpg')
    return challenger_format

def back_image_generate(challenger_format, icon):

    back_im = challenger_format.copy()
    back_im.paste(icon, (600, 80))

    return back_im

def mask_image(challenger_format, back_im):

    mask = Image.new("L", back_im.size, 0)
    draw = ImageDraw.Draw(mask)

    # x0, y0, x1, y1
    draw.ellipse((700, 85, 1000, 600), fill=255)

    mask_blur = mask.filter(ImageFilter.GaussianBlur(10))
    im = Image.composite(back_im, challenger_format, mask_blur)

    return im





