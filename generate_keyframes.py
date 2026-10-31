#!/usr/bin/env python3
"""生成两个方向的关键帧静态图"""
import numpy as np
from PIL import Image, ImageDraw, ImageFont
import math

def create_direction_a_keyframe():
    """方向 A: 赛博解剖 - 电机剖面图"""
    img = Image.new('RGB', (1920, 1080), color='#0a0e1a')
    draw = ImageDraw.Draw(img, 'RGBA')

    cx, cy = 960, 540

    # 绘制网格背景
    for i in range(0, 1920, 40):
        draw.line([(i, 0), (i, 1080)], fill=(102, 119, 153, 25), width=1)
    for i in range(0, 1080, 40):
        draw.line([(0, i), (1920, i)], fill=(102, 119, 153, 25), width=1)

    # 外壳圆
    draw.ellipse([cx-280, cy-280, cx+280, cy+280], outline=(0, 217, 255), width=3)

    # 定子圆
    draw.ellipse([cx-220, cy-220, cx+220, cy+220], outline=(0, 217, 255, 153), width=3)

    # 定子线圈（12个）
    for i in range(12):
        angle = (i / 12) * math.pi * 2
        x = cx + math.cos(angle) * 220
        y = cy + math.sin(angle) * 220
        draw.ellipse([x-15, y-15, x+15, y+15], fill=(0, 217, 255))
        draw.line([(cx, cy), (x, y)], fill=(0, 217, 255, 76), width=1)

    # 内转子圆
    draw.ellipse([cx-140, cy-140, cx+140, cy+140], outline=(255, 51, 102), width=4)

    # 转子磁极（8个）
    for i in range(8):
        angle = (i / 8) * math.pi * 2 + math.pi / 8
        x1 = cx + math.cos(angle) * 100
        y1 = cy + math.sin(angle) * 100
        x2 = cx + math.cos(angle) * 140
        y2 = cy + math.sin(angle) * 140
        draw.line([(x1, y1), (x2, y2)], fill=(255, 51, 102), width=6)

    # 中心辉光（用渐变圆模拟）
    for r in range(80, 0, -2):
        alpha = int(255 * (1 - r/80) * 0.3)
        draw.ellipse([cx-r, cy-r, cx+r, cy+r],
                     fill=(255, 51, 102, alpha))

    # 中心点
    draw.ellipse([cx-12, cy-12, cx+12, cy+12], fill=(255, 255, 255))

    # 轴承环
    draw.ellipse([cx-90, cy-90, cx+90, cy+90], outline=(102, 119, 153, 178), width=2)
    draw.ellipse([cx-70, cy-70, cx+70, cy+70], outline=(102, 119, 153, 178), width=2)

    # 编码器指示线
    draw.line([(cx, cy-140), (cx, cy-300)], fill=(0, 217, 255), width=2)
    draw.ellipse([cx-8, cy-308, cx+8, cy-292], fill=(0, 217, 255))

    # 扫描线
    for i in range(5):
        y = 200 + i * 200
        draw.line([(0, y), (1920, y)], fill=(0, 217, 255, 128), width=1)

    # 文字（使用默认字体）
    try:
        font_title = ImageFont.truetype("arial.ttf", 48)
        font_sub = ImageFont.truetype("arial.ttf", 32)
        font_small = ImageFont.truetype("arial.ttf", 24)
    except:
        font_title = ImageFont.load_default()
        font_sub = ImageFont.load_default()
        font_small = ImageFont.load_default()

    draw.text((1200, 400), "PMSM", fill=(255, 255, 255), font=font_title)
    draw.text((1200, 460), "LOW INERTIA", fill=(0, 217, 255), font=font_sub)
    draw.text((1200, 510), "DUAL ENCODERS", fill=(0, 217, 255), font=font_sub)
    draw.text((1200, 580), "HIGH-SPEED INNER ROTOR", fill=(102, 119, 153), font=font_small)
    draw.text((1200, 620), "CROSSED ROLLER BEARING", fill=(102, 119, 153), font=font_small)
    draw.text((1200, 660), "LOCAL AIR COOLING", fill=(102, 119, 153), font=font_small)

    img.save('direction_a_keyframe.png')
    print('Direction A keyframe saved: direction_a_keyframe.png')

