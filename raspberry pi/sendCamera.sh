gst-launch-1.0 -v v4l2src device=/dev/video2 ! video/x-raw, format=YUY2, width=1920, height=1080, pixel-aspect-ratio=1/1, framerate=30/1, colorimetry=bt709, interlace-mode=progressive  ! queue ! videoscale ! video/x-raw,width=1920,height=1080 !  videoconvert ! queue ! timeoverlay ! x264enc bitrate=4000 speed-preset=ultrafast tune=zerolatency key-int-max=15 noise-reduction=100000 ! video/x-h264,profile=constrained-baseline ! h264parse ! rtph264pay !  udpsink host=10.0.0.18 port=5000