## [PIL](https://pillow.readthedocs.io/en/stable/index.html)

```python
box = (100, 100, 400, 400)
region = im.crop(box)

# When pasting regions back, the size of the region must match the given region exactly.
region = region.transpose(Image.ROTATE_180)
im.paste(region, box)

def roll(image, delta):
    """Roll an image sideways."""
    xsize, ysize = image.size

    delta = delta % xsize
    if delta == 0: return image

    part1 = image.crop((0, 0, delta, ysize))
    part2 = image.crop((delta, 0, xsize, ysize))
    image.paste(part1, (xsize-delta, 0, xsize, ysize))
    image.paste(part2, (0, 0, xsize-delta, ysize))

    return image

# 转换颜色
img = Image.open('/Users/ayixi/Downloads/1.png')
r, g, b = img.split()
Image.merge('RGB', (b, g, r)).show()

img.resize((128, 128))
img.rotate(45) == img.transpose(Image.ROTATE_45)

out = im.transpose(Image.FLIP_LEFT_RIGHT) # 左右翻转
out = im.transpose(Image.FLIP_TOP_BOTTOM) # 上下翻转

im = im.convert("L")
im = im.convert("RGB")

img.filter(ImageFilter.DETAIL)

img.point(lambda i: i * 3)

# split the image into individual bands
source = im.split()

R, G, B = 0, 1, 2

# select regions where red is less than 100
mask = source[R].point(lambda i: i < 100 and 255)

# process the green band
out = source[G].point(lambda i: i * 0.7)

# paste the processed band back, but only where red was < 100
source[G].paste(out, None, mask)

# build a new multiband image
im = Image.merge(im.mode, source)

img.getbands() -> ('R', 'G', 'B')
```