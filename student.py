from email import message
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

class student:
    def __init__(self,root):
        self.root= root
        self.root.geometry("1530x790+0+0")
        self.root.title("Student Details")

        #variable

        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_name=StringVar()
        self.var_regno=StringVar()
        self.var_stdid=StringVar()
        self.var_gender=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        


        #background 
        img=Image.open(r"C:\Users\mukes\Desktop\images\student_bg.png")
        img=img.resize((1530,790),Image.ANTIALIAS)
        self.photo=ImageTk.PhotoImage(img)

        bg_img=Label(self.root,image=self.photo)
        bg_img.place(x=0,y=0)

        #main frame
        #main_frame=Frame(bg_img,bd=2)
        #main_frame.place(x=50,y=110,width=1420,height=640)

        #left label frame
        #Left_frame = LabelFrame(main_frame,bd=5,relief=RIDGE)
        #Left_frame.place(x=10,y=20,width=690,height=600)

        #img1=Image.open(r"C:\Users\mukes\Desktop\images\frame_pic.jpg")
        #img1=img1.resize((675,100),Image.ANTIALIAS)
        #self.photo1=ImageTk.PhotoImage(img1)

        #left_pic=Label(main_frame,image=self.photo1)
        #left_pic.place(x=16,y=25)

        #left_label= Label(left_pic,text="STUDENT DETAILS",font=("calibri",20,"bold"))
        #left_label.place(x=210,y=25,width=250,height=50)

        #course 

        course_frame = LabelFrame(bg_img,bd=5,relief=RIDGE)
        course_frame.place(x=90,y=220,width=680,height=150)
        
        #department
        dep_label=Label(course_frame,text="Department",font=("calibri",12,"bold"),bg="white")
        dep_label.grid(row=0,column=0,padx=10,sticky=W)

        dep_combo=ttk.Combobox(course_frame,textvariable=self.var_dep,font=("calibri",12,"bold"),state="readonly")
        dep_combo["values"]=("Select Department","Computer","IT","ECE","EEE")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)
        
        #course
        course_label=Label(course_frame,text="Course",font=("calibri",12,"bold"),bg="white")
        course_label.grid(row=0,column=2,padx=10,sticky=W)

        course_combo=ttk.Combobox(course_frame,textvariable=self.var_course,font=("calibri",12,"bold"),state="readonly")
        course_combo["values"]=("Select Course","FE","SE","TE","BE")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)

        #year
        year_label=Label(course_frame,text="Year",font=("calibri",12,"bold"),bg="white")
        year_label.grid(row=1,column=0,padx=10,sticky=W)

        year_combo=ttk.Combobox(course_frame,textvariable=self.var_year,font=("calibri",12,"bold"),state="readonly")
        year_combo["values"]=("Select Year","2020-21","2021-22","2022-23","2023-24")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)

        #semester
        sem_label=Label(course_frame,text="Semester",font=("calibri",12,"bold"),bg="white")
        sem_label.grid(row=1,column=2,padx=10,sticky=W)

        sem_combo=ttk.Combobox(course_frame,textvariable=self.var_semester,font=("calibri",12,"bold"),state="readonly")
        sem_combo["values"]=("Select Semester","Semester-1","Semester-2")
        sem_combo.current(0)
        sem_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)

        #details frame

        details_frame = LabelFrame(bg_img,bd=5,relief=RIDGE)
        details_frame.place(x=90,y=340,width=680,height=350)
        
        #student name
        std_name=Label(details_frame,text="Student Name",font=("calibri",12,"bold"),bg="white")
        std_name.grid(row=0,column=0,padx=10,pady=10,sticky=W)

        std_name_entry=ttk.Entry(details_frame,textvariable=self.var_name,width=60,font=("calibri",12,"bold"))
        std_name_entry.grid(row=0,column=1,padx=10,pady=10,sticky=W)

        #student reg.no
        std_regno=Label(details_frame,text="Register Number",font=("calibri",12,"bold"),bg="white")
        std_regno.grid(row=1,column=0,padx=10,pady=10,sticky=W)

        std_regno_entry=ttk.Entry(details_frame,textvariable=self.var_regno,width=60,font=("calibri",12,"bold"))
        std_regno_entry.grid(row=1,column=1,padx=10,pady=10,sticky=W)

        #student id
        std_id=Label(details_frame,text="Student id",font=("calibri",12,"bold"),bg="white")
        std_id.grid(row=2,column=0,padx=10,pady=10,sticky=W)

        std_id_entry=ttk.Entry(details_frame,textvariable=self.var_stdid,width=60,font=("calibri",12,"bold"))
        std_id_entry.grid(row=2,column=1,padx=10,pady=10,sticky=W)

        #Gender
        std_gender=Label(details_frame,text="Gender",font=("calibri",12,"bold"),bg="white")
        std_gender.grid(row=3,column=0,padx=10,pady=10,sticky=W)

        std_gender__combo=ttk.Combobox(details_frame,textvariable=self.var_gender,font=("calibri",12,"bold"),state="readonly")
        std_gender__combo["values"]=("Select Gender","Male","Female","Other")
        std_gender__combo.current(0)
        std_gender__combo.grid(row=3,column=1,padx=10,pady=10,sticky=W)

        #Email
        std_email=Label(details_frame,text="Email",font=("calibri",12,"bold"),bg="white")
        std_email.grid(row=4,column=0,padx=10,pady=10,sticky=W)

        std_email_entry=ttk.Entry(details_frame,textvariable=self.var_email,width=60,font=("calibri",12,"bold"))
        std_email_entry.grid(row=4,column=1,padx=10,pady=10,sticky=W)

        #Phone number
        std_pho=Label(details_frame,text="Phone Number",font=("calibri",12,"bold"),bg="white")
        std_pho.grid(row=5,column=0,padx=10,pady=10,sticky=W)

        std_pho_entry=ttk.Entry(details_frame,textvariable=self.var_phone,width=60,font=("calibri",12,"bold"))
        std_pho_entry.grid(row=5,column=1,padx=10,pady=10,sticky=W)

        #Radio Button

        #self.var_radio1=StringVar()
        #radiobtn1=ttk.Radiobutton(details_frame,variable=self.var_radio1,text="Take Photo Sample",value="Yes")
        #radiobtn1.grid(row=5,column=0,pady=10)

        #radiobtn2=ttk.Radiobutton(details_frame,variable=self.var_radio1,text="Don't Take Photo Sample",value="No")
        #radiobtn2.grid(row=5,column=1,pady=10)

        #Button frame
        button_frame = LabelFrame(bg_img,bd=5,relief=RIDGE)
        button_frame.place(x=90,y=650,width=680,height=50)

        save_btn=Button(button_frame,text="SAVE",command=self.add_data,width=16,font=("calibri",14,"bold"),bg="lightblue",fg="black")
        save_btn.grid(row=0,column=0)

        update_btn=Button(button_frame,text="UPDATE",command=self.update_data,width=16,font=("calibri",14,"bold"),bg="lightblue",fg="black")
        update_btn.grid(row=0,column=1)

        delete_btn=Button(button_frame,text="DELETE",command=self.delete_data,width=15,font=("calibri",14,"bold"),bg="lightblue",fg="black")
        delete_btn.grid(row=0,column=2)

        reset_btn=Button(button_frame,text="RESET",command=self.reset_data,width=16,font=("calibri",14,"bold"),bg="lightblue",fg="black")
        reset_btn.grid(row=0,column=3)

        #Button 2 frame
        button2_frame = LabelFrame(bg_img,bd=5,relief=RIDGE)
        button2_frame.place(x=850,y=650,width=600,height=50)

        addpic_btn=Button(button2_frame,command=self.generate_dataset,text="ADD PHOTO",width=29,font=("calibri",14,"bold"),bg="lightblue",fg="black")
        addpic_btn.grid(row=0,column=0)

        updatepic_btn=Button(button2_frame,text="UPDATE PHOTO",width=28,font=("calibri",14,"bold"),bg="lightblue",fg="black")
        updatepic_btn.grid(row=0,column=1)
     
        
        #Right label frame
        #Right_frame = LabelFrame(main_frame,bd=5,relief=RIDGE)
        #Right_frame.place(x=715,y=20,width=690,height=600)

        #img2=Image.open(r"C:\Users\mukes\Desktop\images\frame_pic.jpg")
        #img2=img2.resize((675,100),Image.ANTIALIAS)
        #self.photo2=ImageTk.PhotoImage(img2)

        #right_pic=Label(main_frame,image=self.photo2)
        #right_pic.place(x=720,y=25)

        #right_label= Label(main_frame,text="STUDENT DATA",font=("calibri",20,"bold"))
        #right_label.place(x=950,y=52,width=250,height=50)

        #******SEARCH SYSTEM******#

        #search_frame = LabelFrame(main_frame,bd=5,relief=RIDGE)
        #search_frame.place(x=722,y=130,width=675,height=50)

        #search_label=Label(search_frame,text="SEARCH-BY",font=("calibri",12,"bold"),bg="lightblue",fg="black")
        #search_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        #search_combo=ttk.Combobox(search_frame,font=("calibri",12,"bold"),state="readonly")
        #search_combo["values"]=("Select","Name","Register number")
        #search_combo.current(0)
        #search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        #search_entry=ttk.Entry(search_frame,width=20,font=("calibri",12,"bold"))
        #search_entry.grid(row=0,column=2,padx=10,pady=10,sticky=W)
        
        #search_btn=Button(search_frame,text="SEARCH",width=10,font=("calibri",12,"bold"),bg="orange",fg="black")
        #search_btn.grid(row=0,column=3)

        #showall_btn=Button(search_frame,text="SHOWALL",width=10,font=("calibri",12,"bold"),bg="orange",fg="black")
        #showall_btn.grid(row=0,column=4,padx=5)

        #TABLE FRAME
        table_frame = LabelFrame(bg_img,bd=5,relief=RIDGE)
        table_frame.place(x=850,y=220,width=600,height=400)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.student_table=ttk.Treeview(table_frame,column=("Department","Course","Year","Semester","Name","Register number","Student Id","Gender","Email","Phone Number"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("Department",text="Department")
        self.student_table.heading("Course",text="Course")
        self.student_table.heading("Year",text="Year")
        self.student_table.heading("Semester",text="Semester")
        self.student_table.heading("Name",text="Name")
        self.student_table.heading("Register number",text="Register number")
        self.student_table.heading("Student Id",text="Student Id")
        self.student_table.heading("Gender",text="Gender")
        self.student_table.heading("Email",text="Email")
        self.student_table.heading("Phone Number",text="Phone Number")
        self.student_table["show"]="headings"

        self.student_table.column("Department",width=100)
        self.student_table.column("Course",width=100)
        self.student_table.column("Year",width=100)
        self.student_table.column("Semester",width=100)
        self.student_table.column("Name",width=100)
        self.student_table.column("Register number",width=120)
        self.student_table.column("Student Id",width=120)
        self.student_table.column("Gender",width=100)
        self.student_table.column("Email",width=100)
        self.student_table.column("Phone Number",width=120)

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()
        
        
   
    #*******function declaration********

    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_name.get()=="" or self.var_regno.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="root",database="face_recognition")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(

                                                                                                            self.var_dep.get(),
                                                                                                            self.var_course.get(),
                                                                                                            self.var_year.get(),
                                                                                                            self.var_semester.get(),
                                                                                                            self.var_name.get(),
                                                                                                            self.var_regno.get(),
                                                                                                            self.var_stdid.get(),
                                                                                                            self.var_gender.get(),
                                                                                                            self.var_email.get(),
                                                                                                            self.var_phone.get()
                                                                                
                                                                                                            ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("success","Student details has been added Successfully",parent=self.root) 
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)        


    #*****fetch data*******

    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="root",database="face_recognition")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    #****************get cursor********
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]

        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_semester.set(data[3]),
        self.var_name.set(data[4]),
        self.var_regno.set(data[5]),
        self.var_stdid.set(data[6]),
        self.var_gender.set(data[7]),
        self.var_email.set(data[8]),
        self.var_phone.set(data[9])

    # update function

    def update_data(self):
        if self.var_dep.get()=="Select Department" or self.var_name.get()=="" or self.var_regno.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
                Upadate=messagebox.askyesno("Update","Do you want to update this student details",parent=self.root)
                if Upadate>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="root",database="face_recognition")
                    my_cursor=conn.cursor()
                    my_cursor.execute("update student set dep=%s,course=%s,year=%s,semester=%s,name=%s,regno=%s,gender=%s,email=%s,phone=%s where stdid=%s",
                        (
                                                                                                                             
                            self.var_dep.get(),
                            self.var_course.get(),
                            self.var_year.get(),
                            self.var_semester.get(),
                            self.var_name.get(),
                            self.var_regno.get(),
                            self.var_gender.get(),
                            self.var_email.get(),
                            self.var_phone.get(),
                            self.var_stdid.get()
                                                                                                                            
                        ))     
                
                else:
                    if not Upadate:
                        return                                                                                                          
                messagebox.showinfo("Success","Students details successfully updated",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Error occured due to:{str(es)}",parent=self.root)   


    # delete function
    def delete_data(self):
        if self.var_stdid.get()=="":
            messagebox.showerror("Error","Student register number must be present",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Student delete page","Are you sure you want to delete the student details",parent=self.root)
                if delete>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="root",database="face_recognition")
                    my_cursor=conn.cursor()
                    sql="delete from student where stdid=%s"
                    val=(self.var_stdid.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return    
                
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Student data successfully deleted",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Error occured due to:{str(es)}",parent=self.root)    

    # reset function

    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_semester.set("Select Semester")
        self.var_name.set("")
        self.var_regno.set("")
        self.var_stdid.set("")
        self.var_gender.set("Select Gender")
        self.var_email.set("")
        self.var_phone.set("")


    #************* Take photo sample************
    def generate_dataset(self):
        if self.var_dep.get()=="Select Department" or self.var_name.get()=="" or self.var_regno.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
                Upadate=messagebox.askyesno("Update","Are you sure you want to add the photo?",parent=self.root)
                if Upadate>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="root",database="face_recognition")
                    my_cursor=conn.cursor()
                    my_cursor.execute("select * from student")
                    myresult=my_cursor.fetchall()
                    id=0
                    for x in myresult:
                        id=id+1
                    my_cursor.execute("update student set dep=%s,course=%s,year=%s,semester=%s,name=%s,regno=%s,gender=%s,email=%s,phone=%s where stdid=%s",
                                    (
                                                                                                                             
                                        self.var_dep.get(),
                                        self.var_course.get(),
                                        self.var_year.get(),
                                        self.var_semester.get(),
                                        self.var_name.get(),
                                        self.var_regno.get(),
                                        self.var_gender.get(),
                                        self.var_email.get(),
                                        self.var_phone.get(),
                                        self.var_stdid.get()
                                                                                                                            
                                    )) 
                    
                    conn.commit()
                    self.fetch_data()
                    self.reset_data()
                    conn.close()

                    # LOAD LIBRARY FROM OPEN CV

                    face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                    def face_crop(img):
                        gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                        faces=face_classifier.detectMultiScale(gray,1.3,5)

                        for (x,y,w,h) in faces:
                            face_crop=img[y:y+h,x:x+w]
                            return face_crop

                    cap=cv2.VideoCapture(0)
                    img_id=0
                    while True:
                        ret,my_frame=cap.read()
                        if face_crop(my_frame) is not None:
                            img_id+=1
                            face=cv2.resize(face_crop(my_frame),(450,450))
                            face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY) 
                            file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                            cv2.imwrite(file_name_path,face)
                            cv2.putText(face,str(img_id),(50,50),cv2.FONT_ITALIC,2,(0,255,255),2)
                            cv2.imshow("Cropped Face",face)

                        if cv2.waitKey(1)==13 or int(img_id)==100:
                            break

                    cap.release()
                    cv2.destroyAllWindows()
                    messagebox.showinfo("result","Generating of image sample completed")

            except Exception as es:
                messagebox.showerror("Error",f"Error occured due to:{str(es)}",parent=self.root)                
                    



                                                                                                                                                            

if __name__ == "__main__":
    root=Tk()
    obj=student(root)
    root.mainloop()