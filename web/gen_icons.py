from PIL import Image, ImageDraw

def make_icon(size):
    img = Image.new('RGBA', (size, size), (12, 14, 19, 255))
    draw = ImageDraw.Draw(img)
    cx, cy = size // 2, size // 2
    s = size * 0.35
    pts = [
        (cx - s*0.15, cy - s*0.85),
        (cx - s*0.55, cy + s*0.05),
        (cx - s*0.05, cy + s*0.05),
        (cx + s*0.15, cy + s*0.85),
        (cx + s*0.55, cy - s*0.05),
        (cx + s*0.05, cy - s*0.05),
    ]
    draw.polygon([pts[0], pts[1], pts[2], pts[5]], fill=(0, 229, 160, 255))
    draw.polygon([pts[2], pts[3], pts[4], pts[5]], fill=(79, 172, 254, 255))
    return img

make_icon(192).save('icon-192.png')
make_icon(512).save('icon-512.png')
print('Done')
