import rclpy
from rclpy.node import Node

class HelloNode(Node):

    def __init__(self):
        super().__init__('hello_node')
        self.get_logger().info("Hello ROS 2!")

def main():
    rclpy.init()
    node = HelloNode()
    rclpy.spin(node)

if __name__ == '__main__':
    main()
