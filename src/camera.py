import cv2
import numpy

class Camera:
    is_installed: bool = False
    resolutions = ['640x480', '1024x768', '1920x1080', '2920x1080']
    resolution_setting: int = 1
    
    def __init__(self):
        pass
    
    def check_is_installed(self):
        capture = cv2.VideoCapture(0)
        if capture.isOpened():
            print("Camera is installed")
            self.is_installed = True
            capture.release()
        else:
            print("Camera is not installed")

    def set_camera_frame(self, resolution_setting: int):
        self.resolution_setting = resolution_setting

    def take_photo(self) -> numpy.ndarray:
        cap = cv2.VideoCapture(0)
        resolution = self.resolutions[self.resolution_setting]
        cap.set(cv2.CAP_PROP_FRAME_WIDTH, int(resolution.split('x')[0]))
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, int(resolution.split('x')[1]))
        ret, frame = cap.read()
        if ret:
            return frame
        else:
            return