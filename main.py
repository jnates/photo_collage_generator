from pathlib import Path 
from itertools import cycle 
from PIL import Image

path = Path("/gdrive/MyDrive/Colab/data/aumentadas_buenas") # Image folder path to include in collage

from pathlib import Path 
from itertools import cycle
 
from PIL import Image

colors = (
    (255, 255, 255),
    (255, 211, 51),
    (255, 231, 113),
    (112, 164, 203),
    (83, 144, 193),
    (67, 133, 187),
    (61, 121, 170),
    (48, 106, 153),
)

def most_frequent_color(image):
    w, h = image.size
    pixels = image.getcolors(w * h)
    most_frequent_pixel = pixels[0]
    for count, color in pixels:
      if count > most_frequent_pixel[0]:
          most_frequent_pixel = color

      if len(most_frequent_pixel) == 2:
          return most_frequent_pixel[1]
      else:
          return most_frequent_pixel

def closer_to(rgb, colors):
    closer = None
    _dist = None
    for i, color in enumerate(colors):
        dist = (
            (rgb[0] - color[0])**2 +
            (rgb[1] - color[1])**2 + 
            (rgb[2] - color[2])**2
        )
        if _dist is None:
            closer = i
            _dist = dist
        if dist < _dist:
            closer = i
            _dist = dist
    return closer

ref_im = Image.open("/gdrive/MyDrive/Colab/fondo.jpg") # original image
w, h = 30, 30
ref_im = ref_im.resize((w, h))
bg_im = ref_im.resize((w * 125, h * 125)) # original image 25 times bigger


