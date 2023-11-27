import cv2

# Load the video
video_path = './videos/mykarttest/GOPR0079.MP4'
cap = cv2.VideoCapture(video_path)

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'mp4v') # or (*'XVID')
out = cv2.VideoWriter('./videos/mykarttest/gpgs.MP4', fourcc, 20.0, (int(cap.get(3)), int(cap.get(4))), isColor=False)

# Read until video is completed
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        # Convert each frame to grayscale
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Write the grayscale frame
        out.write(gray_frame)

        # Display the resulting frame (optional)
        # cv2.imshow('Frame', gray_frame)

        # Press Q on keyboard to exit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# Release everything when done
cap.release()
out.release()
cv2.destroyAllWindows()
