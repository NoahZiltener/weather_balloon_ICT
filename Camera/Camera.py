import picamera

camera = picamera.PiCamera(resolution=(640, 480))
stream = picamera.PiCameraCircularIO(camera)
camera.start_recording("recording.h264", format='h264')

try:
    while True:
        camera.wait_recording()

finally:
    camera.stop_recording()
