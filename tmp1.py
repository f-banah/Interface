import tkinter
import tkinter.ttk as ttk
import mysql.connector
import tkinter.messagebox as MessageBox
from tkinter import*

def insert():
    if(e_idFiliere.get()=="" or e_nomFiliere.get()==""):
        MessageBox.showinfo("Insert status", "Des champs sont manquants")


     else:

        conn=mysql.connector.connect(host="sql3.freemysqlhosting.net",user="sql3348311",password="SLxH2RVI6h", database="sql3348311")
        cursor = conn.cursor()
        sql="INSERT INTO filiere(idFiliere,nomFiliere) VALUES (%s,%s)"
        val=(e_idFiliere.get(),e_nomFiliere.get())
        cursor.execute(sql,val)

        conn.commit();

        e_idFiliere.delete(0,'end')
        e_nomFiliere.delete(0,'end')
        MessageBox.showinfo("Insert status", "La filière a été ajoutée");
        conn.close();



def delete() :
 if(e_idFiliere.get()== ""):
        MessageBox.showinfo("Delete status", "L'id est nécessaire ")


 else:
        conn=mysql.connector.connect(host="sql3.freemysqlhosting.net",user="sql3348311",password="SLxH2RVI6h", database="sql3348311")
        cursor = conn.cursor()

        sql="DELETE FROM filiere WHERE idFiliere= %s"
        val=(e_idFiliere.get(),)
        cursor.execute(sql,val)
        conn.commit();

        e_idFiliere.delete(0,'end')
        e_nomFiliere.delete(0,'end')
        MessageBox.showinfo("Delete status", "La filière a été supprimée");
        conn.close();



def update():

    if(e_idFiliere.get()=="" or e_nomFiliere.get()==""):
        MessageBox.showinfo("Update status", "Des champs sont manquants")


    else:
        conn=mysql.connector.connect(host="sql3.freemysqlhosting.net",user="sql3348311",password="SLxH2RVI6h", database="sql3348311")
        cursor = conn.cursor()
        sql="UPDATE filiere SET nomFiliere=%s WHERE idFiliere=%s"
        val=(e_nomFiliere.get(),e_idFiliere.get())
        cursor.execute(sql,val)
        conn.commit();

        e_idFiliere.delete(0,'end')
        e_nomFiliere.delete(0,'end')
        MessageBox.showinfo("Update status", "La filière a été modifiée");
        conn.close();

def get():
 if(e_idFiliere.get()== ""):
        MessageBox.showinfo("Fetch status", "L'id est nécessaire ")


 else:
        conn=mysql.connector.connect(host="sql3.freemysqlhosting.net",user="sql3348311",password="SLxH2RVI6h", database="sql3348311")
        cursor = conn.cursor()
        sql="SELECT * FROM filiere WHERE idFiliere= %s"
        val=(e_idFiliere.get(),)
        cursor.execute(sql,val)

        rows=cursor.fetchall()

        for row in rows:
            e_nomFiliere.insert(0,row[1])

        conn.close();


root = tkinter.Tk()
root.title("Menu")

idFiliere=tkinter.Label(root,text="Entrer l'identifiant de la filière :",font=("bold",10))
idFiliere.place(x=20,y=30)

nomFiliere=tkinter.Label(root,text='Entrer le nom de la filière :',font=("bold",10))
nomFiliere.place(x=20,y=60);

e_idFiliere=tkinter.Entry()
e_idFiliere.place(x=200,y=30)


e_nomFiliere=tkinter.Entry()
e_nomFiliere.place(x=200,y=60)

insert=  tkinter.Button(root,text='ajouter',font=("italic",10),bg="white",command=insert)
insert.place(x=20,y=140)


delete=  tkinter.Button(root,text='supprimer',font=("italic",10),bg="white",command=delete)
delete.place(x=70,y=140)


update=  tkinter.Button(root,text='modifier',font=("italic",10),bg="white",command=update)
update.place(x=130,y=140)

get=  tkinter.Button(root,text='afficher',font=("italic",10),bg="white",command=get)
get.place(x=190,y=140)


def faireApparaitreLeToplevel():
    Toplevel(root)

go = Button(root , text = 'Les filières', command=faireApparaitreLeToplevel)
go.pack()


root.mainloop()



