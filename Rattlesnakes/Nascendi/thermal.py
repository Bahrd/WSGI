'''
Copilot'ed [October 2025]:
'Here’s a complete, runnable Python example showing how to capture video from a USB camera using OpenCV'
'''

import cv2
from sys import argv
def open_usb_camera(camera_index = 2, width = 160, height = 120, fps = -1):
    cap = cv2.VideoCapture(camera_index, cv2.CAP_DSHOW) 

    if not cap.isOpened():
        raise RuntimeError(f'Cannot open camera index {camera_index}')

    # Set resolution
    w, h = cap.get(cv2.CAP_PROP_FRAME_WIDTH), cap.get(cv2.CAP_PROP_FRAME_HEIGHT)    
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, w)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, h - 2) #????

    # Set FPS
    if(fps > 0):
        cap.set(cv2.CAP_PROP_FPS, fps)

    # Optional: Adjust camera parameters (values depend on camera capabilities)
    cap.set(cv2.CAP_PROP_BRIGHTNESS, 4)   
    cap.set(cv2.CAP_PROP_CONTRAST, -1)     
    cap.set(cv2.CAP_PROP_SATURATION, 1)   
    cap.set(cv2.CAP_PROP_EXPOSURE, +4)     

    return cap

class FailedFrameGrabbing(Exception):
    '''No frame, no game'''
    pass

thermal_camera = 2
global_shutter = 1
default_camera = 0 

def main():
    cap:cv2.VideoCapture = None
    try:
        camera = eval(argv[1]) if len(argv) > 1 else 2
        cap = open_usb_camera(camera) # thermal is the new default here
        scale = 2.0
        while True:
            ret, frame = cap.read()
            if not ret:
                raise FailedFrameGrabbing('Failed to grab a frame!')

            if camera == thermal_camera:
               frame = cv2.flip(frame, -1)
               frame = cv2.resize(cv2.applyColorMap(frame, cv2.COLORMAP_JET),
                                  None, fx = scale, fy = scale,
                                  interpolation = cv2.INTER_LINEAR)
            cv2.imshow(f'USB Camera {frame.shape}', frame)

            # Press 'q' to quit
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    except Exception as e:
        print(f'Exceptional error: {e}')

    finally:
        if(cap is not None):
            cap.release()
        cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
