import json

def save_json(data, path):
    path.write_text(json.dumps(data, indent=2), encoding="utf-8")

def make_summary(result):
    stats = result["statistics"]
    quality = result["quality"]
    shapes = result["shapes"]
    lines = [
        "VISIONCHECK ANALYSIS",
        "========================================",
        f"Image: {result['input']}",
        f"Size: {stats['width']} x {stats['height']}",
        f"Channels: {stats['channels']}",
        f"Sharpness: {quality['sharpness']} ({quality['sharpness_label']})",
        f"Brightness: {quality['brightness']} ({quality['lighting_label']})",
        f"Contrast: {quality['contrast']}",
        f"Detected shapes: {len(shapes)}",
        "",
        "Shape details:"
    ]
    for index, shape in enumerate(shapes, start=1):
        lines.append(
            f"{index}. {shape['shape']} | area={shape['area']} | "
            f"box={shape['width']}x{shape['height']}"
        )
    return "\n".join(lines) + "\n"
