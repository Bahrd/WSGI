## Bash:
# for i in LEPTON35 OV9281 DEFCAM; do python ./PiCams.py $i; done

from picamera2 import Picamera2
import PIL.Image, cv2, numpy as np
from sys import argv
from enum import Enum, auto

class usb_camera(Enum):
    # LEPTON35 https://groupgets.com/products/flir-lepton-3-5
    # OV9281   https://www.ovt.com/products/ov9281/
    #
    # The camera device order is somehow arbitrary:
    # + on Windows LEPTON is the last,
    # + on RaspBerry the last is OV9281
    DEFCAM, LEPTON35, OV9281 = (0, auto(), auto())

#  Our thermal camera is treated in a less standard way...
canum = eval('usb_camera.' + argv[1]) if len(argv) > 1 else usb_camera.LEPTON35
try:
   picam2 = Picamera2(canum.value)
   picam2.configure(picam2.create_preview_configuration())
   picam2.start()

   if(canum == usb_camera.LEPTON35):
      ## Thermal camera needs special processing
      (buffer, ), metadata = picam2.capture_buffers(["main"])
      # The colder the object, the higher the value
      buffer = 255 - buffer
      # Buffer is 1D, reshape to 2D
      buffer = buffer.reshape(120, 160)
      # Convert to a color-like lookin' image
      img = np.stack([buffer] * 3, axis = -1)
      # Apply a thermal-looking colormap
      img = cv2.applyColorMap(img, cv2.COLORMAP_JET)
      # The deed is done, save the image
      PIL.Image.fromarray(img).save(f"{canum.name}.png")
   else:
      # Regular camera, just capture and save
      picam2.capture_file(f"{canum.name}.png")
except Exception as e:
   # Just announce any error
   print(f"Error with camera {canum.name}: {e}")
finally:
   # There is nothing else to see, move on, go home, and..
   picam2.close()
