import cv2
import numpy as np

def basic_stats(image):
    h, w = image.shape[:2]
    channels = 1 if image.ndim == 2 else image.shape[2]
    return {"width": w, "height": h, "channels": channels, "pixels": int(w*h)}

def sharpness_score(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return float(cv2.Laplacian(gray, cv2.CV_64F).var())

def brightness_score(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return float(np.mean(gray))

def contrast_score(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return float(np.std(gray))

def dominant_color(image):
    pixels = image.reshape(-1, 3).astype(np.float32)
    mean_bgr = pixels.mean(axis=0)
    b, g, r = [float(x) for x in mean_bgr]
    return {"blue": round(b, 2), "green": round(g, 2), "red": round(r, 2)}

def image_quality(image):
    sharp = sharpness_score(image)
    bright = brightness_score(image)
    contrast = contrast_score(image)

    if sharp < 80:
        sharp_label = "low sharpness"
    elif sharp < 250:
        sharp_label = "moderate sharpness"
    else:
        sharp_label = "high sharpness"

    if bright < 70:
        light_label = "dark"
    elif bright > 190:
        light_label = "bright"
    else:
        light_label = "balanced lighting"

    return {
        "sharpness": round(sharp, 2),
        "brightness": round(bright, 2),
        "contrast": round(contrast, 2),
        "sharpness_label": sharp_label,
        "lighting_label": light_label,
    }
