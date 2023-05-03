
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([

        Node(
            package='rqt_gui_py',
            executable='rqt_gui',
            name='rqt_gui',
            output='screen'
        ),
    ])
