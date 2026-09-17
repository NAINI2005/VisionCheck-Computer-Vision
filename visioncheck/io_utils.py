from pathlib import Path
import cv2

SUPPORTED_EXTENSIONS = {".jpg", ".jpeg", ".png", ".bmp", ".webp"}

def load_image(path):
    file = Path(path)
    if not file.exists():
        raise FileNotFoundError(f"Image not found: {path}")
    if file.suffix.lower() not in SUPPORTED_EXTENSIONS:
        raise ValueError(f"Unsupported image format: {file.suffix}")
    image = cv2.imread(str(file))
    if image is None:
        raise ValueError("Could not read the image file.")
    return image

def save_image(path, image):
    target = Path(path)
    target.parent.mkdir(parents=True, exist_ok=True)
    if not cv2.imwrite(str(target), image):
        raise IOError(f"Could not save image: {path}")
    return target
