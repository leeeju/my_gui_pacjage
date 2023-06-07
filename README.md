# gui_widget_Project

## 환경구성
- OS : ubuntu22.04 
- ros : humble
- tools : Qt creator, python3.0, turtlesim_node

## 기간
- 2023.05.01 ~ 진행중

-----
- 패키지 생성(ament_cmake)
  
```python
 ros2 pkg create my_gui_pacjage --build-type ament_cmake --dependencies geometry_msgs python_qt_binding qt_gui_py_common rclpy rqt_py_common std_srvs ament_lint_auto ament_lint_common
```
- Qt creator
  creator를 사용한 ui 디자인을 편리하게 쓸수 있는 장점이 있지만 개인적으로 코드를 만들기 어려웠다 일단 예제가 일반적인 프로그램의 예제이고 ros와의 연동을 하는데는 개인적으로 어려움이 있었다 turtlesim_node를 사용해서 움직임을 주는 코드와 ui를 제작하여 사용하였다 메시지 명령만 다른것으로 바꿔 주면 모든 로봇에서 사용이 가능하다 

- 툴 선택 창
![Screenshot from 2023-05-03 15-33-50](https://user-images.githubusercontent.com/84003327/235856652-3f8f9778-eb57-4d36-adc8-e9222a131a70.png)
- ui 제작 창
![Screenshot from 2023-05-03 17-15-12](https://user-images.githubusercontent.com/84003327/235864325-dbe71a5c-7e22-4e4a-a818-cf6110a99fee.png)
