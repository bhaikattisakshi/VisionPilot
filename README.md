# 🔬 VisionPilot

**AI-Powered Image Analysis | Python · OpenCV · Streamlit**

VisionPilot is a computer vision project that allows users to upload images and run image-processing operations through a simple web interface.

## Features

- Image statistics and brightness analysis
- Contour-based object counting
- Threshold-based image segmentation
- Canny edge detection
- Rule-based natural-language request routing

## Tech Stack

- Python
- OpenCV
- NumPy
- Pillow
- Streamlit

## Run Locally

1. Clone this repository.
2. Create and activate a Python virtual environment.
3. Install the dependencies.
4. Launch the application.

```bash
pip install streamlit opencv-python pillow numpy
streamlit run app.py
```

## Project Status

**In progress.** The current version uses rule-based request routing. Integration with a real decision model, including Strands Decider 2B, is planned.

## Disclaimer

Object counts and segmentation results are estimates based on traditional image-processing techniques. Results depend on image quality and object separation.

## Author

Sakshi Bhaikatti
