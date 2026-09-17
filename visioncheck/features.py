import cv2
import numpy as np

def basic_stats(image):
    height, width = image.shape[:2]
    channels = 1 if image.ndim == 2 else image.shape[2]
    return {
        "width": width,
        "height": height,
        "channels": channels,
        "pixels": width * height
    }

def brightness_score(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return float(np.mean(gray))

def contrast_score(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return float(np.std(gray))

def sharpness_score(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return float(cv2.Laplacian(gray, cv2.CV_64F).var())

def image_quality(image):
    brightness = brightness_score(image)
    contrast = contrast_score(image)
    sharpness = sharpness_score(image)
    if sharpness >= 1000:
        sharpness_label = "high sharpness"
    elif sharpness >= 150:
        sharpness_label = "medium sharpness"
    else:
        sharpness_label = "low sharpness"
    if brightness < 70:
        lighting_label = "dark"
    elif brightness > 190:
        lighting_label = "bright"
    else:
        lighting_label = "normal lighting"
    return {
        "sharpness": round(sharpness, 2),
        "brightness": round(brightness, 2),
        "contrast": round(contrast, 2),
        "sharpness_label": sharpness_label,
        "lighting_label": lighting_label
    }

def dominant_color(image):
    mean = image.mean(axis=(0, 1))
    return {
        "blue": round(float(mean[0]), 2),
        "green": round(float(mean[1]), 2),
        "red": round(float(mean[2]), 2)
    }
