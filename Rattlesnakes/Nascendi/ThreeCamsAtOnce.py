'''
Copilot'ed [October 2025]: A runnable Python example showing how to capture video from a USB camera using OpenCV'
The snippet for a two-camera USB module consisted of:
+ Global shutter camera Omnivision 1280x800@120fps OV9281
+ Thermal camera 160x120@9fps FLIR Lepton 3.5
+ default (usually a rolling shutter RGB) camera
'''

import cv2
from sys import argv
from enum import Enum, auto

class FailedFrameGrabbing(Exception):
    '''No frame, no game'''
    pass

class usb_camera(Enum):
    # LEPTON35 https://groupgets.com/products/flir-lepton-3-5
    # OV9281   https://www.ovt.com/products/ov9281/
    #
    # The camera device order is somehow arbitrary: 
    # + on Windows LEPTON is the last, 
    # + on RaspBerry the last is OV9281
    DEFCAM, OV9281, LEPTON35 = (0, auto(), auto())

def set_up_camera(camera_index):
    cap = cv2.VideoCapture(camera_index.value, cv2.CAP_DSHOW) 

    if not cap.isOpened():
        raise RuntimeError(f'Cannot open {camera_index.name}')

    # Set resolution
    w, h = cap.get(cv2.CAP_PROP_FRAME_WIDTH), cap.get(cv2.CAP_PROP_FRAME_HEIGHT)    
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, w)
    # That's not way one should write code, but hey!
    # We didn't start this mess - after all!                                        
    correction = camera_index.value if camera_index == usb_camera.LEPTON35 else 0  #WTF?
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, h - correction)                             #FTW!
    return cap


ABC = [set_up_camera(c) for c in (usb_camera.DEFCAM, usb_camera.OV9281, usb_camera.LEPTON35)]

import matplotlib.pyplot as plt


def main():
    cap:cv2.VideoCapture = None
    try:
        camera = eval('usb_camera.' + argv[1]) if len(argv) > 1 else usb_camera.LEPTON35
        # FLIR's Lepton 3.5 thermal camera is the new default here
        cap = set_up_camera(camera) 
        while True:
            ret, frame = cap.read()
            if not ret:
                raise FailedFrameGrabbing('Failed to grab a frame!')

            if camera == usb_camera.LEPTON35:
               scale = 2.0
               frame = cv2.applyColorMap(frame, cv2.COLORMAP_JET)
               # no selfie, no mirroring
               frame = cv2.flip(frame, 0)
               frame = cv2.resize(frame, None, fx = scale, fy = scale,
                                  interpolation = cv2.INTER_LANCZOS4)
            # Insert here your own resize/rotate routine #
            # ...
            # ... and show it off!
            plt.imshow(frame)

            # Press 'q' to quit
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    except Exception as e:
        print(f'Exceptional error: {e}')

    finally:
        if(cap is not None):
            cap.release()
        cv2.destroyAllWindows()

main() if __name__ == '__main__' else None
