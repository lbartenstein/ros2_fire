# ros2_fire

## Installation and prerequisites 
```bash
pip install ultralytics 
```

Numpy needs to be version < 2 (!)  

```bash
pip install "numpy<2.0" 
```

Install package with 

```bash
cd ros2_fire 

colcon build 
```

Activate with 
```bash
source install/setup.bash 

ros2 launch fire_detection_ros2 fire_detection_ros2 
```

## Running and first steps

Create the topic /image by running the cam2image node

```bash
sudo apt-get install ros-humble-image-tools

# device_id defaults to 1 which should be fine for most cases
ros2 run image_tools cam2image --ros-args -p device_id:=2
```

Showing available webcams and the stream on the /image topic is possible with

```bash
# show video devices available on your system
sudo apt install v4l-utils
v4l2-ctl --list-devices

# Show video stream to check if correct camera is chosen and image is being published
ros2 run image_tools showimage 
```

Start fire detection node with
```bash
ros2 launch fire_detection_ros2 fire_detection_ros2 
```

## Success! 

It's working now :)
![](/assets/success.png)