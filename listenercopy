nano ~/ros2_ws/src/my_robot_pkg/my_robot_pkg/talker.py

import rclpy
from rclpy.node import Node
from std_msgs.msg import String

# Publisher node that sends a message to the "chatter" topic every second
class Talker(Node):

    def __init__(self):
        # Initialize the node with the name "talker"
        super().__init__('talker')

        # Create a publisher that sends String messages on the "chatter" topic
        self.publisher = self.create_publisher(
            String,
            'chatter',
            10
        )

        # Create a timer that calls publish_message() every 1 second
        self.timer = self.create_timer(
            1.0,
            self.publish_message
        )

    def publish_message(self):
        # Create a ROS String message
        msg = String()

        # Store text inside the message
        msg.data = "Hello from Inaba's ROS node!"

        # Publish the message to the topic
        self.publisher.publish(msg)

        # Print the message in the terminal
        self.get_logger().info(msg.data)

def main():
    # Start ROS 2 communication
    rclpy.init()

    # Create the Talker node
    node = Talker()

    # Keep the node running
    rclpy.spin(node)

if __name__ == '__main__':
    main()
