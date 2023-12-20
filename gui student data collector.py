from tkinter import *
import csv
import os.path
from pathlib import Path
#from github import Github

root = Tk()
root.geometry("500x500")
def calculation():
    na = sn_en.get()
    roll = sroll_en.get()
    seme1 = se1_en.get()
    seme1_1 = se1_en.get()
    seme2 = se2_en.get()
    seme2_2 = se2_en.get()
    seme3 = se3_en.get()
    seme3_3 = se3_en.get()
    seme4 = se4_en.get()
    seme4_4 = se4_en.get()
    seme5 = se5_en.get()
    seme5_5 = se5_en.get()
    seme6 = se6_en.get()
    seme6_6 = se6_en.get()
    seme7 = se7_en.get()
    seme7_7 = se7_en.get()
    seme8 = se8_en.get()
    seme8_8 = se8_en.get()

    total_semester_mark = eval(seme1)+eval(seme2)+eval(seme3)+eval(seme4)+eval(seme5)+eval(seme6)+eval(seme7)+eval(seme8)
    average = total_semester_mark/8

    if average >= 20.0:
        student_report = "Pass" 
    else:
        student_report = "Fail"
    
    #DROPOUT STUDENT COUNT
    if student_report == "Pass":
        student_dropout = 0
    else:
        student_dropout = 1

    #FILE EXIST OR NOT FINDOUT
    filecheck = os.path.isfile('training datset_csv.csv')
    if filecheck == False:
        with open('training datset_csv.csv','+a') as csvfile:
            headfield = ['name','rollNo','semester1','semester2','semester3','semester4','semester5','semester6','semester7','semester8','totalmarksemester','averagemark','report','dropout'] 
            wr = csv.DictWriter(csvfile, fieldnames=headfield)
            wr.writeheader()
            csvfile.close()
        
   
    with open('training datset_csv.csv','+a') as csvfile:
        data = [na,roll,seme1_1,seme2_2,seme3_3,seme4_4,seme5_5,seme6_6,seme7_7,seme8_8,total_semester_mark,average,student_report,student_dropout]
        wr = csv.DictWriter(csvfile, fieldnames= data)
        wr.writeheader()
        print("csvfile creted")

    print("Program Running Successfully.. :)")
    exit()
    

sn = Label(root,text = "StudentName :")
sn.pack()
sn_en = Entry(root,width = 30)
sn_en.pack()

sroll = Label(text ="RollNo :")
sroll.pack()
sroll_en = Entry(root, width=30)
sroll_en.pack()

se_1 = Label(root,text = "Semester 1 :")
se_1.pack()
se1_en = Entry(root,width = 30)
se1_en.pack()

se_2= Label(root,text = "Semester 2 :")
se_2.pack()
se2_en = Entry(root,width = 30)
se2_en.pack()

se_3= Label(root,text = "Semester 3 :")
se_3.pack()
se3_en = Entry(root,width = 30)
se3_en.pack()

se_4= Label(root,text = "Semester 4 :")
se_4.pack()
se4_en = Entry(root,width = 30)
se4_en.pack()

se_5= Label(root,text = "Semester 5 :")
se_5.pack()
se5_en = Entry(root,width = 30)
se5_en.pack()

se_6= Label(root,text = "Semester 6 :")
se_6.pack()
se6_en = Entry(root,width = 30)
se6_en.pack()

se_7= Label(root,text = "Semester 7 :")
se_7.pack()
se7_en = Entry(root,width = 30)
se7_en.pack()

se_8= Label(root,text = "Semester 8 :")
se_8.pack()
se8_en = Entry(root,width = 30)
se8_en.pack()



bu_1 = Button(root, text = 'Save', command=calculation)
bu_1.pack()

"""   #dustbin
filename = "training datset_csv.csv"
    filelocation = Path('/home/g/Documents/college mam given project')
    if filelocation.is_file():
        print("file exist") 
    else:
        print("No file in Directory")
        #headfield = ['name','rollNo','semester1','semester2','semester3','semester4','semester5','semester6','semester7','semester8','totalmarksemester','averagemark','report','dropout'] 
        #wr = csv.DictWriter(csvfile, fieldnames=headfield)
        #wr.writeheader()
        #wr = csv.writer(csvfile)
        #rowlist=[[na],[roll]]
        #wr.writerow(roll)
        #wr.writerow(rowlist)

        #github upload program
    g = Github('https://github.com/dataanalyti/studentdata.git')
    repo = g.get_repo('sandbox/gh_api')
    with open('training datset_csv.csv','r') as file:
        data = file.read()
    
    repo.creat_file('studentdata/training datset_csv.csv', 'upload csv',data, branch='main')

    print("Git file upload Successfully..")
"""

root.mainloop()