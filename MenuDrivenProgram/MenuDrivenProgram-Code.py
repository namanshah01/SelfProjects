import os

class File:
    def __init__(self):
        self.task=input("1 - Add Record\n2 - Update Record\n3 - Delete Record\n4 - Show Record\n5 - Search Record\n6 - Quit\nEnter input : ")
        while(self.task!='6'):
            if self.task=='1':
                self.Add()
            elif self.task=='2':
                self.Update()
            elif self.task=='3':
                self.Delete()
            elif self.task=='4':
                self.Show()
            elif self.task=='5':
                self.Search()
            self.task=input("1 - Add Record\n2 - Update Record\n3 - Delete Record\n4 - Show Record\n5 - Search Record\n6 - Quit\nEnter input : ")

    #Add Record
    def Add(self):
        #taking input
        self.rollno=input("Enter rollno : ")
        self.name=input("Enter name : ")
        self.address=input("Enter address : ")
        #storing the input with separating parameters(";" - sep inside block, "." - sep of blocks)
        #"store_info.txt" original text file to store info(append mode)
        self.store=open("store_info.txt","a")
        self.store_list=[self.rollno+';',self.name+';',self.address+'.']
        self.store.writelines(self.store_list)
        self.store.close()
        print("Record added successfully\n")

    #Delete Record
    def Delete(self):
        #input rollno to be deleted
        s_roll=input("Enter rollno to be deleted : ")
        #"store_info.txt" original text file to store info(read mode)
        file_show=open("store_info.txt","r")
        data=file_show.read()
        #"new_store_info.txt" new text file with temporary name(w+ mode, same as append mode)
        new_file=open("new_store_info.txt","w+")
        #spliting all the info into blocks(form of block in .txt file - rollno;name;address.)
        info_block=data.split(".")
        #next 5 lines to check if the input rollno exists in the file
        check=False
        for counter in range (0,len(info_block)-1):
            temp_block=info_block[counter].split(";")
            if temp_block[0]==s_roll:
                check=True
        #if there is a match in the roll no, all the info blocks from of original file is copied
        #to the new file except the block of the rollno to be deleted
        if check==True:
            for counter in range (0,len(info_block)-1):
                temp_block=info_block[counter].split(";")
                if temp_block[0]!=s_roll:
                    info_block[counter]+='.'
                    new_file.writelines(info_block[counter])
            #original file is deleted, the new file with the updated info is given the name of the
            #original file so the code keeps running with the same file name
            file_show.close()
            new_file.close()
            os.remove("store_info.txt")
            os.rename("new_store_info.txt","store_info.txt")
            print("Record successfully deleted\n")
        else:
            print("Record not found\n")

    #Update Record
    def Update(self):
        #explanation of the code similar to the Delete method
        s_roll=input("Enter rollno to be update : ")

        file_show=open("store_info.txt","r")
        data=file_show.read()
        new_file=open("new_store_info.txt","w+")

        info_block=data.split(".")

        check=False
        for counter in range (0,len(info_block)-1):
            temp_block=info_block[counter].split(";")
            if temp_block[0]==s_roll:
                check=True

        if check==True:
            for counter in range (0,len(info_block)-1):
                temp_block=info_block[counter].split(";")
                if temp_block[0]!=s_roll:
                    info_block[counter]+='.'
                    new_file.writelines(info_block[counter])
                else:
                    temp_block[1]=input("Enter new name : ")
                    temp_block[2]=input("Enter new address : ")
                    info_block[counter]=temp_block[0]+";"+temp_block[1]+";"+temp_block[2]+"."
                    new_file.writelines(info_block[counter])
            file_show.close()
            new_file.close()
            os.remove("store_info.txt")
            os.rename("new_store_info.txt","store_info.txt")
            print("Record successfully updated\n")
        else:
            print("Record not found\n")

    #Show Record
    def Show(self):
        file_show=open("store_info.txt","r")
        data=file_show.read()
        print((data.replace(";","\t")).replace(".","\n"))
        file_show.close()

    #Search Record
    def Search(self):
        s_roll=input("Enter rollno to be searched : ")

        file_show=open("store_info.txt","r")
        data=file_show.read()

        info_block=data.split(".")
        for counter in range (0,len(info_block)):
            temp_block=info_block[counter].split(";")
            if temp_block[0]==s_roll:
                print("Record found :",info_block[counter].replace(";","\t"),"\n")
                break
        if counter==(len(info_block)-1):
            print("Record not found\n")
        file_show.close()

#only object is to be made, all the other methods are called from the constructor itself
f=File()
