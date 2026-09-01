"""Generate OG image for SuperDuperSkills — 1200x630."""
from PIL import Image, ImageDraw, ImageFont
import os

W, H = 1200, 630
img = Image.new("RGB", (W, H), "#0c0e13")
draw = ImageDraw.Draw(img)

# Background gradient effect — draw rectangles
for y in range(H):
    r = int(12 + (y / H) * 8)
    g = int(14 + (y / H) * 10)
    b = int(19 + (y / H) * 15)
    draw.line([(0, y), (W, y)], fill=(r, g, b))

# Accent glows
from PIL import ImageFilter
glow = Image.new("RGBA", (W, H), (0, 0, 0, 0))
gd = ImageDraw.Draw(glow)
gd.ellipse([100, 80, 500, 380], fill=(0, 229, 160, 18))
gd.ellipse([700, 200, 1100, 500], fill=(79, 172, 254, 14))
glow = glow.filter(ImageFilter.GaussianBlur(60))
img.paste(Image.alpha_composite(Image.new("RGBA", (W, H), (0, 0, 0, 0)), glow).convert("RGB"), (0, 0))

# Halftone dots
for x in range(0, W, 24):
    for y in range(0, H, 24):
        draw.ellipse([x, y, x+1, y+1], fill=(255, 255, 255, 6))

# Try to find a good font, fallback to default
font_paths = [
    "C:/Windows/Fonts/segoeui.ttf",
    "C:/Windows/Fonts/arial.ttf",
    "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
    "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
]

def get_font(size, bold=False):
    for p in font_paths:
        if os.path.exists(p):
            try:
                return ImageFont.truetype(p, size)
            except:
                pass
    return ImageFont.load_default()

font_title = get_font(64, bold=True)
font_subtitle = get_font(28)
font_badge = get_font(22)
font_stats = get_font(20)

# Badge pill
badge_text = "2,638 SKILLS · 17 CATEGORIES · 30+ SOURCES"
bbox = draw.textbbox((0, 0), badge_text, font=font_badge)
bw = bbox[2] - bbox[0] + 32
bx = (W - bw) // 2
draw.rounded_rectangle([bx, 140, bx + bw, 180], radius=20, fill=(0, 229, 160, 30), outline=(0, 229, 160, 80))
draw.text((bx + 16, 146), badge_text, fill="#00e5a0", font=font_badge)

# Title
title1 = "SuperDuper"
title2 = "Skills"
bbox1 = draw.textbbox((0, 0), title1, font=font_title)
bbox2 = draw.textbbox((0, 0), title2, font=font_title)
tw1 = bbox1[2] - bbox1[0]
tw2 = bbox2[2] - bbox2[0]
total_w = tw1 + tw2 + 16
tx = (W - total_w) // 2
draw.text((tx, 210), title1, fill="#e8e6e1", font=font_title)
draw.text((tx + tw1 + 16, 210), title2, fill="#00e5a0", font=font_title)

# Subtitle
sub = "The Complete AI Agent Skills Catalog"
bbox_s = draw.textbbox((0, 0), sub, font=font_subtitle)
sw = bbox_s[2] - bbox_s[0]
draw.text(((W - sw) // 2, 300), sub, fill="#8b8d97", font=font_subtitle)

# Description line
desc = "Unified skills for Claude Code · Gemini CLI · Codex · Every major AI agent"
bbox_d = draw.textbbox((0, 0), desc, font=font_stats)
dw = bbox_d[2] - bbox_d[0]
draw.text(((W - dw) // 2, 350), desc, fill="#5a5c64", font=font_stats)

# Stats row
stats = [("2,638", "skills"), ("17", "categories"), ("8", "core suite"), ("30+", "sources")]
stat_y = 420
stat_gap = 220
stat_start = (W - (len(stats) - 1) * stat_gap) // 2

for i, (num, label) in enumerate(stats):
    sx = stat_start + i * stat_gap
    # Number
    bbox_n = draw.textbbox((0, 0), num, font=get_font(36, bold=True))
    nw = bbox_n[2] - bbox_n[0]
    draw.text((sx - nw // 2, stat_y), num, fill="#00e5a0", font=get_font(36, bold=True))
    # Label
    bbox_l = draw.textbbox((0, 0), label, font=font_stats)
    lw = bbox_l[2] - bbox_l[0]
    draw.text((sx - lw // 2, stat_y + 44), label, fill="#8b8d97", font=font_stats)

# Bottom accent line
draw.rectangle([0, H - 4, W, H], fill="#00e5a0")

# GitHub URL
url = "github.com/camilolealdev/superduperskills"
bbox_u = draw.textbbox((0, 0), url, font=font_stats)
uw = bbox_u[2] - bbox_u[0]
draw.text(((W - uw) // 2, H - 50), url, fill="#5a5c64", font=font_stats)

# Save
out = os.path.join(os.path.dirname(__file__), "og-image.png")
img.save(out, "PNG", quality=95)
print(f"Saved: {out} ({os.path.getsize(out)} bytes)")
