from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from face_recognition import face_recognition
from student import student
from train import train
from face_recognition import face_recognition
from attendance import attendance

class face_recognition_System:
    def __init__(self,root):
        self.root= root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        #background 
        img=Image.open(r"C:\Users\mukes\Desktop\images\bg2.png")
        img=img.resize((1530,790),Image.ANTIALIAS)
        self.photo=ImageTk.PhotoImage(img)

        bg_img=Label(self.root,image=self.photo)
        bg_img.place(x=0,y=0)

        #Student details button
        
        img1=Image.open(r"C:\Users\mukes\Desktop\images\student1.png")
        img1=img1.resize((260,220),Image.ANTIALIAS)
        self.photo1=ImageTk.PhotoImage(img1)

        b1=Button(bg_img,image=self.photo1,command=self.student_details,cursor="hand2")
        b1.place(x=450,y=200,width=300,height=220)

        b1_1=Button(bg_img,text="STUDENT DETAILS",command=self.student_details,cursor="hand2",font=("calibri",18,"bold",),bg="lightblue",fg="black")
        b1_1.place(x=450,y=400,width=300,height=40)

        #Train data button
        
        img2=Image.open(r"C:\Users\mukes\Desktop\images\train.jpg")
        img2=img2.resize((260,220),Image.ANTIALIAS)
        self.photo2=ImageTk.PhotoImage(img2)

        b2=Button(bg_img,image=self.photo2,cursor="hand2",command=self.train_data)
        b2.place(x=780,y=200,width=300,height=220)

        b2_1=Button(bg_img,text="TRAIN DATA",command=self.train_data,cursor="hand2",font=("calibri",18,"bold",),bg="lightblue",fg="black")
        b2_1.place(x=780,y=400,width=300,height=40)

        #Face Recognition button
        
        img3=Image.open(r"C:\Users\mukes\Desktop\images\facebg.jpg")
        img3=img3.resize((260,220),Image.ANTIALIAS)
        self.photo3=ImageTk.PhotoImage(img3)

        b3=Button(bg_img,image=self.photo3,cursor="hand2",command=self.face_data)
        b3.place(x=450,y=500,width=300,height=220)

        b3_1=Button(bg_img,text="FACE RECOGNITION",cursor="hand2",command=self.face_data,font=("calibri",18,"bold",),bg="lightblue",fg="black")
        b3_1.place(x=450,y=700,width=300,height=40)

        #Attendance button
        
        img4=Image.open(r"C:\Users\mukes\Desktop\images\attendance.png")
        img4=img4.resize((260,220),Image.ANTIALIAS)
        self.photo4=ImageTk.PhotoImage(img4)

        b4=Button(bg_img,image=self.photo4,cursor="hand2",command=self.attend)
        b4.place(x=780,y=500,width=300,height=220)

        b4_1=Button(bg_img,text="ATTENDANCE",cursor="hand2",command=self.attend,font=("calibri",18,"bold",),bg="lightblue",fg="black")
        b4_1.place(x=780,y=700,width=300,height=40)

    
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=student(self.new_window)

    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=train(self.new_window)

    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=face_recognition(self.new_window)
        
    def attend(self):
        self.new_window=Toplevel(self.root)
        self.app=attendance(self.new_window)         



if __name__ == "__main__":
    root=Tk()
    obj=face_recognition_System(root)
    root.mainloop()