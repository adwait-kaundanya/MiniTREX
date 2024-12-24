# Mini-Trex ROS 2 Project

## Overview
This project controls the **Mini-TRex robot** using ROS 2. The setup requires three separate terminals and assumes that all necessary ROS 2 packages are already installed. Before starting, ensure the ROS 2 package on the **MyCobotPi** is updated with the code for the subscriber node to enable communication.

---

## Steps to Run the Project

### **1. Start the ROS 2 Nodes**

Open **three terminals**, and execute the following commands in each:
The three terminals are for:

1) Launching the RVIZ2 and MoveIt2 motion planning framework
2) Subscriber node for the manipulator (Elephant Robotics MyCobot280Pi)
3) Subscriber node for the Gantry

These 3 steps **must be followed in the mentioned order** for proper and safe execution.
#### **Terminal 1: Launch the Mini-Trex Node**
```bash
cd ros2/mini_trex_ws
```
```bash
source install/setup.bash
```
```bash
ros2 launch mini_trex_moveit_config demo.launch.py
```
After executing these commands you should be able to see the RVIZ2 window open up with the robots model. Now open the second terminal.

Before moving onto the next steps make sure the USB is connected from the Blackbox controller to the PC.

#### **Terminal 2: Launch the manipulator subscriber**
```bash
ssh er@***.***.*.***
```

where the star represents the ip address of the raspberry pi.

Once the ssh conection has been established.
```bash
cd colcon_ws
```
```bash
source install/setup.bash
```
```bash
ros2 run mycobot280pi mini_trex_listener
```

Once the above command is executed the mycobot should go to its home position.
Visually confirm the home pose of the robot.

#### **Terminal 3: Launch the Gantry subscriber node**
```bash
cd ros2/mini_trex_ws
```
```bash
source install/setup.bash
```
```bash
ros2 run gantry_subscriber gantry_listener
```
After executing this command the gantry will start moving to its home position
