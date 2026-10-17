
import cv2
import numpy as np


def image_stats(image):
    """Return basic information about an RGB image."""
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

    return {
        "width": int(image.shape[1]),
        "height": int(image.shape[0]),
        "mean_brightness": round(float(np.mean(gray)), 2),
    }


def count_objects(image):
    """Estimate object count using thresholding and contours."""
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    _, mask = cv2.threshold(
        blurred,
        0,
        255,
        cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU,
    )

    contours, _ = cv2.findContours(
        mask,
        cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE,
    )

    objects = [
        contour
        for contour in contours
        if cv2.contourArea(contour) >= 20
    ]

    annotated = image.copy()
    cv2.drawContours(
        annotated, objects, -1, (0, 255, 0), 2
    )

    return {
        "count": len(objects),
        "annotated_image": annotated,
        "note": (
            "Estimated count using contours. "
            "Touching objects may be counted as one."
        ),
    }


def segment_image(image):
    """Create a basic foreground/background segmentation mask."""
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    _, mask = cv2.threshold(
        blurred,
        0,
        255,
        cv2.THRESH_BINARY + cv2.THRESH_OTSU,
    )

    return {
        "mask": mask,
        "note": (
            "Otsu threshold segmentation. "
            "The foreground may appear black or white."
        ),
    }


def measure_edges(image):
    """Detect image edges using the Canny algorithm."""
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    edges = cv2.Canny(gray, 80, 160)

    return {
        "edge_count": int(np.count_nonzero(edges)),
        "edge_image": edges,
        "note": (
            "Edge-pixel count, not physical length "
            "or particle size."
        ),
    }
