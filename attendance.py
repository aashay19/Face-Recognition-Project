from email import message
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
from time import strftime
from datetime import datetime
import csv
from tkinter import filedialog


mydata=[]
class attendance:
    def __init__(self,root):
        self.root= root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face recognition")
        
        #*************variables**********
        self.var_name=StringVar()
        self.var_regno=StringVar()
        self.var_time=StringVar()
        self.var_date=StringVar()
        self.var_status=StringVar()
        
        #background 
        img=Image.open(r"C:\Users\mukes\Desktop\images\attendancebg.png")
        img=img.resize((1530,790),Image.ANTIALIAS)
        self.photo=ImageTk.PhotoImage(img)

        bg_img=Label(self.root,image=self.photo)
        bg_img.place(x=0,y=0)
        
        
        
        #name
        std_name=Label(bg_img,text="NAME: ",font=("calibri",12,"bold"),border=5,bg="grey",fg="black")
        std_name.place(x=125,y=300)

        std_name_entry=ttk.Entry(bg_img,width=50,textvariable=self.var_name,font=("calibri",12,"bold"))
        std_name_entry.place(x=250,y=304)
        
        #regno
        std_regno=Label(bg_img,text="REGISTER NO.: ",font=("calibri",12,"bold"),border=5,bg="grey",fg="black")
        std_regno.place(x=125,y=350)

        std_regno_entry=ttk.Entry(bg_img,width=50,textvariable=self.var_regno,font=("calibri",12,"bold"))
        std_regno_entry.place(x=250,y=354)
        
        #Date
        std_date=Label(bg_img,text="DATE: ",font=("calibri",12,"bold"),border=5,bg="grey",fg="black")
        std_date.place(x=125,y=400)

        std_date_entry=ttk.Entry(bg_img,width=50,textvariable=self.var_date,font=("calibri",12,"bold"))
        std_date_entry.place(x=250,y=404)
        
        #Time
        std_time=Label(bg_img,text="TIME: ",font=("calibri",12,"bold"),border=5,bg="grey",fg="black")
        std_time.place(x=125,y=450)

        std_time_entry=ttk.Entry(bg_img,width=50,textvariable=self.var_time,font=("calibri",12,"bold"))
        std_time_entry.place(x=250,y=454)
        
        #Attendance status
        atd_status=Label(bg_img,text="Status",font=("calibri",12,"bold"),border=5,bg="grey",fg="black")
        atd_status.place(x=125,y=500)

        atd_status__combo=ttk.Combobox(bg_img,font=("calibri",12,"bold"),textvariable=self.var_status,state="readonly")
        atd_status__combo["values"]=("Status","Present","Absent")
        atd_status__combo.current(0)
        atd_status__combo.place(x=250,y=504)
        
        #buttons
        
        update_btn=Button(bg_img,text="UPDATE",width=16,font=("calibri",14,"bold"),bg="lightblue",fg="black")
        update_btn.place(x=125,y=550)
        
        reset_btn=Button(bg_img,text="RESET",command=self.reset_data,width=16,font=("calibri",14,"bold"),bg="lightblue",fg="black")
        reset_btn.place(x=335,y=550)
        
        #Button frame
        button_frame = LabelFrame(bg_img,bd=10,relief=RIDGE)
        button_frame.place(x=800,y=640,width=600,height=60)
        
        import_csv_btn=Button(button_frame,text="IMPORT CSV",command=self.importcsv,width=28,font=("calibri",14,"bold"),bg="lightblue",fg="black")
        import_csv_btn.grid(row=0,column=0)
        
        export_csv_btn=Button(button_frame,text="EXPORT CSV",command=self.exportcsv,width=28,font=("calibri",14,"bold"),bg="lightblue",fg="black")
        export_csv_btn.grid(row=0,column=1)
        
        
        #Right label frame
        Right_frame = LabelFrame(bg_img,bd=10,relief=RIDGE)
        Right_frame.place(x=800,y=200,width=600,height=400)

        scroll_x=ttk.Scrollbar(Right_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(Right_frame,orient=VERTICAL)

        self.student_table=ttk.Treeview(Right_frame,column=("Name","Register number","Time","Date","Attendance Status"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("Name",text="Name")
        self.student_table.heading("Register number",text="Register number")
        self.student_table.heading("Time",text="Time")
        self.student_table.heading("Date",text="Date")
        self.student_table.heading("Attendance Status",text="Attendance Status")
        self.student_table["show"]="headings"

        self.student_table.column("Name",width=100)
        self.student_table.column("Register number",width=120)
        self.student_table.column("Time",width=100)
        self.student_table.column("Date",width=100)
        self.student_table.column("Attendance Status",width=120)

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        
        
    #***********fetch data*************
    
    def fetchdata(self,rows):
        self.student_table.delete(*self.student_table.get_children())
        for i in rows:
            self.student_table.insert("",END,values=i)
    
    # import csv
    def importcsv(self):
        global mydata
        mydata.clear()
        f=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
        with open(f) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchdata(mydata)
            
    #export csv
    def exportcsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("No Data","No Data found",parent=self.root)
                return False
            f=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
            with open(f,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data export","Your data has been exported successfully")
        except Exception as es:
                messagebox.showerror("Error",f"Error occured due to:{str(es)}",parent=self.root)
                
    def get_cursor(self,event=""):
        cursor_row=self.student_table.focus()
        content=self.student_table.item(cursor_row)
        rows=content['values']
        self.var_name.set(rows[0])
        self.var_regno.set(rows[1])                       
        self.var_time.set(rows[2])   
        self.var_date.set(rows[3])   
        self.var_status.set(rows[4])
        
        
    def reset_data(self):
        self.var_name.set("")
        self.var_regno.set("")                       
        self.var_time.set("")   
        self.var_date.set("")   
        self.var_status.set("")      
                          
            
            
      
        

if __name__ == "__main__":
    root=Tk()
    obj=attendance(root)
    root.mainloop()