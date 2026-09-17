import cv2

def resize_keep_ratio(image, max_width=900, max_height=700):
    h, w = image.shape[:2]
    scale = min(max_width / w, max_height / h, 1.0)
    if scale == 1.0:
        return image.copy()
    return cv2.resize(image, (int(w * scale), int(h * scale)), interpolation=cv2.INTER_AREA)

def grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

def denoise(image, kernel=5):
    return cv2.GaussianBlur(image, (kernel, kernel), 0)

def edge_map(image):
    gray = grayscale(image)
    smooth = denoise(gray)
    return cv2.Canny(smooth, 70, 160)
