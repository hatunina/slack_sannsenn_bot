"""
コラージュ生成関連
"""

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFilter


def collage_generate_pipeline(icon_image):
    # 素材画像を開く
    challenger_format = open_image()
    # 素材画像にアイコンを貼り付け
    back_im = back_image_generate(challenger_format, icon_image)
    # マスク処理と複合処理
    im = mask_image(challenger_format, back_im)

    return im


def open_image():
    # 素材画像を開く
    challenger_format = Image.open('./images/challenger.jpg')
    return challenger_format


def back_image_generate(challenger_format, icon):
    # 素材画像にアイコンを貼り付け
    back_im = challenger_format.copy()
    # x, y
    back_im.paste(icon, (580, 80))
    return back_im


def mask_image(challenger_format, back_im):
    # マスク処理と複合処理
    mask = Image.new("L", back_im.size, 0)
    draw = ImageDraw.Draw(mask)

    # 楕円を切り抜く（x0, y0, x1, y1）
    draw.ellipse((650, 90, 1030, 590), fill=255)

    # 枠をぼやかす
    mask_blur = mask.filter(ImageFilter.GaussianBlur(10))
    im = Image.composite(back_im, challenger_format, mask_blur)

    return im





