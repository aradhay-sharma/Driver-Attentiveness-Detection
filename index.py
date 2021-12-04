from tkinter import *
from flask import Flask,redirect, url_for,render_template,request
import os

def d_dtcn():
	root = Tk()
	root.configure(background = "white")

	def function1(): 
		os.system("python drowsiness_detection.py --shape_predictor shape_predictor_68_face_landmarks.dat")
		exit()

	#def function2(): 
	#	os.system("python android_cam.py --shape_predictor shape_predictor_68_face_landmarks.dat")
	#	exit()

	
		
	root.title("Driver Attentiveness Detection")
	Label(root, text="  Driver Attentiveness Detection  ",font=("Helvetica",24),fg="white",bg="#2e8bc0",height=5).grid(row=2,rowspan=2,columnspan=5,sticky=N+E+W+S,padx=5,pady=10)
	Button(root,text="Use Webcam",font=("Helvetica",18),bg="#0c2d48",fg='white',command=function1).grid(row=5,columnspan=5,sticky=W+E+N+S,padx=5,pady=5)
	#Button(root,text="Run using phone cam",font=("times new roman",20),bg="#0D47A1",fg='white',command=function2).grid(row=7,columnspan=5,sticky=W+E+N+S,padx=5,pady=5)
	Button(root,text="Exit",font=("Helvetica",18),bg="#0c2d48",fg='white',command=root.destroy).grid(row=9,columnspan=5,sticky=W+E+N+S,padx=5,pady=5)

	root.mainloop()