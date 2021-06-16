from tkinter import *
from tkinter import messagebox
from pymongo import MongoClient
from functools import partial
from bson import ObjectId

w=Tk()
w.title("Club Events")
w.wm_iconbitmap("collegeLogo.ico")
w.geometry("900x500")
w.configure(bg='yellow')
lbl = Label (w, text="Welcome to \n WCE Club Events", bg="yellow", fg="black", font="none 24 bold").grid(row=0, column=6, columnspan=2, pady=10, padx=10, ipadx=50)
connection = MongoClient()

# CREATE DATABASE
database = connection['Club']
# CREATE COLLECTION
collection = database['Club_Events']
print("Database connected")



def insert_window():
	nw=Toplevel(w)
	nw.title("Insertion")
	nw.geometry("600x500")
	nw.configure(bg='yellow')
	global e1,e2,e3,e4,e5,e6

	label=Label(nw, text="Insert Events", bg="yellow", fg="black", font="none 18 bold")
	label.grid(row=2, column=0, columnspan=2, pady=10, padx=10, ipadx=50)

	label1=Label(nw, text="Event Id:", bg="yellow", fg="black", font="none 12 bold")
	label1.grid(row=5, column=0)

	e1=Entry(nw, width=50)
	e1.grid(row=5, column=1, padx=30, pady=10)

	label2=Label(nw, text="Event Name:", bg="yellow", fg="black", font="none 12 bold")
	label2.grid(row=9, column=0)

	e2=Entry(nw, width=50)
	e2.grid(row=9, column=1, padx=30,  pady=10)

	label3=Label(nw, text="Club Name:", bg="yellow", fg="black", font="none 12 bold")
	label3.grid(row=13, column=0)

	e3=Entry(nw, width=50)
	e3.grid(row=13, column=1, padx=30,  pady=10)

	label4=Label(nw, text="Platform:", bg="yellow", fg="black", font="none 12 bold")
	label4.grid(row=17, column=0)

	e4=Entry(nw, width=50)
	e4.grid(row=17, column=1, padx=30,  pady=10)

	label5=Label(nw, text="Date:", bg="yellow", fg="black", font="none 12 bold")
	label5.grid(row=21, column=0)

	e5=Entry(nw, width=50)
	e5.grid(row=21, column=1, padx=30,  pady=10)

	label6=Label(nw, text="Time:", bg="yellow", fg="black", font="none 12 bold")
	label6.grid(row=30, column=0)

	e6=Entry(nw, width=50)
	e6.grid(row=30, column=1, padx=30,  pady=10)

	insertbtn=Button(nw, text="Insert", command=insert_data, font="none 14 bold")
	insertbtn.grid(row=35, column=0, columnspan=2, pady=10, padx=10, ipadx=50)


def insert_data():
	eid=e1.get()
	ename=e2.get()
	cname=e3.get()
	pname=e4.get()
	date=e5.get()
	time=e6.get()
	data = { "event_id": eid, "event_name": ename, "club_name": cname, "event_platform": pname, "date": date, "time": time }
	document = collection.insert_one(data)
	messagebox.showinfo("Information","Data Inserted Successfully...:)")
	return document.inserted_id

def update_window():
	nw=Toplevel(w)
	nw.title("Updation")
	nw.geometry("600x500")
	nw.configure(bg='yellow')
	global e1,e2,e3,e4,e5,e6

	label=Label(nw, text="Update Events",bg="yellow", fg="black", font="none 18 bold")
	label.grid(row=2, column=0, columnspan=2, pady=10, padx=10, ipadx=50)

	label1=Label(nw, text="Event Id", bg="yellow", fg="black", font="none 12 bold")
	label1.grid(row=4, column=0)

	e1=Entry(nw, width=50)
	e1.grid(row=4, column=1, padx=30,  pady=10)

	label2=Label(nw, text="Event Name", bg="yellow", fg="black", font="none 12 bold")
	label2.grid(row=7, column=0)

	e2=Entry(nw, width=50)
	e2.grid(row=7, column=1, padx=30,  pady=10)

	label3=Label(nw, text="Club Name", bg="yellow", fg="black", font="none 12 bold")
	label3.grid(row=10, column=0)

	e3=Entry(nw, width=50)
	e3.grid(row=10, column=1, padx=30,  pady=10)

	label4=Label(nw, text="Platform", bg="yellow", fg="black", font="none 12 bold")
	label4.grid(row=13, column=0)

	e4=Entry(nw, width=50)
	e4.grid(row=13, column=1, padx=30,  pady=10)

	label5=Label(nw, text="Date", bg="yellow", fg="black", font="none 12 bold")
	label5.grid(row=16, column=0)

	e5=Entry(nw, width=50)
	e5.grid(row=16, column=1, padx=30,  pady=10)

	label6=Label(nw, text="Time", bg="yellow", fg="black", font="none 12 bold")
	label6.grid(row=19, column=0)

	e6=Entry(nw, width=50)
	e6.grid(row=19, column=1, padx=30,  pady=10)

	insertbtn=Button(nw, text="Update", command=update_or_create, font="none 14 bold")
	insertbtn.grid(row=21, column=0, columnspan=2, pady=10, padx=10, ipadx=50)


