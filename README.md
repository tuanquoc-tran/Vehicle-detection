# Vehicle Detection
## Introduction
This Final project using yolov3 - tiny architecture with opencv to detect vehicle in Vietnam's traffic

## Description
#### 1. Data 
- Data for this project were collected from cameras in Ho Chi Minh City. Number of photo were 4000 including 1200 night photos and 2800 daytime photos 
- Identifiers was common vehicle in Vietnam. 
- The data was divided into 75% training and 25% testing.
#### 2. Model
- I used both yolov3 and yolov3-tiny for this project to compare the speed and accuracy of each model
#### 3. Training 
- I used google colab gpu for training. When training with yolov3 at 9000 step took 2 day and yolov3-tiny at 20000 step the same time
#### 4. Result 
- Weights were evaluated and executed on Jetson nano board
- I used a dnn function of opnecv library to execuate on GPU of jetson nano board. When using yolov3 the speed is achieved 8FPS, also the speed of yolov3-tiny was 22 FPS

![image](https://user-images.githubusercontent.com/51257497/99928570-36971e00-2d7c-11eb-84f5-309ff8c66463.png)
![image](https://user-images.githubusercontent.com/51257497/99928574-431b7680-2d7c-11eb-8b46-125d72d482b3.png)
![image](https://user-images.githubusercontent.com/51257497/99928580-4878c100-2d7c-11eb-9d7e-c24673af988d.png)
![image](https://user-images.githubusercontent.com/51257497/99928582-50386580-2d7c-11eb-9559-f2e44e1031d7.png)
![image](https://user-images.githubusercontent.com/51257497/99928589-54fd1980-2d7c-11eb-89ca-b8c8efdd8846.png)
![image](https://user-images.githubusercontent.com/51257497/99928593-5b8b9100-2d7c-11eb-86ae-b41a597a0345.png)

## Author 
### Leturer
PhD, Duc Bui Ha - Lecturer of Faculty of Mechanical Engineering (FME), Ho Chi Minh City University of Technology and Education, Vietnam.
### Students
+ Tuan Tran - Mechatronics student, Ho Chi Minh City University of Technology and Education, Vietnam.
+ Tuan Nguyen - Mechatronics student, Ho Chi Minh City University of Technology and Education, Vietnam.
+ Bao Nguyen - Mechatronics student, Ho Chi Minh City University of Technology and Education, Vietnam.
