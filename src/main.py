import cv2
import os
import time
import logging

def main():
    #Generate log file
    logging.basicConfig(filename='info.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S'
    )

    # Define resolutions
    sizes = ['640x480', '1024x768', '1920x1080', '2920x1080']
    print("Available resolutions:")
    for i, size in enumerate(sizes):
        print(f"{i+1}. {size}")
        
    # Select resolution
    resolution_idx = int(input("Select the resolution (1-4): ")) - 1
    resolution = sizes[resolution_idx]

    # Enter number of photos
    frames = int(input("Enter the number of photos: "))

    # Enter delay between photos
    delay = int(input("Enter the delay between all photos (s): "))

    # Create captures folder
    parent_dir = os.path.abspath(os.path.join(os.getcwd(), os.pardir))
    captures_dir = os.path.join(parent_dir, 'captures')
    if not os.path.exists('captures'):
        os.makedirs('captures')

    # Take photos
    for i in range(frames):
        image_name = f'captures/capture_{i+1}.jpg'
        print(image_name)
        cap = cv2.VideoCapture(0)
        logging.info('Camera capture taken')
        print("Working on your photo...")
        cap.set(cv2.CAP_PROP_FRAME_WIDTH, int(resolution.split('x')[0]))
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, int(resolution.split('x')[1]))
        ret, frame = cap.read()
        if ret:
            cv2.imwrite(image_name, frame)
            print(image_name)
            print(frame)
            cv2.imshow("Captured Image", frame)
        cap.release()
        
        if i < frames - 1:
            for i in range(delay):
                print("Next capture in", delay - i)
                time.sleep(1)

if __name__ == '__main__':
    main()