From the root directory, load your profile settings for your virtual environment using the commands:
Source ~/.profile
Workon cv

Navigate to the Desktop directory on your Pi and look at the files in the directory
Cd Desktop
Ls

Here you will see bvlc_googlenet.caffemodel, bvlc_googlenet.prototxt, picture.png, OpenCV.py, SecuritySystem.py, and synset_words.txt. Keep in mind that everything is case sensitive

Bvlc_googlenet.caffemodel → Image recognition model used with OpenCV
Bvlc_googlenet.prototxt → Describes the structure of the data that will be serialized
Synset_words.txt → Categories(labels) for images that have been processed by OpenCV
Picture.png → Image that will be captured by the raspberry pi and processed through OpenCV for recognition
SecuritySystem.py → Python script that manages the motion sensor, Pi camera, laser, LED, and photosensitive resistance sensor.


Running this project calls upon two python scripts, both of which exist inside of one script. OpenCV.py is called in SecuritySystem.py with the parameter pointing to the picture.png file path. To run the project, run the command:
Python SecuritySystem.py

The raspberry pi will wait until motion is detected before turning on the laser. Once it detects movement, the laser will turn on and the photosensitive sensor will begin reading input as ON. Once the path between the two has been broken or ‘tripped’ the camera will activate and take a picture. After the picture has been taken, OpenCV.py will run on the image that was taken, and return its results in the console. Afterwards, the process will start over and wait for movement to be detected again.
To stop the script, press Ctrl + C
