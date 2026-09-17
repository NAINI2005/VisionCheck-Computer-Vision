import cv2

def classify_contour(contour):
    perimeter = cv2.arcLength(contour, True)
    if perimeter == 0:
        return "unknown"
    approx = cv2.approxPolyDP(contour, 0.04 * perimeter, True)
    vertices = len(approx)
    if vertices == 3:
        return "triangle"
    if vertices == 4:
        x, y, w, h = cv2.boundingRect(approx)
        ratio = w / h if h else 0
        return "square/rectangle" if 0.9 <= ratio <= 1.1 else "rectangle"
    circularity = 4 * 3.14159 * cv2.contourArea(contour) / (perimeter * perimeter)
    if circularity > 0.75:
        return "circle/round"
    return "irregular"

def find_shapes(image, min_area=500):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 50, 150)
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    shapes = []
    for contour in contours:
        area = cv2.contourArea(contour)
        if area < min_area:
            continue
        x, y, w, h = cv2.boundingRect(contour)
        shapes.append({
            "shape": classify_contour(contour),
            "area": round(float(area), 2),
            "x": int(x), "y": int(y), "width": int(w), "height": int(h)
        })
    return sorted(shapes, key=lambda item: item["area"], reverse=True)

def draw_shape_boxes(image, shapes):
    output = image.copy()
    for item in shapes:
        x, y = item["x"], item["y"]
        w, h = item["width"], item["height"]
        cv2.rectangle(output, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(output, item["shape"], (x, max(20, y - 8)),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)
    return output
