def rgb_to_hex(r, g, b):
    """Convert RGB color to HEX format."""
    hex_color = f"#{r:02x}{g:02x}{b:02x}"
    return hex_color

def hex_to_rgb(hex_color):
    """Convert HEX color to RGB format."""
    hex_color = hex_color.lstrip("#")
    r, g, b = tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
    return (r, g, b)

def rgb_to_hsv(r, g, b):
    """Convert RGB color to HSV format."""
    r, g, b = r / 255.0, g / 255.0, b / 255.0
    cmax = max(r, g, b)
    cmin = min(r, g, b)
    delta = cmax - cmin

    if delta == 0:
        hue = 0
    elif cmax == r:
        hue = ((g - b) / delta) % 6
    elif cmax == g:
        hue = (b - r) / delta + 2
    else:
        hue = (r - g) / delta + 4

    hue = round(hue * 60)
    if hue < 0:
        hue += 360

    saturation = 0 if cmax == 0 else (delta / cmax)
    value = cmax
    return (hue, saturation, value)

def hsv_to_rgb(hue, saturation, value):
    """Convert HSV color to RGB format."""
    c = value * saturation
    x = c * (1 - abs((hue / 60) % 2 - 1))
    m = value - c
    if 0 <= hue < 60:
        r, g, b = c, x, 0
    elif 60 <= hue < 120:
        r, g, b = x, c, 0
    elif 120 <= hue < 180:
        r, g, b = 0, c, x
    elif 180 <= hue < 240:
        r, g, b = 0, x, c
    elif 240 <= hue < 300:
        r, g, b = x, 0, c
    else:
        r, g, b = c, 0, x
    r, g, b = (r + m) * 255, (g + m) * 255, (b + m) * 255
    return (round(r), round(g), round(b))

def convert_color(color, input_format, output_format):
    """Convert color between RGB, HEX and HSV formats."""
    if input_format == "rgb" and output_format == "hex":
        return rgb_to_hex(*color)
    elif input_format == "hex" and output_format == "rgb":
        return hex_to_rgb(color)
    elif input_format == "rgb" and output_format == "hsv":
        return rgb_to_hsv(*color)
    elif input_format == "hsv" and output_format == "rgb":
        return hsv
