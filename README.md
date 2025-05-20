# Invisibility Cloak 🧙‍♂️

A fun computer vision project that creates a Harry Potter-style invisibility cloak effect using Python and OpenCV. This project uses your webcam to detect a red cloth and replaces it with the background, creating the illusion of invisibility.

## Requirements

- Python 3.x
- OpenCV (`cv2`)
- NumPy

## Installation

1. Clone this repository:
```bash
git clone https://github.com/Aayush-05/InvisibilityCloak.git
cd Invisibility-Cloak
```

2. Install the required packages:
```bash
pip install opencv-python numpy
```

## How to Use

1. Run the script:
```bash
python invisibilityCloak.py
```

2. When the program starts:
   - Stand in front of your webcam
   - Hold a red cloth (or any red object) in front of you
   - The program will capture the background for 5 seconds
   - After that, when you move the red cloth, it will appear as if you're invisible!

3. Press 'Esc' key to exit the program.

## How It Works

1. The program captures your webcam feed and waits for 3 seconds
2. It then captures 30 frames to create a background image
3. In real-time, it:
   - Detects red objects in the frame
   - Replaces the red areas with the corresponding background
   - Creates the illusion of invisibility

## Tips for Best Results

- Use a solid red cloth for best results
- Ensure good lighting conditions
- Keep the background relatively static
- Stand a few feet away from the camera
- Avoid wearing red clothing while using the cloak

## Troubleshooting

- If the effect isn't working well, try adjusting the lighting
- Make sure your webcam is working properly
- If the red detection is too sensitive or not sensitive enough, you can adjust the HSV values in the code

## License

This project is open source and available under the MIT License.

## Contributing

Feel free to submit issues and enhancement requests!