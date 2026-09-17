from pathlib import Path
import cv2

SUPPORTED = {".jpg", ".jpeg", ".png", ".bmp"}

def load_image(path: str):
    file_path = Path(path)
    if not file_path.exists():
        raise FileNotFoundError(f"Image not found: {file_path}")
    if file_path.suffix.lower() not in SUPPORTED:
        raise ValueError("Supported formats: JPG, JPEG, PNG, BMP")
    image = cv2.imread(str(file_path))
    if image is None:
        raise ValueError("OpenCV could not read the image.")
    return image

def save_image(path: str, image):
    out = Path(path)
    out.parent.mkdir(parents=True, exist_ok=True)
    if not cv2.imwrite(str(out), image):
        raise OSError(f"Could not save image to {out}")
    return out
