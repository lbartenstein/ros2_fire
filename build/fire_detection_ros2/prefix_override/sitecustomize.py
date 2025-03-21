import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/heinzrobotic/ros2_fire/install/fire_detection_ros2'
