

import cv2
import numpy as np

from vision_tools import (
    image_stats,
    count_objects,
    segment_image,
    measure_edges,
)

# Create a white image with three black circles.
image = np.full((300, 400, 3), 255, dtype=np.uint8)

cv2.circle(image, (80, 100), 30, (0, 0, 0), -1)
cv2.circle(image, (200, 100), 30, (0, 0, 0), -1)
cv2.circle(image, (320, 100), 30, (0, 0, 0), -1)

print("Image statistics:", image_stats(image))

count_result = count_objects(image)
print("Detected objects:", count_result["count"])

seg_result = segment_image(image)
print("Segmentation mask shape:", seg_result["mask"].shape)

edge_result = measure_edges(image)
print("Edge pixels:", edge_result["edge_count"])

cv2.imwrite("test_input.png", image)
cv2.imwrite("test_count.png", count_result["annotated_image"])
cv2.imwrite("test_mask.png", seg_result["mask"])
cv2.imwrite("test_edges.png", edge_result["edge_image"])

print("Test completed! Output images saved.")
