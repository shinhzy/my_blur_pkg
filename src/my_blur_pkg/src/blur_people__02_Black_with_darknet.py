#!/usr/bin/env python
import rospy
import sys
import roslib
from darknet_ros_msgs.msg import BoundingBoxes
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
import cv2

bridge = CvBridge()
cv_image = None


# Change ROS Image message to OpenCV
def image_callback(msg):

    
    global cv_image
    try:
        cv_image = bridge.imgmsg_to_cv2(msg, "bgr8")
    except CvBridgeError as e:
        print(e)

def bounding_boxes_callback(msg):
    global cv_image

    if cv_image is None:
        return
    #img = cv_image.copy()

    # Set ROI be set blur or mosaic 
    for box in msg.bounding_boxes:
        if box.Class == "person": # and cv_image is not None:
            cv_image[box.ymin:box.ymax, box.xmin:box.xmax] = 0

    cv2.imshow("Blacked out people", cv_image)
    cv2.waitKey(1)



if __name__ == '__main__':

    rospy.init_node('blur_people', anonymous=True)
    # Subscribe Image Node
    rospy.Subscriber("/bebop/image_raw", Image, image_callback)
    # Subscribe darknet_ros bounding boxes
    rospy.Subscriber("/darknet_ros/bounding_boxes", BoundingBoxes, bounding_boxes_callback)
    
    image_pub = rospy.Publisher("/blurred_image", Image, queue_size=1)

    try:
        rospy.spin()
    except KeyboardInterrupt:
        print("Shutting down")

