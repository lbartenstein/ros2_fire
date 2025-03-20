import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/wardenrobotics/ros2_fire/install/fire_detection_ros2'
