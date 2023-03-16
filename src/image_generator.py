from PIL import Image, ImageFont, ImageDraw

from pathlib import Path

FOLDER = 'test'

font_paths = Path(f'res/fonts/{FOLDER}').glob('*.ttf')

LETTERS = '6729'

BG_COLOR = '#000000'
FG_COLOR = '#ffffff'

WIDTH = 32
HEIGHT = 32

save_path = Path(f'res/images/{FOLDER}')

for font_path in font_paths:
    font = ImageFont.truetype(font=str(font_path), size=32)

    image = Image.new(mode='RGB', size=(HEIGHT, WIDTH), color=BG_COLOR)

    draw = ImageDraw.Draw(im=image)

    for letter in LETTERS:
        draw.text(xy=(WIDTH/2, HEIGHT/2), text=letter, font=font, fill=FG_COLOR, anchor='mm')

        image.save(fp = save_path / (f"{letter}_{font_path.stem}.png"))

        draw.rectangle(((0,0), image.size), fill=BG_COLOR)

