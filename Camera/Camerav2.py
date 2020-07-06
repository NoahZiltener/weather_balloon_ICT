from datetime import datetime
import picamera


recordingtime = 120
now = datetime.now()
dt_string = now.strftime("%d_%m_%Y_%H_%M_%S")

camera = picamera.PiCamera(resolution=(1920, 1080))
camera.start_recording('%d_%s.h264' % (1, dt_string))
camera.wait_recording(recordingtime)
i = 2

try:
    while True:
        now = datetime.now()
        dt_string = now.strftime("%d_%m_%Y_%H_%M_%S")
        camera.split_recording('%d_%s.h264' % (i, dt_string))
        camera.wait_recording(recordingtime)
        i = i + 1

finally:
    camera.stop_recording()
