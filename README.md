# VisionCheck — Command-Line Computer Vision Toolkit

A simple Computer Vision project that analyzes an input image from the command line. It performs preprocessing, image-quality analysis, edge detection, contour-based shape detection, and generates JSON/text reports.

## Features
- Image loading and validation
- Grayscale conversion, resizing, Gaussian denoising and Canny edge detection
- Brightness, contrast and sharpness analysis
- Contour detection and basic shape classification
- Annotated image output
- JSON and text reports
- Pytest-based testing

## Tech Stack
- Python 3
- OpenCV
- NumPy
- Matplotlib
- Pytest

## Setup

```bash
python -m venv .venv
.venv\Scripts\activate
python -m pip install -r requirements.txt
```

## Run

```bash
python -m visioncheck sample_data/sample_shapes.png
```

The program creates an `outputs/` folder containing:
- `edges.png`
- `annotated.png`
- `analysis.json`
- `summary.txt`

## Testing

```bash
pytest -q
```

Expected result: 4 tests passed.

## Project Structure

```text
visioncheck/
  __init__.py
  __main__.py
  cli.py
  io_utils.py
  preprocess.py
  features.py
  contours.py
  reporting.py
tests/
sample_data/
docs/
```

## Limitations
This is a basic educational computer vision toolkit. Shape classification is based on contour geometry and is not intended for complex real-world object recognition. Lighting and image quality can affect results.

## Future Scope
- Real-time webcam input
- More object categories
- Machine-learning based classification
- GUI interface
- Batch image processing

## Author
Naini Nautiyal — 24BAI10526
VIT Bhopal University
Course: Computer Vision
