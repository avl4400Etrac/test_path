#!/usr/bin/env python3
import rospy
#pip3 install matplotlib
import matplotlib.pyplot as plt
import matplotlib.image as img

 #Init node 
rospy.init_node("my_test_node")

rospy.loginfo("Hello from test")
#Read path from param
my_path = rospy.get_param("my_img_path",default="none")
rospy.loginfo("My Path is: "+  my_path)

#Read image from path
file_path = my_path + "/smile.png"
rospy.loginfo("File Path is: "+  file_path)
#load image
testImage = img.imread(file_path)
  
# displaying the image
plt.imshow(testImage)
plt.show(block=True)
rospy.loginfo("Byby")
#rospy.spin() #not need eas plt.show() blocks thread