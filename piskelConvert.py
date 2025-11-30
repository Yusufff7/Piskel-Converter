import json
import base64
from io import BytesIO
from PIL import Image

#----------CONFIG-----------------

#This should be your file name / location
fileName = "shield.piskel"

#Update this to include any custom colors and the letter you would like to be printed when a pixel of that color is encountered
pixelMap = {
    0xFF0000: "R",
    0xFFFF00: "Y",
    0x00FF00: "G",
    0xD2691E: "D",
    0xBFBFBF: "5",
    0x5F5F5F: "3",
    0xFFFFFF: "W",
    0x000000: "Z",
    0x800080: "P"
    # Add more mappings here as needed...
}

#-------------END CONFIG------------

with open(fileName, "r", encoding="utf-8") as f:
    data = json.load(f)

piskel = data["piskel"]
width = int(piskel["width"])
height = int(piskel["height"])

raw_layer = piskel["layers"][0]
layer = json.loads(raw_layer)
chunk = layer["chunks"][0]

b64_png = chunk["base64PNG"]
if "," in b64_png:
    b64_png = b64_png.split(",", 1)[1]

png_bytes = base64.b64decode(b64_png)
image = Image.open(BytesIO(png_bytes)).convert("RGBA")

def pixelColor(x, y):
    r, g, b, a = image.getpixel((x, y))
    return (r << 16) | (g << 8) | b

def pixelLetter(x, y):
    hexVal = pixelColor(x, y)
    return pixelMap[hexVal]

TILE_W = 11
TILE_H = 11

tiles_x = width // TILE_W  
tiles_y = height // TILE_H  

tiles = []  

for tile_row in range(tiles_y):       
    for tile_col in range(tiles_x):   
        sprite_str = ""
        for dy in range(TILE_H):
            for dx in range(TILE_W):
                gx = tile_col * TILE_W + dx  
                gy = tile_row * TILE_H + dy  
                sprite_str += pixelLetter(gx, gy)
        tiles.append((tile_row, tile_col, sprite_str))

for tile_row, tile_col, sprite_str in tiles:
    print(f"Tile ({tile_row}, {tile_col})")
    print(sprite_str)
    print()
