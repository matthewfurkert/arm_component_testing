import cv2
import rclpy
from sensor_msgs.msg import Image
from rclpy.node import Node
from cv_bridge import CvBridge

class CameraSubscriberNode(Node):
    def __init__(self):
        super().__init__("camera_subscriber")

        self.bridgeObject = CvBridge()
        self.subscriber_ = self.create_subscription(Image, "camera_image", self.listener_callbackFunction, 10)
        self.subscriber_
    
    def listener_callbackFunction(self, imageMessage):
        self.get_logger().info("The image frame is received")
        openCVImage = self.bridgeObject.imgmsg_to_cv2(imageMessage)
        cv2.imshow("Camera Video", openCVImage)
        cv2.waitKey(1)

def main():
    rclpy.init()
    node = CameraSubscriberNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()