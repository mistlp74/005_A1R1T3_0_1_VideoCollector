import cv2
import os

frames = 24.0  # frames per sec

image_folder = "your_folder_path"
video_name = "output_video.mp4"

images = [img for img in sorted(os.listdir(image_folder)) if img.endswith(".png")]

if not images:
    raise ValueError("There is no images in this folder")

first_frame = cv2.imread(os.path.join(image_folder, images[0]))
if first_frame is None:
    raise ValueError(f"Cannot read the first image: {images[0]}")

height, width, _ = first_frame.shape

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(video_name, fourcc, frames, (width, height))

try:
    for image_name in images:
        image_path = os.path.join(image_folder, image_name)
        frame = cv2.imread(image_path)

        if frame is None:
            print(f"Problem with reading: {image_path}")
            continue

        if frame.shape[1] != width or frame.shape[0] != height:
            frame = cv2.resize(frame, (width, height))

        out.write(frame)
finally:
    out.release()

print(f"Video saved: {video_name}")