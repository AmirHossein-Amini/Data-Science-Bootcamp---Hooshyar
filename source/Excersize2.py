import json

# Function to calculate lens power, focal length, and radius of curvature
def calculate_lens_parameters\
    (object_distance_cm, refractive_index):
    """calculate lens power, focal lenghth and radius of curvature"""

    d0 = object_distance_cm
    di = object_distance_cm # given as in excersize document

    f = 1 / (1/d0 + 1/di)

    P = 100 / f

    R = ((refractive_index - 1) ** 2) / P

    return P, f, R

# Load JSON data
with open("/home/amirhossein/Documents/Data Science Course\
 - Hooshyar/Excersizes/data.json", "r") as file:
    data = json.load(file)

# Process each case
for case in data:
    refractive_error = case["input"]["refractive_error"]
    object_distance_cm = case["input"]["object_distance_cm"]
    refractive_index = case["input"]["refractive_index"]

    # Calculate the lens parameters
    lens_power, focal_length, radius_of_curvature = calculate_lens_parameters(
        object_distance_cm, refractive_index
    )

    print(f"Calculated Lens Power: {lens_power:.2f} diopters")
    print(f"Calculated Focal Length: {focal_length:.2f} cm")
    print(f"Calculated Radius of Curvature: {radius_of_curvature:.4f} m")
    print("-" * 50)