from setuptools import setup

package_name = 'fire_detection_ros2'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/launch', ['launch/fire_detection.launch.py']), # launch
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Ali Alipour', 
    maintainer_email='a.alipour@ostfalia.de', 
    description='ROS2 package for fire detection using YOLO', 
    license='TODO: License declaration', 
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'webcam_fire = fire_detection_ros2.webcam_fire:main', 
        ],
    },
)