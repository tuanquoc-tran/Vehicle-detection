# Vehicle Detection
## Introduction
This Final project using yolov3 - tiny architecture with opencv to detect vehicle in Vietnam's traffic

## Description
1. Data 
- Data for this project were collected from cameras in Ho Chi Minh City. Number of photo were 4000 including 1200 night photos and 2800 daytime photos 
- Identifiers was common vehicle in Vietnam. 
- The data was divided into 75% training and 25% testing.
2. Model
- I used both yolov3 and yolov3-tiny for this project to compare the speed and accuracy of each model
3. Training 
- I used google colab gpu for training. When training with yolov3 at 9000 step took 2 day and yolov3-tiny at 20000 step the same time
4. Result 
- Weights were evaluated and executed on Jetson nano board
- I used a dnn function of opnecv library to execuate on GPU of jetson nano board. When using yolov3 the speed is achieved 8FPS, also the speed of yolov3-tiny was 22 FPS

![image](https://user-images.githubusercontent.com/51257497/99928366-5bd75c80-2d7b-11eb-972c-7d7072b00406.png)
![image](https://user-images.githubusercontent.com/51257497/99928379-6db8ff80-2d7b-11eb-856f-d69ed3b9418e.png)
![image](https://user-images.githubusercontent.com/51257497/99928388-77dafe00-2d7b-11eb-8789-729802ad828b.png)
![image](https://user-images.githubusercontent.com/51257497/99928395-7e697580-2d7b-11eb-8a3f-44b8cadec519.png)
![image](https://user-images.githubusercontent.com/51257497/99928399-86291a00-2d7b-11eb-929a-3f4c34c7cf60.png)
![image](https://user-images.githubusercontent.com/51257497/99928416-9214dc00-2d7b-11eb-8410-022bf398e151.png)
