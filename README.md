# gui_widget_Project

## 환경구성
- OS : ubuntu22.04 
- ros : humble
- tools : Qt creator, python3.0, turtlesim_node

-----
- 패키지 생성(ament_cmake)
  
```python
 ros2 pkg create my_gui_pacjage --build-type ament_cmake --dependencies geometry_msgs python_qt_binding qt_gui_py_common rclpy rqt_py_common std_srvs ament_lint_auto ament_lint_common
```


![Screenshot from 2023-05-03 15-33-50](https://user-images.githubusercontent.com/84003327/235856652-3f8f9778-eb57-4d36-adc8-e9222a131a70.png)
