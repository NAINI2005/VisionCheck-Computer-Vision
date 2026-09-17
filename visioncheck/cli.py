import argparse
from pathlib import Path
from .io_utils import load_image, save_image
from .preprocess import edge_map
from .features import basic_stats, image_quality, dominant_color
from .contours import find_shapes, draw_shape_boxes
from .reporting import save_json, make_summary

def build_parser():
    parser = argparse.ArgumentParser(
        description="VisionCheck: command-line computer vision analysis using OpenCV."
    )
    parser.add_argument("image", help="Path to an input image")
    parser.add_argument("--output", default="outputs", help="Output directory")
    parser.add_argument("--min-area", type=float, default=500,
                        help="Minimum contour area for shape detection")
    return parser

def run(args):
    image = load_image(args.image)
    out = Path(args.output)
    out.mkdir(parents=True, exist_ok=True)

    stats = basic_stats(image)
    quality = image_quality(image)
    color = dominant_color(image)
    shapes = find_shapes(image, min_area=args.min_area)

    edges = edge_map(image)
    annotated = draw_shape_boxes(image, shapes)

    edge_path = save_image(str(out / "edges.png"), edges)
    annotated_path = save_image(str(out / "annotated.png"), annotated)

    result = {
        "input": str(Path(args.image)),
        "statistics": stats,
        "quality": quality,
        "dominant_color_bgr_mean": color,
        "shapes": shapes,
        "outputs": {
            "edge_image": str(edge_path),
            "annotated_image": str(annotated_path)
        }
    }

    save_json(result, out / "analysis.json")
    (out / "summary.txt").write_text(make_summary(result), encoding="utf-8")
    print("VisionCheck completed.")
    print(f"Image size      : {stats['width']} x {stats['height']}")
    print(f"Sharpness       : {quality['sharpness']:.1f} ({quality['sharpness_label']})")
    print(f"Lighting        : {quality['brightness']:.2f} ({quality['lighting_label']})")
    print(f"Shapes detected : {len(shapes)}")
    print(f"Results saved   : {out.resolve()}")

def main():
    parser = build_parser()
    args = parser.parse_args()
    run(args)

if __name__ == "__main__":
    main()
