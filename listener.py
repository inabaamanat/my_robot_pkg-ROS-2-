nano ~/ros2_ws/src/my_robot_pkg/my_robot_pkg/listener.py

import rclpy
from rclpy.node import Node
from std_msgs.msg import String

# Subscriber node that listens to messages on the "chatter" topic
class Listener(Node):

    def __init__(self):
        # Initialize the node with the name "listener"
        super().__init__('listener')

        # Subscribe to the "chatter" topic
        self.subscription = self.create_subscription(
            String,
            'chatter',
            self.callback,
            10
        )

    # This function runs whenever a new message is received
    def callback(self, msg):

        # Display the received message
        self.get_logger().info(
            f"I heard: {msg.data}"
        )

def main():
    # Start ROS 2 communication
    rclpy.init()

    # Create the Listener node
    node = Listener()

    # Keep the node running and waiting for messages
    rclpy.spin(node)

if __name__ == '__main__':
    main()
