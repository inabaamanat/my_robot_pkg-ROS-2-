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




 What Happens When It Runs?
ROS 2 is initialized using rclpy.init()
A node called hello_node is created
The node logs the message:
Hello ROS 2!
rclpy.spin() keeps the node running and ready to communicate with other nodes

Although simple, this program introduces the fundamental building block of every ROS 2 application: the node!
