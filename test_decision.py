
from decision import choose_tool

test_cases = [
    ("Count the objects", "count_objects"),
    ("How many particles are there?", "count_objects"),
    ("Create a segmentation mask", "segment_image"),
    ("Separate the foreground from the background", "segment_image"),
    ("Find the boundaries", "measure_edges"),
    ("Detect the edges", "measure_edges"),
    ("Calculate image brightness", "image_stats"),
    ("Tell me a joke", None),
]

failed = 0

for request, expected in test_cases:
    actual = choose_tool(request)
    passed = actual == expected

    print(f"{'PASS' if passed else 'FAIL'} | {request}")
    print(f"Expected: {expected} | Actual: {actual}\n")

    if not passed:
        failed += 1

print(f"Results: {len(test_cases) - failed}/{len(test_cases)} passed")
