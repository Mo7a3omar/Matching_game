# Shape Matching Game

This is a fun and interactive shape matching game for kids using computer vision and hand tracking. The game allows children to drag and match shapes to their corresponding outlines using their fingers. It also features a "New Game" button to randomize the shapes and start a new game.

## Features

- **Interactive Shape Matching**: Drag and drop shapes to match their corresponding outlines.
- **Real-time Hand Tracking**: Uses Mediapipe for real-time hand tracking and interaction.
- **Multiple Shape Dragging**: Allows dragging of multiple shapes simultaneously.
- **New Game Button**: Start a new game by randomizing the positions of the shapes.

## Requirements

- Python 3.7 or higher
- OpenCV
- Mediapipe
- NumPy

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/shape-matching-game.git
   cd shape-matching-game
Install the required dependencies:
bash
Copy code
pip install opencv-python mediapipe numpy
Usage
Run the game script:

bash
Copy code
python game.py
The game window will open, showing the shapes and their corresponding outlines.

Use your index fingers to drag and drop the shapes to match their outlines.

Click the "New Game" button in the top-right corner to randomize the positions of the shapes and start a new game.

How It Works
The game uses the webcam to capture real-time video.
Mediapipe is used to detect and track hand landmarks.
OpenCV is used to draw shapes and handle the drag-and-drop interaction.
When a shape is close to its target position, it snaps into place and changes color.
Code Overview
game.py: Main script containing the game logic, shape class, and hand tracking implementation.
Contributing
Contributions are welcome! Please feel free to submit a pull request or open an issue to discuss any changes or improvements.

License
This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgements
Mediapipe for the hand tracking library.
OpenCV for the computer vision library.
