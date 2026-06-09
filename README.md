# my_robot_pkg-ROS-2-
Come along as I learn Robot Operating System 2(ROS 2)!

# my_robot_pkg

My first ROS 2 package created while learning the Robot Operating System (ROS 2) during the Texas Robotics Research Fellowship at The University of Texas at Austin.

This repository documents my introduction to ROS 2 concepts including workspaces, packages, nodes, and Python-based robot software development. The goal of this project is to build a strong foundation for future robotics applications in areas such as medical robotics, haptics, autonomous systems, and human-robot interaction.

# What is ROS 2?

ROS 2 (Robot Operating System 2) is an open-source robotics middleware that provides tools, libraries, and communication frameworks for building robotic systems.

Instead of creating one large program, ROS 2 organizes robot software into smaller components called nodes that communicate with one another through topics, services, and actions.

Sensor Node  --->  Topic  --->  Controller Node
                                    |
                                    v
                              Actuator Node

This modular architecture allows robotic systems to scale from simple projects to complex multi-robot applications.

# What is a Node?

A node is an individual executable process within a ROS 2 system.

Examples include:

Camera Node
LiDAR Node
Motor Controller Node
State Estimator Node
Path Planning Node

Each node is responsible for a specific task and can communicate with other nodes across the system.

Project Overview

This package contains a simple ROS 2 Python node named hello_node.

The node demonstrates:

Creating a custom ROS 2 node
Initializing the ROS 2 client library (rclpy)
Inheriting from the ROS 2 Node class
Logging information to the ROS 2 console
Keeping a node alive using the ROS 2 execution loop

# ROS 2 Workspace Structure
ros2_ws/
├── src/
│   └── my_robot_pkg/
├── build/
├── install/
└── log/
src/ contains source code and packages
build/ contains generated build files
install/ contains compiled and executable packages
log/ stores build and runtime logs
