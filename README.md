# Hand-Motion-Controlled Cursor

**Hand-Motion-Controlled Cursor** is a Python-based project that allows users to control the computer cursor using hand gestures captured by a depth-sensing camera. This project provides an intuitive and interactive way to interact with your computer.

## Table of Contents
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Getting Started](#getting-started)
- [Usage](#usage)

## Features

- Control the computer cursor with hand movements.
- Recognize hand gestures for clicking and other interactions.
- Easily customize and extend the gesture recognition logic.
- Compatible with popular depth-sensing cameras like Intel RealSense and Microsoft Kinect.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.8 or higher installed.
- Depth-sensing camera (Intel RealSense, Microsoft Kinect, webcam etc.) connected and functioning.
- Dependencies installed (listed in `requirements.txt`).

## Getting Started

To get started with this project, follow these steps:

1. Clone the repository to your local machine:

   ```shell
   git clone https://github.com/edokaa/hand-cursor-control.git
   ```

2. Navigate to the project directory:
    ```shell
    cd hand-cursor-control
    ```

3. Install the required dependencies:
    ```shell
    pip install -r requirements.txt
    ```
4. Run the project:
    ```shell
    python main.py
    ```

## Usage
- Ensure your depth-sensing camera is correctly set up and recognized by the system.
- Launch the project by running main.py.
- Follow the on-screen instructions for gesture controls.
- Customize gesture recognition logic in the code as needed for your specific use case.
