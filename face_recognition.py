from email import message
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np
from time import strftime
from datetime import datetime


class face_recognition:
    def __init__(self,root):
        self.root= root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face recognition")


        #background 
        imgg=Image.open(r"C:\Users\mukes\Desktop\images\face.png")
        imgg=imgg.resize((1530,790),Image.ANTIALIAS)
        self.photo=ImageTk.PhotoImage(imgg)

        bg_img=Label(self.root,image=self.photo)
        bg_img.place(x=0,y=0)

        #img1=Image.open(r"C:\Users\mukes\Desktop\images\face1.jpg")
        #img1=img1.resize((500,500),Image.ANTIALIAS)
        #self.photo1=ImageTk.PhotoImage(img1)

        #face_img1=Label(bg_img,image=self.photo1)
        #face_img1.place(x=35,y=140)

        #title_lbl=Label(bg_img,text="FACE RECOGNITION",font=("calibri",25,"bold"))
        #title_lbl.place(x=35,y=20,width=1450,height=50)

        lbl1=Label(bg_img,text="CLICK ON THE BUTTON BELOW FOR FACE RECOGNITION",font=("calibri",16,"bold"),bg="orange",fg="black")
        lbl1.place(x=520,y=350,width=500,height=50)

        #button
        face_btn=Button(bg_img,text="FACE RECOGNIZE",command=self.face_recog,width=20,font=("calibri",14,"bold"),bg="skyblue",fg="black")
        face_btn.place(x=660,y=445)
        
    #**********attendance***********
        
    def mark_attendance(self,i,j):
            with open("attendance.csv","r+",newline="\n") as f:
                myDataList=f.readlines()
                name_list=[]
                for line in myDataList:
                    entry=line.split((","))
                    name_list.append(entry[0])
                if((i not in name_list)) and ((i not in name_list)):
                    now=datetime.now()
                    d1=now.strftime("%d/%m/%Y")
                    dtString=now.strftime("%H:%M:%S")
                    f.writelines(f"\n{i},{j},{dtString},{d1},Present")
                         

        #**********face recognition function******

    def face_recog(self):
        def draw_boundary(img,classifier,scaleFactor,minNeighbors,color,text,clf):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)

            coord=[]

            for (x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,255),3)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                confidence=int((100*(1-predict/300)))

                conn=mysql.connector.connect(host="localhost",username="root",password="root",database="face_recognition")
                my_cursor=conn.cursor()
                
                my_cursor.execute("select name from student where stdid="+str(id))
                i=my_cursor.fetchone()
                i="+".join(i)

                my_cursor.execute("select regno from student where stdid="+str(id))
                j=my_cursor.fetchone()
                j="+".join(j)

                if confidence>77:
                    cv2.putText(img,f"NAME: {i}",(x,y-60),cv2.FONT_ITALIC,0.8,(0,255,0),3)
                    cv2.putText(img,f"REGISTER NO.: {j}",(x,y-30),cv2.FONT_ITALIC,0.8,(0,255,0),3)
                    self.mark_attendance(i,j)
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,"UNKNOWN FACE",(x,y-5),cv2.FONT_ITALIC,0.8,(255,255,0),3)
                
                coord=[x,y,w,h]

            return coord 

        def recognize(img,clf,faceCascade):
            coord=draw_boundary(img,faceCascade,1.1,10,(255,25,225),"Face",clf)
            return img

        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf= cv2.face_LBPHFaceRecognizer.create()
        clf.read("classifier.xml")

        video_cap=cv2.VideoCapture(0)

        while True:
            ret,img=video_cap.read()
            img=recognize(img,clf,faceCascade)
            cv2.imshow("Welcome to Face Recognition",img)

            if cv2.waitKey(1)==13:
                break
        video_cap.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    root=Tk()
    obj=face_recognition(root)
    root.mainloop()


