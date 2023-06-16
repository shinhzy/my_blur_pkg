# my_blur_pkg 
---
## 이미지 블러 과정 확인
### [1] 영상을 촬영하여 image_raw를 출력하는 중심 코드
```
root@bebop:/# cd ~/bebop_ws
root@bebop:~/bebop_ws# roslaunch bebop_driver bebop_node.launch
```
### [2] 영상 yolo 처리 관련 darknet_ros 호출 = 객체 인식
```
root@bebop:/# cd ~
root@bebop:~# roslaunch darknet_ros darknet_ros.launch
```
### [3] 객체 인식된 부분의 데이터를 darknet_ros 에서 받아서 그 부분을 검정색으로 처리
```
root@bebop:/# cd ~/my_blur_pkg
root@bebop:~/my_blur_pkg# rosrun my_blur_pkg blur_people.py
```
### [4] 기타 수동 조작 및 자동 제어는 기존 코드 그대로 사용
---



## 본 기능에 대해
이미지 인식의 과정을 darknet_ros에 맡겨야 하기에 필요한데,이 기능 자체로 영상이 출력됨.
따라서 후처리된 영상이 따로 출력되어야 하므로 영상창이 2개가 됨. 또한 속도가 조금 느림.
가우시안 블러는 좀 더 느려서 검정색 검열로 처리함.

이를 완전히 해결하기 위해서는 darknet_ros 내의 YoloObjectDetector.cpp 를 수정해야하나,
기능 구현은 가능할 지라도 특이한 디렉토리 구조에 의해 catkin_make 와 source 에 약간의 문제가 있어서
우선 이렇게만 만들어 두었음.



