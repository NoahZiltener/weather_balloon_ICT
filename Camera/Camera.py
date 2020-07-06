import picamera

camera = picamera.PiCamera(resolution=(640, 480))
stream = picamera.PiCameraCircularIO(camera)
camera.start_recording("recording.h264", format='h264')
camera.start_preview()

try:
    while True:
        camera.wait_recording()

finally:
    camera.stop_recording()
    camera.stop_preview()
