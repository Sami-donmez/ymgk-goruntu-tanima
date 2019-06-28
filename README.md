# Requirement
- Python 3.4+
- OpenCV 3.1.0
- Numpy
- Ip Camera (I'm using the android app "IP Webcam")

# How to run ?
1. Please make sure that you have folders called 'dataset' and 'trainer' in the same directory
2. Run in the command line the face_datasets.py for taking your face image as datasets. Don't forget to set each person's face to unique ID (You need to edit the code everytime, or maybe just change the id variable to raw_input[OPTIONAL])
3. If you have more face to be include, change the ID and run the program again
4. Train your datasets by running training.py
5. Lastly, run face_recognition.py
