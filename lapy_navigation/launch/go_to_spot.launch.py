import os

from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node

def generate_launch_description():
    
    package_navigation = "lapy_navigation"

    config = os.path.join(get_package_share_directory(package_navigation),'config','spot_list.yaml')

    spot_name = LaunchConfiguration('spot_name')
    
    return LaunchDescription([ 
    
        DeclareLaunchArgument(
            'spot_name',
            default_value='start',
            description='Spot name, see config/spot_list.yaml'
        ),
            
        Node(
            package = package_navigation,
            executable = 'go_to_pose',
            name = 'move_to_spot',
            parameters = [
                {'spot_name':spot_name},
                {'use_sim_time': False},
                config
            ],
            output = 'screen',
        )
    ])