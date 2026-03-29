"""Generate OG image and default blog thumbnail for dccartagena.github.io."""
from PIL import Image, ImageDraw, ImageFont
import os

BASE_DIR = "/home/dccartagena/projects/dccartagena.github.io"

# Brand colors
TEAL      = (96, 165, 250)
BG_TOP    = (10, 15, 25)
BG_BOT    = (20, 30, 46)
TEXT_MAIN = (241, 245, 249)
TEXT_MUTE = (148, 163, 184)
TEXT_DIM  = (55, 65, 81)

FONT_PATHS = [
    "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
    "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf",
    "/usr/share/fonts/truetype/freefont/FreeSansBold.ttf",
]
FONT_PATHS_REG = [
    "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
    "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf",
    "/usr/share/fonts/truetype/freefont/FreeSans.ttf",
]


def load_font(paths, size):
    for p in paths:
        if os.path.exists(p):
            return ImageFont.truetype(p, size)
    return ImageFont.load_default()


def gradient_bg(draw, w, h, top=BG_TOP, bottom=BG_BOT):
    for y in range(h):
        t = y / h
        r = int(top[0] + (bottom[0] - top[0]) * t)
        g = int(top[1] + (bottom[1] - top[1]) * t)
        b = int(top[2] + (bottom[2] - top[2]) * t)
        draw.line([(0, y), (w, y)], fill=(r, g, b))


def create_og_image():
    w, h = 1200, 630
    img = Image.new("RGB", (w, h))
    draw = ImageDraw.Draw(img)

    gradient_bg(draw, w, h)

    # Left teal accent bar
    draw.rectangle([(0, 0), (10, h)], fill=TEAL)

    # Top-right decorative corner triangle (dark panel)
    draw.polygon([(w - 280, 0), (w, 0), (w, 280)], fill=(18, 28, 44))
    # Subtle diagonal stripes inside corner
    for i in range(6):
        x0 = w - 280 + i * 45
        draw.line([(x0, 0), (w, 280 - i * 45)], fill=(25, 38, 58), width=1)

    # Bottom teal accent strip
    draw.rectangle([(10, h - 6), (w, h)], fill=(30, 64, 140))

    # Fonts
    f_xl  = load_font(FONT_PATHS,     72)
    f_lg  = load_font(FONT_PATHS,     34)
    f_md  = load_font(FONT_PATHS_REG, 26)
    f_sm  = load_font(FONT_PATHS_REG, 22)

    # Name
    name = "J.D. Cardenas Cartagena"
    draw.text((80, 190), name, font=f_xl, fill=TEXT_MAIN)

    # Teal underline below name
    bbox = draw.textbbox((80, 190), name, font=f_xl)
    draw.rectangle([(80, bbox[3] + 8), (min(bbox[2], w - 280), bbox[3] + 13)], fill=TEAL)

    # Sub-labels
    draw.text((80, bbox[3] + 30), "Researcher  ·  ML Engineer  ·  Safe AI", font=f_lg, fill=TEAL)
    draw.text((80, bbox[3] + 82), "Trustworthy AI for Safety-Critical Systems", font=f_md, fill=TEXT_MUTE)

    # Site URL bottom-left
    draw.text((80, h - 65), "dccartagena.github.io", font=f_sm, fill=TEXT_DIM)

    out = os.path.join(BASE_DIR, "images", "og-default.png")
    img.save(out)
    print(f"  ✓ {out}")


def create_blog_thumbnail():
    w, h = 800, 450
    img = Image.new("RGB", (w, h))
    draw = ImageDraw.Draw(img)

    gradient_bg(draw, w, h, top=(10, 15, 25), bottom=(18, 27, 40))

    # Left teal accent bar
    draw.rectangle([(0, 0), (8, h)], fill=TEAL)

    # Top-right decorative corner
    draw.polygon([(w - 200, 0), (w, 0), (w, 200)], fill=(16, 26, 40))
    for i in range(5):
        x0 = w - 200 + i * 38
        draw.line([(x0, 0), (w, 200 - i * 38)], fill=(22, 35, 52), width=1)

    # Bottom teal strip
    draw.rectangle([(8, h - 5), (w, h)], fill=(30, 64, 140))

    # Fonts
    f_lg  = load_font(FONT_PATHS,     44)
    f_md  = load_font(FONT_PATHS_REG, 22)
    f_sm  = load_font(FONT_PATHS_REG, 18)

    draw.text((50, 155), "J.D. Cardenas Cartagena", font=f_lg, fill=TEXT_MAIN)

    bbox = draw.textbbox((50, 155), "J.D. Cardenas Cartagena", font=f_lg)
    draw.rectangle([(50, bbox[3] + 6), (min(bbox[2], w - 160), bbox[3] + 10)], fill=TEAL)

    draw.text((50, bbox[3] + 22), "Blog", font=f_md, fill=TEAL)
    draw.text((50, h - 44), "dccartagena.github.io", font=f_sm, fill=TEXT_DIM)

    out = os.path.join(BASE_DIR, "images", "blog-thumbnail-default.png")
    img.save(out)
    print(f"  ✓ {out}")


if __name__ == "__main__":
    print("Generating images...")
    create_og_image()
    create_blog_thumbnail()
    print("Done.")