def create_direction_b_keyframe():
    """方向 B: 机械芭蕾 - 粒子流电机"""
    img = Image.new('RGB', (1920, 1080), color='#000000')
    draw = ImageDraw.Draw(img, 'RGBA')

    cx, cy = 960, 540

    # 生成粒子
    np.random.seed(42)

    # 螺旋粒子（蓝色）
    for i in range(200):
        angle = (i / 200) * math.pi * 8
        radius = 150 + math.sin(angle * 3) * 50
        x = cx + math.cos(angle) * radius
        y = cy + math.sin(angle) * radius
        alpha = int(255 * (1 - i/200))
        size = 2 + int(3 * (1 - i/200))
        draw.ellipse([x-size, y-size, x+size, y+size],
                     fill=(99, 102, 241, alpha))

    # 辐射粒子（金色）
    for i in range(300):
        angle = np.random.random() * math.pi * 2
        distance = np.random.random() * 300
        x = cx + math.cos(angle) * distance
        y = cy + math.sin(angle) * distance
        alpha = int(255 * (1 - distance/300))
        size = 1 + int(2 * (1 - distance/300))
        draw.ellipse([x-size, y-size, x+size, y+size],
                     fill=(251, 191, 36, alpha))

    # 电机轮廓
    draw.ellipse([cx-200, cy-200, cx+200, cy+200],
                 outline=(99, 102, 241, 153), width=3)
    draw.ellipse([cx-120, cy-120, cx+120, cy+120],
                 outline=(99, 102, 241, 153), width=3)

    # 磁场线（8条旋转）
    for i in range(8):
        angle = (i / 8) * math.pi * 2 + math.pi / 4
        x1 = cx + math.cos(angle) * 80
        y1 = cy + math.sin(angle) * 80
        x2 = cx + math.cos(angle) * 200
        y2 = cy + math.sin(angle) * 200

        # 渐变线（用多段模拟）
        for j in range(10):
            t = j / 10
            x = x1 + (x2 - x1) * t
            y = y1 + (y2 - y1) * t
            alpha = int(255 * (1 - t))
            draw.ellipse([x-2, y-2, x+2, y+2],
                         fill=(139, 92, 246, alpha))

    # 中心能量球
    for r in range(100, 0, -2):
        alpha = int(255 * (1 - r/100) ** 0.5 * 0.8)
        draw.ellipse([cx-r, cy-r, cx+r, cy+r],
                     fill=(251, 191, 36, alpha))

    # 核心点
    draw.ellipse([cx-8, cy-8, cx+8, cy+8], fill=(255, 255, 255))

    # 外圈辉光
    for r in range(400, 200, -10):
        alpha = int(255 * (1 - (r-200)/200) * 0.2)
        draw.ellipse([cx-r, cy-r, cx+r, cy+r],
                     fill=(99, 102, 241, alpha))

    # 文字
    try:
        font_title = ImageFont.truetype("simhei.ttf", 56)
        font_sub = ImageFont.truetype("simhei.ttf", 36)
        font_small = ImageFont.truetype("simhei.ttf", 28)
    except:
        try:
            font_title = ImageFont.truetype("arial.ttf", 56)
            font_sub = ImageFont.truetype("arial.ttf", 36)
            font_small = ImageFont.truetype("arial.ttf", 28)
        except:
            font_title = ImageFont.load_default()
            font_sub = ImageFont.load_default()
            font_small = ImageFont.load_default()

    draw.text((1700, 350), "永磁同步电机", fill=(255, 255, 255),
              font=font_title, anchor="rm")
    draw.text((1700, 420), "低惯量内转子", fill=(99, 102, 241),
              font=font_sub, anchor="rm")
    draw.text((1700, 470), "双编码器", fill=(99, 102, 241),
              font=font_sub, anchor="rm")
    draw.text((1700, 560), "HIGH-SPEED ROTATION", fill=(139, 92, 246, 204),
              font=font_small, anchor="rm")
    draw.text((1700, 610), "MAGNETIC FIELD", fill=(139, 92, 246, 204),
              font=font_small, anchor="rm")

    img.save('direction_b_keyframe.png')
    print('Direction B keyframe saved: direction_b_keyframe.png')

if __name__ == '__main__':
    print('Generating keyframes...')
    create_direction_a_keyframe()
    create_direction_b_keyframe()
    print('Done!')
