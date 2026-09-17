import json
from pathlib import Path

def save_json(data, path):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2), encoding="utf-8")
    return path

def make_summary(path, stats, quality, shapes):
    lines = [
        "VISIONCHECK ANALYSIS",
        "=" * 40,
        f"Image: {path}",
        f"Size: {stats['width']} x {stats['height']}",
        f"Channels: {stats['channels']}",
        f"Sharpness: {quality['sharpness']} ({quality['sharpness_label']})",
        f"Brightness: {quality['brightness']} ({quality['lighting_label']})",
        f"Contrast: {quality['contrast']}",
        f"Detected shapes: {len(shapes)}",
        "",
        "Shape details:"
    ]
    for i, shape in enumerate(shapes, 1):
        lines.append(f"{i}. {shape['shape']} | area={shape['area']} | box={shape['width']}x{shape['height']}")
    return "\n".join(lines) + "\n"
