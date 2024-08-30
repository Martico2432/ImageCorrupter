from PIL import Image, ImageDraw
import tqdm
import random
def corruptimage(fileadress: str):
    """
    Image corrupter:
    Arguments: imagedir
    """
    img = Image.open(fileadress)
    width, height = img.size
    img = img.convert('RGBA')

    for x in tqdm.tqdm(range(width)):
        for y in (range(height)):
            img.putpixel((x, y), (random.randint(0,255), random.randint(0,255), random.randint(0,255),random.randint(0,255)))

    img.save(fileadress)