<h2>Friendship lamps</h2>

# Overview
Two little "lamps", each having a led and they are in sync.
I've made 2 mini lamps that are called "Friendship" lamps! One for me and the other for a close person that lives far from me. The idea is that if I turn my light to colour green, my friend light will also turn green! The lamps accept 6 different colours obtained from combining red-green-blue lights. 

# Demo

![Lights](/../master/lights.gif?raw=True "Lights demo")

![DarkLights](/../master/dark-lights.gif?raw=True "Dark lights demo")

# Schematics

![Schematics](/../master/iot.png?raw=True "Breadboard schematics")


# Pre-requisites

For a single lamp is required: 

<ul>
  <li> Raspberry Pi Zero WH </li>
  <li> RGB led </li>
  <li> Mini-breadboard or breadboard</li>
  <li> Rezistors  </li>
  <li> Heatsync  </li>
  <li> 2 pushdown buttons </li>
  <li> Jmper wires </li>
  <li> Micro sd card >32 GB </li>
  <li> Power supply with micro sd  </li>
</ul>

Additional supplies needed: monitor, keyboard, mouse, hdmi adapter, hdmi cable, USB OTG cable

# Setup

## Creating a new rpi lamp connected to the existing cloud server

1. First you need a bootable micro sd. You can make one easy on your computer by downloading an image from: https://www.raspberrypi.org/software/operating-systems/ and then using a software like BalenaEtcher for flashing the micro sd. 
2. You need to insert the micro sd into your rpi and then connect all the components on the breadboard as presented in the schematics above. A mini breadboard is used in my case since the outcome desired is a little, cute night light.
3. After all the components are properly connected, the rpi will be plugged into a power source and then will start.
4. After finding the ip address of the rpi, you can connect from your computer to it (I used VNC Viewer).
5. Make sure Python 3 is installed (run python3 --version) on the Raspberry Py. If not, install it via `<sudo apt-get install python3>`.
6. The next and final step is the need of cloning the lighted.py file from this repository. After you get the script on your rpi, you need to simply run it for the lamp to get functional. The requests are sent to a cloud server, thus it will work on any network without any additional setups. 

* Optional: You can make the lamp script autorun at the start-up of the Raspberry Pi by adding the following line to the end of the /etc/rc.local file: `<python3 lighted.py>`
* Optional: You can connect the lamp to your own server, either local or on the cloud by changing the url located on top of the lighted.py file. More information in regards to the server used and how it was deployed, you can find here: https://medium.com/fullstackai/how-to-deploy-a-simple-flask-app-on-cloud-run-with-cloud-endpoint-e10088170eb7

## Running the already configured lamp on a different network

1. Connect the raspberry pi to a power outlet and to a monitor. After you can easily connect to your home wireless internet. You will need a hdmi cable and an usb otg cable for this step.
2. Find the file lighted.py located on the rpi's desktop and run it.
3. In addition, you can make the lamp script autorun at the start-up of the Raspberry Pi by adding the following line to the end of the /etc/rc.local file: `<python3 lighted.py>`

## Information regarding the server

The server used for keeping the lights in sync is a simple flask server dockerised and deployed on google cloud.

# Usage

Once the lamps are both plugged in and running, you can play with them in the following way:
* the leftmost button on the schematics picture is used for switching on/off the lamp's light;
* the inner button is used for switching between the lights, there are 6 possible light colours;

You can only switch off your own lamp light, you cannot switch off or on your friend lamp. It could be a bit weird for a sudden light to turn on in the middle of the night! Also, there could be more than 2 lamps connected to the same server and in sync.




