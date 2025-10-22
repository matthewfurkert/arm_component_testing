import cv2
import rclpy
from sensor_msgs.msg import Image
from rclpy.node import Node
from cv_bridge import CvBridge

class CameraPublisherNode(Node):
    def __init__(self):
        super().__init__("camera_publisher")

        self.cameraDeviceNumber=0
        self.camera = cv2.VideoCapture(self.cameraDeviceNumber)
        self.bridgeObject = CvBridge()
        self.periodCommunication=0.02
        self.i=0

        self.publisher_ = self.create_publisher(Image, "camera_image", 10)
        self.timer_ = self.create_timer(self.periodCommunication, self.timer_callbackFunction)

    def timer_callbackFunction(self):
        success, frame = self.camera.read()
        frame = cv2.resize(frame, (820, 640), interpolation=cv2.INTER_CUBIC)

        if success:
            ROS2ImageMessage = self.bridgeObject.cv2_to_imgmsg(frame)
            self.publisher_.publish(ROS2ImageMessage)
            self.get_logger().info("Publishing image number %d" % self.i)
            self.i += 1

        if not self.camera.isOpened():
            self.get_logger().error("Failed to open the camera")
            rclpy.shutdown()
            return


def main():
    rclpy.init()
    node = CameraPublisherNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()