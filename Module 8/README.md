To capture images with your camera module, we will use the ‘raspistill’ command. Implementation can be found below:
'Raspistill -o image1.jpg'
This command outputs a jpg image labeled ‘image1’ to the current directory. You can change the image name and format(jpg,png,etc)
To record videos with your camera module, we will use the ‘raspivid’ command. Implementation can be found below:
'Raspivid -o video1.h264 -t 10000'
This command outputs a video named ‘video1’ and with the video length being 10,000 milliseconds.
