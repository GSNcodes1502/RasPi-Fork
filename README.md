# TODO
- [ ] Make code work with PiCamera2
- [ ] Make documentation
- [ ] Move this repo and TIP-Accessibility-2022 to Organisation
- [ ] Merge Volume detection code if possible
- [ ] Test the code with experiments in real time
- [ ] Merge relevant changes upstream to TIP-Accessibility
- [ ] Implement voice output on the RasPi
# DONE

# System information
- Debian 12 Bookworm
- RasPi Camera module v1.3 (OV5647, 5MP, <resolution>)
- Raspberry Pi 3 Model B+

# Documentation links 
## PiCamera documentation
 - IMPORTANT: DO NOT USE PICAMERA IF YOU ARE ON A 64-BIT SYSTEM. USE PICAMERA2 INSTEAD.   
 - https://docs.arducam.com/Raspberry-Pi-Camera/Native-camera/PiCamera2-User-Guide/
 - https://datasheets.raspberrypi.com/camera/picamera2-manual.pdf
 - 
## Camera Module datasheets
- https://datasheets.raspberrypi.com/camera/raspberry-pi-camera-guide.pdf
  - Contains general info about all the camera modules. Relevant sections : v1
- https://www.raspberrypi.com/documentation/accessories/camera.html
-  https://docs.rs-online.com/2888/0900766b8127db0a.pdf
  - This contains the specifications for the camera module currently being used: the v1.3   
## Extra links that may be relevant
- https://libcamera.org/
  - libcamera is the userspace camera stack used by PiCamera2. Note: openCV has not got builtin support for the libcamera stack, which includes the RasPi camera modules, so openCV's Video.Capture(0) will bring up an error.
  - rpicam is an extension of libcamera made by the Raspberry Pi team      
- https://docs.kernel.org/userspace-api/media/v4l/colorspaces-defs.html
  - v4l2 is the kernel driver used to interface with the camera

- [SSH into RasPi](https://www.makeuseof.com/how-to-ssh-into-raspberry-pi-remote/) 
