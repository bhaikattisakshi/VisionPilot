from decision import choose_tool

import streamlit as st
import numpy as np
from PIL import Image

from vision_tools import (
    image_stats,
    count_objects,
    segment_image,
    measure_edges,
)
from decision import choose_tool

st.set_page_config(
    page_title="VisionPilot",
    page_icon="🔬",
    layout="wide",
)

st.title("🔬 VisionPilot")
st.subheader("Natural-Language Image Analysis")
st.write("Upload an image and describe what you want to analyze.")

uploaded_file = st.file_uploader(
    "Upload your image",
    type=["png", "jpg", "jpeg"],
)

request = st.text_input(
    "What would you like to do?",
    placeholder="Example: Count the objects in this image",
)

if uploaded_file is not None:
    pil_image = Image.open(uploaded_file).convert("RGB")
    image = np.array(pil_image)

    st.image(pil_image, caption="Uploaded image", width=500)

    if st.button("Analyze Image", type="primary"):
        if not request.strip():
            st.warning("Please describe what you want to analyze.")
        else:
            selected_tool = choose_tool(request)

            st.write("Selected tool:", selected_tool or "No matching tool")

            if selected_tool == "count_objects":
                result = count_objects(image)
                st.subheader("Object Counting")
                st.metric("Estimated objects", result["count"])
                st.image(
                    result["annotated_image"],
                    caption="Detected object contours",
                )
                st.caption(result["note"])

            elif selected_tool == "segment_image":
                result = segment_image(image)
                st.subheader("Image Segmentation")
                st.image(result["mask"], caption="Segmentation mask")
                st.caption(result["note"])

            elif selected_tool == "measure_edges":
                result = measure_edges(image)
                st.subheader("Edge Detection")
                st.metric("Edge pixels", result["edge_count"])
                st.image(result["edge_image"], caption="Detected edges")
                st.caption(result["note"])

            elif "statistic" in request.lower() or "brightness" in request.lower() or "dimensions" in request.lower():
                result = image_stats(image)
                st.subheader("Image Statistics")
                st.write("Width:", result["width"], "pixels")
                st.write("Height:", result["height"], "pixels")
                st.write("Mean brightness:", result["mean_brightness"])

            else:
                st.warning(
                    "I couldn't match that request to a tool. "
                    "Try asking to count objects, segment the image, "
                    "detect edges, or calculate brightness."
                )

else:
    st.info("Upload an image to start your analysis.")

st.divider()
st.caption("VisionPilot | Local prototype | Python + OpenCV")
