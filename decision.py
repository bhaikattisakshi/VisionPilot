
def choose_tool(request_text):
    """Select an image-processing tool from a natural-language request."""
    request = request_text.lower()

    if any(word in request for word in [
        "count", "number", "how many", "particles", "objects"
    ]):
        return "count_objects"

    if any(word in request for word in [
        "segment", "segmentation", "mask",
        "foreground", "background"
    ]):
        return "segment_image"

    if any(word in request for word in [
        "edge", "boundary", "boundaries", "outline"
    ]):
        return "measure_edges"

    if any(word in request for word in [
        "brightness", "statistics", "dimensions",
        "image size", "width", "height"
    ]):
        return "image_stats"

    return None
