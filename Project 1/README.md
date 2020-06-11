Github Reference:
https://github.com/Azure-Samples/iot-hub-python-raspberrypi-client-app

From the root directory, navigate to the iot-hub-python-raspberrypi-client-app  directory
Cd iot-hub-python-raspberrypi-client-app

The script we will be running is a tripwire (laser + photosensitive resistor sensor) that will detect if the connection between the laser and resistor has been broken. It will send the state of the tripwire to Azure, and you can view the data at app.powerbi.com. To run the script, run the command:
python viewdata.py '<device connection string>’
python viewdata.py 'HostName=BoellisIoTHub.azure-devices.net;DeviceId=pi2;SharedAccessKey=26sxHnRAfdrX56ZmDBqCcjsLpHbpC+QcKXcg/haKFIU='sudo shu

Once you are signed in to your account on app.powerbi.com
Go to My Workspaces → Datasets
Click on the first icon(the bar graph) to view the data being sent from your raspberry pi to Azure.
From here, you can create different types of graphs/models to visualize your data
