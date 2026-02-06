# VideoCollector

## Description

**VideoCollector** is a simple Python script that combines a set of images from a specified folder into a video file. The script uses the OpenCV library, automatically sets frame size, and allows you to specify the FPS. For example it can be used for combines images after render.

---

## Features

- Automatic filename sorting for correct frame order
- Resizes all images to match the first frame's size
- Skips unreadable or corrupted images

---

## Requirements

- Python 3.8+
- `opencv-python` (`cv2`)

---

## Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/mistlp74/005_A1R1T3_0_2_VideoCollector.git
    cd VideoCollector
    ```

2. **Install dependencies:**
    ```bash
    pip install opencv-python
    ```

---

## Usage

1. Specify the path to the folder with images and the desired path/filename for the output video in the script.
2. Run the script:
    ```bash
    python videocollector.py
    ```

---

## Troubleshooting

- **No output video file:** Check that the image and video paths are correct and the folder contains images.

---

## Author

Developed by [Milis Carter](https://github.com/MilisCarter74)