def update_or_create():
	eid=e1.get();
	ename=e2.get()
	cname=e3.get()
	pname=e4.get()
	date=e5.get()
	time=e6.get()
	data = {"event_name": ename, "club_name": cname, "event_platform": pname, "date": date, "time": time }
	document = collection.update_one({'event_id': eid}, {"$set": data}, upsert=True)
	messagebox.showinfo("Information","Data Updated Successfully...:)")
	return document.acknowledged

def delete_window():
	nw=Toplevel(w)
	nw.title("Deletion")
	nw.geometry("600x500")
	nw.configure(bg='yellow')
	global e1,e2,e3,e4,e5,e6

	label=Label(nw, text="Delete Events", bg="yellow", fg="black", font="none 18 bold")
	label.grid(row=2, column=0, columnspan=2, pady=10, padx=10, ipadx=50)

	label1=Label(nw, text="Event Id", bg="yellow",fg="black", font="none 12 bold")
	label1.grid(row=4, column=0)

	e1=Entry(nw, width=50)
	e1.grid(row=4, column=1, padx=30,  pady=10)

	label2=Label(nw, text="Event Name", bg="yellow",fg="black", font="none 12 bold")
	label2.grid(row=7, column=0)

	e2=Entry(nw, width=50)
	e2.grid(row=7, column=1, padx=30,  pady=10)


	deletbtn=Button(nw, text="Delete", command=remove_data, font="none 14 bold")
	deletbtn.grid(row=21, column=0, columnspan=2, pady=10, padx=10, ipadx=50)

def remove_data():
    eid=e1.get();
    ename=e2.get()
    data = {"event_name": ename}
    document = collection.delete_one(data)
    messagebox.showinfo("Information","Data Deleted Successfully...:)")
    return document.acknowledged

def show_window():
	nw=Toplevel(w)
	nw.title("View")
	nw.geometry("600x500")
	nw.configure(bg='yellow')
	global e1,e2,e3,e4,e5,e6

	label=Label(nw, text="View Events", bg="yellow", fg="black", font="none 18 bold")
	label.grid(row=2, column=0, columnspan=2, pady=10, padx=10, ipadx=50)

	label1=Label(nw, text="Event Id", bg="yellow",fg="black", font="none 12 bold")
	label1.grid(row=4, column=0)

	e1=Entry(nw, width=50)
	e1.grid(row=4, column=1, padx=30,  pady=10)

	label2=Label(nw, text="Event Name", bg="yellow",fg="black", font="none 12 bold")
	label2.grid(row=7, column=0)

	e2=Entry(nw, width=50)
	e2.grid(row=7, column=1, padx=30,  pady=10)


	showbtn=Button(nw, text="View", command=get_single_data, font="none 14 bold")
	showbtn.grid(row=21, column=0, columnspan=2, pady=10, padx=10, ipadx=50)

def get_single_data():
	eid=e1.get();
	ename=e2.get()
	data = {"event_name": ename}
	data1 = collection.find_one(data)
	result=""
	arr=[]
	for arr in data1:
		result+=str(arr)+"\n"
	messagebox.showinfo("Information",data1)
	print(data1)

def delete_all():
	x=collection.delete_many({})
	s=str(x.deleted_count)+" events deleted"
	messagebox.showinfo("Information",s)

def view_all():
	for x in collection.find():
		print(x)

def get_multiple_data():
    data = collection.find()
    return list(data)


def update_existing(document_id, data):
    document = collection.update_one({'_id': ObjectId(document_id)}, {"$set": data})
    return document.acknowledged





insert=Button(w, text="Insert", command=insert_window, font="none 14 bold")
insert.grid(row=2, column=0, columnspan=2, pady=30, padx=30, ipadx=50)

insert=Button(w, text="Update", command=update_window, font="none 14 bold")
insert.grid(row=2, column=9, columnspan=2, pady=30, padx=30, ipadx=50)

insert=Button(w, text="Delete", command=delete_window, font="none 14 bold")
insert.grid(row=8, column=0, columnspan=2, pady=30, padx=30, ipadx=50)

insert=Button(w, text="Delete All", command=delete_all, font="none 14 bold")
insert.grid(row=8, column=9, columnspan=2, pady=30, padx=30, ipadx=50)

insert=Button(w, text="View", command=show_window, font="none 14 bold")
insert.grid(row=11, column=0, columnspan=2, pady=30, padx=30, ipadx=50)

insert=Button(w, text="View All", command=view_all, font="none 14 bold")
insert.grid(row=11, column=9, columnspan=2, pady=30, padx=30, ipadx=50)

w.mainloop()

