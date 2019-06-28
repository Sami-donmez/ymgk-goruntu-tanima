import tkinter as tk

# Import OpenCV2 for image processing
import cv2

# Import numpy for matrices calculations
import numpy as np

# Import ssl for ssl issues
from ssl import SSLContext,PROTOCOL_TLSv1

# Import urlopen to open the url of the ip webcam
from urllib.request import urlopen

# Create Local Binary Patterns Histograms for face recognization
recognizer = cv2.cv2.face.LBPHFaceRecognizer_create()

# Load the trained mode
recognizer.read('trainer/trainer.yml')

# Load prebuilt model for Frontal Face
cascadePath = "haarcascade_frontalface_default.xml"

# Create classifier from prebuilt model
faceCascade = cv2.CascadeClassifier(cascadePath);

# Set the font style
font = cv2.FONT_HERSHEY_SIMPLEX

# Ip of the IP webcam server (on phone). The phone and your computer must be in the same LAN (connected to the same WiFi)
url = 'http://192.168.43.1:8080/shot.jpg'
#url = 'http://10.93.135.156:8080/shot.jpg'

def onclickBtn1():
	# Loop
	while True:
		# Read the video frame from the url
		gcontext = SSLContext(PROTOCOL_TLSv1)  # Only for gangstars
		info = urlopen(url, context=gcontext).read()


		imgNp=np.array(bytearray(info),dtype=np.uint8)
		im=cv2.imdecode(imgNp,-1)


		# Convert the captured frame into grayscale
		gray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)

		# Get all face from the video frame
		faces = faceCascade.detectMultiScale(gray, 1.3,5)

		# For each face in faces
		for(x,y,w,h) in faces:

			# Create rectangle around the face
			cv2.rectangle(im, (x-20,y-20), (x+w+20,y+h+20), (0,255,0), 4)

			# Recognize the face belongs to which ID
			Id, conf = recognizer.predict(gray[y:y+h,x:x+w])

			# Check the ID if exist 
			if(Id == 1):
				Id = "M.Samanci"
			# # Uncomment this block if you want to recognize other faces, and replace with the id provided in face_datasets
			elif(Id == 2):
				Id = "Y.Emre.Kilic" # # Name of the other person you want to recognize
			# #If not exist, then it is Unknown
			# else:
			#     Id = "Unknown"

			# Put text describe who is in the picture
			cv2.rectangle(im, (x-22,y-90), (x+w+22, y-22), (0,255,0), -1)
			cv2.putText(im, str(Id), (x,y-40), font, 1, (255,255,255), 3)

		# Display the video frame with the bounded rectangle
		cv2.imshow('im',im) 

		# If 'q' is pressed, close program
		if cv2.waitKey(10) & 0xFF == ord('q'):
			break
		
		
root=tk.Tk()
root.title("YÜZ TANIMA")
root.geometry("350x350+30+30")
root.configure(background='grey')

btn1=tk.Button(root,text="YÜZ TANIMA", fg="white", bg="blue", command=onclickBtn1)
btn1.pack(padx=10, pady=100)

btn2=tk.Button(root,text="KAPAT", bg="red", fg="white", width=10,command=root.destroy)
btn2.pack(padx=10, pady=10)


root.mainloop()