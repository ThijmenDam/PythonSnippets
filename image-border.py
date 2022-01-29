# Author: T. M. Dam
# Created on: 29/01/2022

# File Name: image-border.py
# Description: quickly add a (customizable) border to an image via the command line

import os
import sys
import argparse
from PIL import Image, ImageOps, ImageDraw


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument('file')
    parser.add_argument('--border-color', default='white')
    parser.add_argument('--border-width', default=10)
    parser.add_argument('--border-radius', default=20)

    args = parser.parse_args()

    if not os.path.isfile(args.file):
        print(f"ERROR: '{args.file}' not found")

    savepath = f"{args.file.split('.')[0]}_border.png"

    img = Image.open(args.file)

    if int(args.border_radius) == 0:
        img = ImageOps.expand(img, border=args.border_width, fill=args.border_color)
        img.save(savepath)
        return

    w, h = img.size
    alpha = Image.new('RGBA', (w + args.border_width * 2, h + args.border_width * 2), (255, 0, 0, 0))
    alpha.paste(img, (args.border_width, args.border_width))

    draw = ImageDraw.Draw(alpha)
    draw.rounded_rectangle(
        (2, 2, float(img.width) + 2 * args.border_width - 2, float(img.height) + 2 * args.border_width - 2),
        radius=args.border_radius,
        outline=args.border_color,
        width=args.border_width,
    )

    alpha.save(savepath)

if __name__ == "__main__":
    main()
