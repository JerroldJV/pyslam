import sys
import cv2
import time
from datetime import datetime

# CHESSBOARD SIZE
chessboard_size = (11,7)

# grab an image every 
kSaveImageDeltaTime = 0.1 # s

if __name__ == "__main__":

    video_path = "/tmp/pyslam/videos/mykarttest/GOPR0079_compressed.mp4"  # Replace with your MP4 file path
    if len(sys.argv) == 2:
        video_path = sys.argv[1]

    print('opening video file:', video_path)

    cap = cv2.VideoCapture(video_path)
    
    lastSaveTime = time.time()  # Initialize with the current time
 
    while cap.isOpened():
        
        ret, image = cap.read()
        if ret: 

            # check if pattern found
            ret, corners = cv2.findChessboardCorners(cv2.cvtColor(image, cv2.COLOR_BGR2GRAY), chessboard_size, None)
        
            if ret == True:     
                print('found chessboard')
                # save image
                filename = datetime.now().strftime('%Y%m%d_%Hh%Mm%Ss%f') + '.bmp'
                image_path="./calib_images/" + filename
                
                elapsedTimeSinceLastSave = time.time() - lastSaveTime  # Calculate elapsed time
                do_save = elapsedTimeSinceLastSave > kSaveImageDeltaTime
                
                if do_save:
                    lastSaveTime = time.time()  # Update last save time
                    print('saving file ', image_path)
                    cv2.imwrite(image_path, image)

                # draw the corners
                image = cv2.drawChessboardCorners(image, chessboard_size, corners, ret)                       

            cv2.imshow('frame', image)                

        else: 
            break
                            
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break    

    cap.release()
    cv2.destroyAllWindows()
