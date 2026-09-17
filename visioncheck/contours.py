import cv2

def find_shapes(image, min_area=500):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    edges = cv2.Canny(blur, 70, 160)
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    results = []
    for contour in contours:
        area = cv2.contourArea(contour)
        if area < min_area:
            continue

        perimeter = cv2.arcLength(contour, True)
        approx = cv2.approxPolyDP(contour, 0.04 * perimeter, True)
        x, y, w, h = cv2.boundingRect(contour)

        if len(approx) == 3:
            shape = "triangle"
        elif len(approx) == 4:
            ratio = w / float(h) if h else 0
            shape = "square/rectangle" if 0.85 <= ratio <= 1.15 else "rectangle"
        elif len(approx) > 7:
            shape = "circle/round"
        else:
            shape = "irregular"

        results.append({
            "shape": shape,
            "area": round(float(area), 2),
            "x": x, "y": y, "width": w, "height": h
        })

    return sorted(results, key=lambda item: item["area"], reverse=True)

def draw_shape_boxes(image, shapes):
    output = image.copy()
    for i, item in enumerate(shapes, start=1):
        x, y, w, h = item["x"], item["y"], item["width"], item["height"]
        cv2.rectangle(output, (x, y), (x+w, y+h), (255, 255, 255), 2)
        text = f"{i}: {item['shape']}"
        cv2.putText(output, text, (x, max(20, y-8)),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.55, (255, 255, 255), 2)
    return output
