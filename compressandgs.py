import cv2
import sys
import os

os.environ['OPENCV_FFMPEG_READ_ATTEMPTS'] = '10000'  # Increase the attempt limit

# Check if the video file is provided as a command line argument
if len(sys.argv) < 2:
    print("Usage: python script.py input_video.mp4")
    sys.exit(1)

# Get the input video file from command line arguments
input_video_path = sys.argv[1]

# Prepare the output file name
input_video_dir = os.path.dirname(input_video_path)
input_video_name, ext = os.path.splitext(os.path.basename(input_video_path))
output_video_path = os.path.join(input_video_dir, f"{input_video_name}_compressed.mp4")

# Open the input video
cap = cv2.VideoCapture(input_video_path)

# Get original video properties
original_fps = cap.get(cv2.CAP_PROP_FPS)
fourcc = cv2.VideoWriter_fourcc(*'mp4v')

# Set the new FPS and calculate frame skip rate
new_fps = 5.0
frame_skip_rate = int(original_fps / new_fps)

# Set the size of the output video
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH) * 240 / cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
height = 240

# Create a VideoWriter object to write the video at 5fps
out = cv2.VideoWriter(output_video_path, fourcc, new_fps, (width, height), isColor=False)

# Frame counter
frame_count = 0

# Read and process the video frame by frame
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Process only every Nth frame
    if frame_count % frame_skip_rate == 0:
        # Resize the frame
        frame_resized = cv2.resize(frame, (width, height))

        # Convert to grayscale
        frame_gray = cv2.cvtColor(frame_resized, cv2.COLOR_BGR2GRAY)

        # Write the frame to the output video
        out.write(frame_gray)

    frame_count += 1

# Release the VideoCapture and VideoWriter objects
cap.release()
out.release()
