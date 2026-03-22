import imageio.v2 as imageio
import os

image_folder = "visualizations"

images = []

for file_name in sorted(os.listdir(image_folder)):
    if file_name.endswith(".png"):
        file_path = os.path.join(image_folder, file_name)
        images.append(imageio.imread(file_path))

imageio.mimsave("dashboard_demo.gif", images, duration = 10)

print("✅ GIF created successfully!")