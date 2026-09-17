import cv2

def resize_image(image, max_width=1000):
    height, width = image.shape[:2]
    if width <= max_width:
        return image
    scale = max_width / width
    return cv2.resize(image, (int(width * scale), int(height * scale)))

def to_grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

def denoise(image):
    return cv2.GaussianBlur(image, (5, 5), 0)

def edge_map(image):
    gray = to_grayscale(image)
    smooth = denoise(gray)
    return cv2.Canny(smooth, 50, 150)
