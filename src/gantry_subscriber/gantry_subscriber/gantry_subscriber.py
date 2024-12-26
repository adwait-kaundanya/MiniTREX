import rclpy
from rclpy.node import Node
from sensor_msgs.msg import JointState

import serial
import time
# from apply_settings_to_gantry import applySettingsMain
# from py_pubsub.apply_settings_to_gantry import applySettingsMain

class JointCommandSubscriber(Node):
    def __init__(self):
        super().__init__('joint_command_subscriber')

        self.serial = serial.Serial('/dev/ttyUSB0',115200)
        print("s:",self.serial)
        self.serial.write("\r\n\r\n".encode())
        time.sleep(2)   # Wait for grbl to initialize 
        self.serial.flushInput()  # Flush startup text in serial input
        self.serial.write("$H\n".encode())
        # self.serial.write((f"G90 G21 G00 X{100} Y{100}\n").encode())
        time.sleep(0.1)
        # self.serial.flushInput()
        # self.serial.write((f"G00 Z{-50}\n").encode())
        # time.sleep(0.1)
        # print (' : ' + grbl_out.strip().decode())
        # time.sleep(5)
        # Close file and serial port
        self.dict={
            'z_axis_joint':None,
            'y_axis_joint':None,
            'x_axis_joint':None,
            'joint_1':None,
            'joint_2':None,
            'joint_3':None,
            'joint_4':None,
            'joint_5':None,
            'joint_6':None

        }
    
    
    ##########################

        self.subscription = self.create_subscription(
            JointState,
            '/joint_states',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning
        

    def listener_callback(self, msg):
        joint_names = msg.name
        # print(joint_names)
        joint_positions = msg.position
        # sent_number = 0

        for i, name in enumerate(joint_names):
            received_number = round(1000*joint_positions[i])
            self.dict[name]=received_number

        # for i, name in enumerate(joint_names):
            
        #     # received_number = round(1000*joint_positions[i])
        #     # print(received_number)
        #     if(name == "z_axis_joint"):
        #         self.serial.write((f"G00 Z{received_number}\n").encode())
        #     if(name == "y_axis_joint"):
        #         self.serial.write((f"G00 Y{received_number}\n").encode())
        #     if(name == "x_axis_joint"):
        #         self.serial.write((f"G00 X{received_number}\n").encode())  
        self.serial.flushInput()  
        self.serial.write((f"G00 X{self.dict['x_axis_joint']} Y{self.dict['y_axis_joint']} Z{self.dict['z_axis_joint']}\n").encode())
        time.sleep(0.05)
    


def main(args=None):

    rclpy.init(args=args)
    node = JointCommandSubscriber()
    rclpy.spin(node)
    
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
