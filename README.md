# pushup_counter_with_python

This project uses OpenCV, imutils, and mediapipe Python libraries to create a push-up counter. Check out the full tutorial [here](https://www.makeuseof.com/python-push-up-counter-computer-vision-camera/).

## Description

The push-up counter project is designed to help users count their push-ups accurately using computer vision techniques. The project leverages OpenCV, imutils, and mediapipe libraries to detect and track body landmarks, providing real-time feedback and guidance to improve push-up form.

## Installation

To install the required libraries, run the following command:

```bash
pip install opencv-python imutils mediapipe numpy
```

## Usage

To run the push-up counter, execute the following command:

```bash
python main.py
```

Make sure to replace the filename in the `cv2.VideoCapture` function with `0` to use your webcam or provide the path to a video file.

## Troubleshooting

If you encounter any issues while running the push-up counter, consider the following troubleshooting steps:

1. Ensure that your webcam is properly connected and recognized by your system.
2. Verify that all required libraries are installed correctly.
3. Check the aspect ratio of your video feed to ensure proper resizing.
4. Make sure you have a clear and well-lit environment for accurate body landmark detection.

## Contributing

We welcome contributions to improve the push-up counter project. If you have any suggestions or improvements, please submit a pull request or open an issue on the GitHub repository.
