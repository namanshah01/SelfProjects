from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox

window=Tk()
window.title('Personal Detail Form')
window.geometry('400x200')

#format: Enter name : _____
enter_name=Label(window,text='Enter Name :                      ')
enter_name.grid(column=0,row=0)
enter_name_txt=Entry(window,width=15)
enter_name_txt.grid(column=1,row=0)

#format: Enter Roll no : _____
enter_rollno=Label(window,text='Enter Roll no :                     ')
enter_rollno.grid(column=0,row=1)
enter_rollno_txt=Entry(window,width=15)
enter_rollno_txt.grid(column=1,row=1)

#format: Enter age : <spinbox from 12 to 25, default=18>
enter_age=Label(window,text='Enter age :                           ')
enter_age.grid(column=0,row=2)
var_spin_age=IntVar()
var_spin_age.set(0)
spin_age=Spinbox(window,from_=12,to=25,width=8,textvariable=var_spin_age)
spin_age.grid(column=1,row=2)

#format: Enter gender :  Male  Female <radiobutton>
enter_gender=Label(window,text='Enter gender :                     ')
enter_gender.grid(column=0,row=3)
gender=IntVar()
gender.set(0)
rad_gender_male=Radiobutton(window,text='Male',value=1,variable=gender)
rad_gender_male.grid(column=1,row=3)
rad_gender_female=Radiobutton(window,text='Female',value=2,variable=gender)
rad_gender_female.grid(column=2,row=3)\


#format: Programming languages :  Python  Java
#        <with checkboxes>        R       C++
#Entry text
enter_prolang=Label(window,text='Programming languages : ')
enter_prolang.grid(column=0,row=4)
#making buttons
#button python
python_state=BooleanVar()
python_state.set(False)
cbox_python=Checkbutton(window,text='Python',var=python_state)
cbox_python.grid(column=1,row=4)
#button java
java_state=BooleanVar()
java_state.set(False)
cbox_java=Checkbutton(window,text='Java',var=java_state)
cbox_java.grid(column=2,row=4)
#button r
r_state=BooleanVar()
r_state.set(False)
cbox_r=Checkbutton(window,text='R           ',var=r_state)
cbox_r.grid(column=1,row=5)
#button C++
cplus_state=BooleanVar()
cplus_state.set(False)
cbox_cplus=Checkbutton(window,text='C++',var=cplus_state)
cbox_cplus.grid(column=2,row=5)


#format: 12th pass, Graduate, Post Graduate, Doctorate <drop down menu>
enter_qual=Label(window,text='Qualifications : ')
enter_qual.grid(column=0,row=6)
qual=Combobox(window)
qual['values']=('12th pass','Graduate','Post Graduate','Doctorate')
#qual.current(1)
qual.grid(column=1,row=6)


#Validation of the entries
def validate():
    if enter_name_txt.get()=='':
        messagebox.showerror('Error','Name not filled')
    elif enter_rollno_txt.get()=='':
        messagebox.showerror('Error','Roll no not filled')
    elif var_spin_age.get()==0:
        messagebox.showerror('Error','Age not filled')
    elif gender.get()==0:
        messagebox.showerror('Error','Gender not filled')
    elif python_state.get()==False and java_state.get()==False and r_state.get()==False and cplus_state.get()==False:
        messagebox.showerror('Error','Programming language not filled')
    elif qual.get()=='':
        messagebox.showerror('Error','Qualifications not filled')
    else:
        res=messagebox.showinfo('Confirm','Submission complete')
        window.destroy()

# confirming cancellation of submission
def confirm_can():
    MsgBox = messagebox.askquestion ('Exit Application','Are you sure you want to exit the application',icon = 'warning')
    if MsgBox == 'yes':
       window.destroy()


cancel_but=Button(window,text='Cancel',command=confirm_can)
cancel_but.grid(column=1,row=7)
save_but=Button(window,text='Save',command=validate)
save_but.grid(column=0,row=7)
