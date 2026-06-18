#!/usr/bin/env python3
"""
Latte BGM — Deep Focus / Night Study & Work サムネイル (1280x720)
夜の書斎背景 + 左ダーク帯 + クリーム色タイトル + 金アクセント + 右上統一アイコン。
スタイルは過去 deep_focus_vol4 サムネを踏襲。背景に犬なし／右上は統一アイコン。
"""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageFilter

W, H = 1280, 720
ROOT = Path("/Users/khhr/Desktop/latte-ecosystem")
SRC  = ROOT / "assets/latte_bgm/images/organized/09_DeepFocus_Night/deep_focus_night_001.png"
ICON = ROOT / "assets/latte_bgm/images/brand/latte_dog_icon_circle_v2.png"
OUT  = ROOT / "assets/latte_bgm/thumbnails/deep_focus_night_latte_bgm.jpg"

FONT_BLACK = "/System/Library/Fonts/Supplemental/Arial Black.ttf"
FONT_BOLD  = "/System/Library/Fonts/Supplemental/Arial Bold.ttf"
FONT_REG   = "/System/Library/Fonts/Supplemental/Arial.ttf"

def cover_crop(img):
    scale = max(W / img.width, H / img.height)
    nw, nh = int(img.width * scale), int(img.height * scale)
    img = img.resize((nw, nh), Image.Resampling.LANCZOS)
    left, top = (nw - W) // 2, (nh - H) // 2
    return img.crop((left, top, left + W, top + H))

def font(path, size):
    return ImageFont.truetype(path, size)

def text_shadow(draw, xy, text, fnt, fill, shadow=(0, 0, 0, 200), offset=4):
    x, y = xy
    draw.text((x + offset, y + offset), text, font=fnt, fill=shadow)
    draw.text((x, y), text, font=fnt, fill=fill)

def main():
    base = cover_crop(Image.open(SRC).convert("RGB"))
    base = base.filter(ImageFilter.UnsharpMask(radius=1.2, percent=115, threshold=5))

    # 左ダーク帯（ネイビー寄り）＋金の細枠＋アクセント
    overlay = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    od = ImageDraw.Draw(overlay)
    od.rectangle((0, 0, 720, H), fill=(8, 12, 22, 140))           # 左ネイビー帯
    od.rectangle((0, 0, W, H), outline=(230, 202, 145, 40), width=3)
    od.rectangle((64, 94, 118, 100), fill=(224, 185, 105, 230))   # 上アクセント線
    od.rectangle((64, 612, 470, 616), fill=(224, 185, 105, 190))  # 下アクセント線
    img = Image.alpha_composite(base.convert("RGBA"), overlay)

    draw = ImageDraw.Draw(img)
    title_font = font(FONT_BLACK, 100)
    badge_font = font(FONT_BOLD, 38)
    sub_font   = font(FONT_BOLD, 36)
    brand_font = font(FONT_BOLD, 27)
    small_font = font(FONT_REG, 24)

    # メインタイトル
    text_shadow(draw, (64, 128), "DEEP",  title_font, (255, 248, 226, 255), offset=5)
    text_shadow(draw, (64, 232), "FOCUS", title_font, (255, 248, 226, 255), offset=5)

    # 30 MIN バッジ（金）
    od2 = ImageDraw.Draw(img)
    od2.rounded_rectangle((64, 352, 232, 406), radius=6, fill=(224, 185, 105, 235))
    draw.text((82, 360), "30 MIN", font=badge_font, fill=(18, 16, 12, 255))

    # サブ（用途）
    text_shadow(draw, (64, 442), "NIGHT STUDY", sub_font, (230, 204, 150, 255), offset=3)
    text_shadow(draw, (64, 486), "& WORK BGM",  sub_font, (230, 204, 150, 255), offset=3)

    # ブランド表記（左下）
    draw.text((64, 632), "LATTE BGM", font=brand_font, fill=(255, 245, 218, 245))
    draw.text((64, 664), "Music for Every Moment", font=small_font, fill=(214, 196, 160, 220))

    # 右上 統一アイコン
    icon = Image.open(ICON).convert("RGBA")
    ic_d = 150
    icon = icon.resize((ic_d, ic_d), Image.Resampling.LANCZOS)
    img.alpha_composite(icon, (W - ic_d - 36, 30))

    OUT.parent.mkdir(parents=True, exist_ok=True)
    img.convert("RGB").save(OUT, "JPEG", quality=94, optimize=True)
    print("WROTE:", OUT)

if __name__ == "__main__":
    main()
