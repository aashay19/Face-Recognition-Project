from email import message
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import cv2
import os
import numpy as np

class train:
    def __init__(self,root):
        self.root= root
        self.root.geometry("1530x790+0+0")
        self.root.title("Train the images")


        #background 
        img=Image.open(r"C:\Users\mukes\Desktop\images\train.png")
        img=img.resize((1530,790),Image.ANTIALIAS)
        self.photo=ImageTk.PhotoImage(img)

        bg_img=Label(self.root,image=self.photo)
        bg_img.place(x=0,y=0)

        #img1=Image.open(r"C:\Users\mukes\Desktop\images\trim2.png")
        #img1=img1.resize((500,500),Image.ANTIALIAS)
        #self.photo1=ImageTk.PhotoImage(img1)

        #train_img1=Label(bg_img,image=self.photo1)
        #train_img1.place(x=35,y=140)

        #title_lbl=Label(bg_img,text="TRAIN YOUR DATA",font=("calibri",25,"bold"))
        #title_lbl.place(x=35,y=20,width=1450,height=50)

        lbl1=Label(bg_img,text="CLICK ON THE BUTTON BELOW TO TRAIN YOUR DATA",font=("calibri",16,"bold"),bg="orange",fg="black")
        lbl1.place(x=540,y=300,width=500,height=50)

        #button
        train_btn=Button(bg_img,text="TRAIN",command=self.train_classify,width=16,font=("calibri",14,"bold"),bg="skyblue",fg="black")
        train_btn.place(x=680,y=490)

    def train_classify(self):
        data_dir=("data")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]

        faces=[]
        ids=[]

        for image in path:
            img=Image.open(image).convert('L')  #Gray scale image
            imageNp=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Train",imageNp)
            cv2.waitKey(1)==13
        ids=np.array(ids)

        #*********train the images*********
        clf = cv2.face_LBPHFaceRecognizer.create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training data completed") 





if __name__ == "__main__":
    root=Tk()
    obj=train(root)
    root.mainloop()