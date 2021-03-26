import tkinter
import tkinter.ttk as ttk
import mysql.connector
import tkinter.messagebox as MessageBox
from tkinter import*

def insert():
    if(e_idEtudiant.get()=="" or e_IdFiliereFK.get()=="" or e_nom.get()=="" or e_prenom.get()=="" or e_age.get()==""):
        MessageBox.showinfo("Insert status", "Des champs sont manquants")


     else:

        conn=mysql.connector.connect(host="sql3.freemysqlhosting.net",user="sql3348311",password="SLxH2RVI6h", database="sql3348311")
        cursor = conn.cursor()
        sql="INSERT INTO Etudiant(idEtudiant,IdFiliereFK,nom,prenom,age) VALUES (%s,%s,%s,%s,%s)"
        val=(e_idEtudiant.get(),e_IdFiliereFK.get(),e_nom.get(),e_prenom.get(),e_age.get())
        cursor.execute(sql,val)

        conn.commit();

        e_idEtudiant.delete(0,'end')
        e_IdFiliereFK.delete(0,'end')
        e_nom.delete(0,'end')
        e_prenom.delete(0,'end')
        e_age.delete(0,'end')
        MessageBox.showinfo("Insert status", "L'étudiant est ajouté");
        conn.close();



def delete() :
 if(e_idEtudiant.get()== ""):
        MessageBox.showinfo("Delete status", "L'id est nécessaire ")


 else:
        conn=mysql.connector.connect(host="sql3.freemysqlhosting.net",user="sql3348311",password="SLxH2RVI6h", database="sql3348311")
        cursor = conn.cursor()

        sql="DELETE FROM Etudiant WHERE idEtudiant= %s"
        val=(e_idEtudiant.get(),)
        cursor.execute(sql,val)
        conn.commit();

        e_idEtudiant.delete(0,'end')
        e_IdFiliereFK.delete(0,'end')
        e_nom.delete(0,'end')
        e_prenom.delete(0,'end')
        e_age.delete(0,'end')
        MessageBox.showinfo("Delete status", "Létudiant est supprimé");
        conn.close();



def update():

    if(e_idEtudiant.get()=="" or e_IdFiliereFK.get()=="" or e_nom.get()=="" or e_prenom.get()=="" or e_age.get()==""):
        MessageBox.showinfo("Update status", "Des champs sont manquants")


    else:
        conn=mysql.connector.connect(host="sql3.freemysqlhosting.net",user="sql3348311",password="SLxH2RVI6h", database="sql3348311")
        cursor = conn.cursor()
        sql="UPDATE Etudiant SET IdFiliereFK=%s WHERE idEtudiant=%s"
        val=(e_IdFiliereFK.get(),e_idEtudiant.get())
        cursor.execute(sql,val)
        conn.commit();

        e_idEtudiant.delete(0,'end')
        e_IdFiliereFK.delete(0,'end')
        e_nom.delete(0,'end')
        e_prenom.delete(0,'end')
        e_age.delete(0,'end')
        MessageBox.showinfo("Update status", "L'étudiant est modifié");
        conn.close();

def get():
  if(e_idEtudiant.get()== ""):
        MessageBox.showinfo("Fetch status", "L'id est nécessaire ")


 else:
        conn=mysql.connector.connect(host="sql3.freemysqlhosting.net",user="sql3348311",password="SLxH2RVI6h", database="sql3348311")
        cursor = conn.cursor()
        sql="SELECT * FROM Etudiant WHERE idEtudiant= %s"
        val=(e_idEtudiant.get(),)
        cursor.execute(sql,val)

        rows=cursor.fetchall()

        for row in rows:
            e_IdFiliereFK .insert(0,row[1])
            e_nom.insert(0,row[2])
            e_prenom.insert(0,row[3])
            e_age.insert(0,row[4])

        conn.close();


root = tkinter.Tk()
root.title("Menu")

idEtudiant=tkinter.Label(root,text="Entrer l'identifiant de l'étudiant :",font=("bold",10))
idEtudiant.place(x=20,y=30)

IdFiliereFK=tkinter.Label(root,text="Entrer l'identifiant de la filière :",font=("bold",10))
IdFiliereFK.place(x=20,y=60)


nom=tkinter.Label(root,text="Entrer votre nom :",font=("bold",10))
nom.place(x=20,y=90)

prenom=tkinter.Label(root,text="Entrer votre prénom:",font=("bold",10))
prenom.place(x=20,y=120)

age=tkinter.Label(root,text="Entrer votre age :",font=("bold",10))
age.place(x=20,y=150)

e_idEtudiant=tkinter.Entry()
e_idEtudiant.place(x=200,y=30)


e_IdFiliereFK=tkinter.Entry()
e_IdFiliereFK.place(x=200,y=60)

e_nom=tkinter.Entry()
e_nom.place(x=200,y=90)

e_prenom=tkinter.Entry()
e_prenom.place(x=200,y=120)

e_age=tkinter.Entry()
e_age.place(x=200,y=150)

insert=  tkinter.Button(root,text='ajouter',font=("italic",10),bg="white",command=insert)
insert.place(x=20,y=200)

delete= tkinter.Button(root,text='supprimer',font=("italic",10),bg="white",command=delete)
delete.place(x=70,y=200)


update= tkinter.Button(root,text='modifier',font=("italic",10),bg="white",command=update)
update.place(x=130,y=200)


get=tkinter.Button(root,text='afficher',font=("italic",10),bg="white",command=get)
get.place(x=190,y=200)

def faireApparaitreLeToplevel():
    Toplevel(root)

go = Button(root , text = 'Les étudiants', command=faireApparaitreLeToplevel)
go.pack()


root.mainloop()




