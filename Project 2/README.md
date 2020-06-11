From the root directory, load your profile settings for your virtual environment using the commands:
Source ~/.profile
Workon cv

Navigate to the Desktop directory on your Pi and look at the files in the directory
Cd Desktop
Ls

To run the script, use the command:
Python cameraTripwireMotion.py

The raspberry pi will wait until motion is detected before turning on the laser. Once it detects movement, the laser will turn on and the photosensitive sensor will begin reading input as ON. Once the path between the two has been broken or ‘tripped’ the camera will activate and take a picture
To stop the script, press Ctrl + C
