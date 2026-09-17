import numpy as np
from visioncheck.features import basic_stats, brightness_score, contrast_score
from visioncheck.contours import find_shapes

def test_basic_stats():
    image = np.zeros((100, 200, 3), dtype=np.uint8)
    result = basic_stats(image)
    assert result["width"] == 200
    assert result["height"] == 100
    assert result["channels"] == 3

def test_brightness_black_image():
    image = np.zeros((20, 20, 3), dtype=np.uint8)
    assert brightness_score(image) == 0

def test_contrast_constant_image():
    image = np.full((20, 20, 3), 100, dtype=np.uint8)
    assert contrast_score(image) == 0

def test_shape_detection():
    image = np.zeros((300, 300, 3), dtype=np.uint8)
    import cv2
    cv2.rectangle(image, (60, 60), (230, 230), (255, 255, 255), -1)
    shapes = find_shapes(image, min_area=500)
    assert len(shapes) >= 1
