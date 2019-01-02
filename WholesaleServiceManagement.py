from builtins import print
from mysql.connector import Error
import mysql.connector
from tkinter import *
import tkinter.messagebox

try:
    conn = mysql.connector.connect(host = "localhost", user = "root", password = "root")
    print(conn)
    mycursor = conn.cursor()
    conn.commit()

except Error as error:
    print(error)

finally:
    mycursor.close()
    conn.close()


rootWindow = Tk("main")
rootWindow.configure(background = "black")
rootWindow.geometry('800x480')
rootWindow.title("WholeSale Service Management System")
#rootWindow.resizable(False)
photo = tkinter.PhotoImage(file = 'unts.png')
w = tkinter.Label(rootWindow, image = photo)
w.grid(row = 0, column = 0)

labelJust = Label(rootWindow)
labelJust.grid()

labelToLogin = Label(rootWindow, text = "Please login to continue: ", fg = "white", bg = "black", font = ("Helvetica", 20))
labelToLogin.grid(row = 2)

labelUsername = Label(rootWindow, text = "Username", fg = "white", bg = "black", font = 14)
labelUsername.grid(row = 3)

entryUsername = Entry(rootWindow)
entryUsername.grid(row = 4)

labelPassword = Label(rootWindow, text = "Password", fg = "white", bg = "black", font = 14)
labelPassword.grid(row = 5)

entryPassword = Entry(rootWindow)
entryPassword.grid(row = 6)

labelJust = Label(rootWindow, text = "", fg = "white", bg = "black")
labelJust.grid(row = 7)

loginButton = Button(rootWindow, text = "Login", fg = "green", font = 14)
loginButton.grid(row = 8)

def doHomeActivity():
    mycursor.close()
    conn.close()
    rootWindow.withdraw()

    rootHomeWindow = Tk("main")
    rootHomeWindow.configure(background="#BFBFBF")
    rootHomeWindow.title("Home Activity")

    labelJust = Label(rootHomeWindow, bg="#bfbfbf")
    labelJust.grid(row=0, column=1)
    labeltitle = Label(rootHomeWindow, bg="dark green", text = "**Services Provided**", font = ("Helvetica 16 bold italic"), fg = "light green")
    labeltitle.grid(row=1, column=1)

    labelJust = Label(rootHomeWindow, bg = "#bfbfbf")
    labelJust.grid(row=2, column = 1)
    button1 = Button(rootHomeWindow, text="Manufacturer side Imports", fg="blue", font=14)
    button1.grid(row = 3, column = 1, sticky = N+S+E+W)

    labelJust = Label(rootHomeWindow, bg = "#bfbfbf")
    labelJust.grid(row=4, column = 1)
    button2 = Button(rootHomeWindow, text="WholeSale Inventory Management", fg="blue", font=14)
    button2.grid(row=5, column=1, sticky = N+S+E+W)

    labelJust = Label(rootHomeWindow, bg = "#bfbfbf")
    labelJust.grid(row=6, column = 1)
    button3 = Button(rootHomeWindow, text="Vendor side Exports", fg="blue", font=14)
    button3.grid(row=7, column=1, sticky = N+S+E+W)

    labelJust = Label(rootHomeWindow, bg = "#bfbfbf")
    labelJust.grid(row=8, column = 1)
    button4 = Button(rootHomeWindow, text="Parent Database", fg="blue", font=14)
    button4.grid(row=9, column=1, sticky = N+S+E+W)

    labelJust = Label(rootHomeWindow, bg="#bfbfbf")
    labelJust.grid(row=10, column=1)
    button5 = Button(rootHomeWindow, text="SET/RESET", fg="red", font=12)
    button5.grid(row=11, column=1)

    labelJust = Label(rootHomeWindow, bg="#bfbfbf")
    labelJust.grid(row=12, column=1)

    def doManufacturer(event):
        rootHomeWindow.withdraw()
        rootManufacturerActivityWindow = Tk("main")
        rootManufacturerActivityWindow.configure(background="#BFBFBF")
        rootManufacturerActivityWindow.title("Manufacturer Activity")

        labelJust = Label(rootManufacturerActivityWindow, bg="#bfbfbf")
        labelJust.grid(row=0, column=1)
        labeltitle = Label(rootManufacturerActivityWindow, bg="dark green", text="**Manufacturer Services**", font=("Helvetica 16 bold italic"), fg="light green")
        labeltitle.grid(row=1, column=1)

        labelJust = Label(rootManufacturerActivityWindow, bg="#bfbfbf")
        labelJust.grid(row=2, column=1)
        button1 = Button(rootManufacturerActivityWindow, text="Manufacturer Inventory Management", fg="blue", font=14)
        button1.grid(row=3, column=1, sticky=N + S + E + W)

        labelJust = Label(rootManufacturerActivityWindow, bg="#bfbfbf")
        labelJust.grid(row=4, column=1)
        button2 = Button(rootManufacturerActivityWindow, text="Manufacturer Monetary Transaction", fg="blue", font=14)
        button2.grid(row=5, column=1, sticky=N + S + E + W)

        labelJust = Label(rootManufacturerActivityWindow, bg="#bfbfbf")
        labelJust.grid(row=6, column=1)

        def doManufacturerInventoryManagement(event):
            rootManufacturerActivityWindow.withdraw()
            rootManufacturerInventoryManagementWindow = Tk("main")
            rootManufacturerInventoryManagementWindow.geometry('520x500')
            rootManufacturerInventoryManagementWindow.title("Manufacture Inventory Management")

            label1 = Label(rootManufacturerInventoryManagementWindow, text="Inventory ID*")
            label2 = Label(rootManufacturerInventoryManagementWindow, text="Manufacture ID")
            label3 = Label(rootManufacturerInventoryManagementWindow, text="Per Inventory Cost")
            label4 = Label(rootManufacturerInventoryManagementWindow, text="Inventory Qty")

            entry1 = Entry(rootManufacturerInventoryManagementWindow)
            entry2 = Entry(rootManufacturerInventoryManagementWindow)
            entry3 = Entry(rootManufacturerInventoryManagementWindow)
            entry4 = Entry(rootManufacturerInventoryManagementWindow)

            label1.grid(row=1, column=0, sticky=E)
            label2.grid(row=2, column=0, sticky=E)
            label3.grid(row=3, column=0, sticky=E)
            label4.grid(row=4, column=0, sticky=E)

            entry1.grid(row=1, column=1)
            entry2.grid(row=2, column=1)
            entry3.grid(row=3, column=1)
            entry4.grid(row=4, column=1)

            insertButton = Button(rootManufacturerInventoryManagementWindow, text="INSERT", fg="green")
            insertButton.grid(row=2, column=2, sticky=W)

            dotlabel1 = Label(rootManufacturerInventoryManagementWindow, text=".......................................................", fg="blue")
            dotlabel1.grid(row=6, column=0)
            dotlabel2 = Label(rootManufacturerInventoryManagementWindow, text=".......................................................", fg="blue")
            dotlabel2.grid(row=6, column=1)
            dotlabel3 = Label(rootManufacturerInventoryManagementWindow, text="........................................", fg="blue")
            dotlabel3.grid(row=6, column=2)

            label5 = Label(rootManufacturerInventoryManagementWindow, text="Inventory ID*")
            label6 = Label(rootManufacturerInventoryManagementWindow, text="Inventory Qty")
            label7 = Label(rootManufacturerInventoryManagementWindow, text="Per Inventory Cost")


            entry5 = Entry(rootManufacturerInventoryManagementWindow)
            entry6 = Entry(rootManufacturerInventoryManagementWindow)
            entry7 = Entry(rootManufacturerInventoryManagementWindow)

            label5.grid(row=7, column=0, sticky=E)
            label6.grid(row=8, column=0, sticky=E)
            label7.grid(row=9, column=0, sticky=E)

            entry5.grid(row=7, column=1)
            entry6.grid(row=8, column=1)
            entry7.grid(row=9, column=1)

            updateButton = Button(rootManufacturerInventoryManagementWindow, text="UPDATE", fg="green")
            updateButton.grid(row=8, column=2, sticky=W)


            dotlabel1 = Label(rootManufacturerInventoryManagementWindow,
                              text=".......................................................", fg="blue")
            dotlabel1.grid(row=10, column=0)
            dotlabel2 = Label(rootManufacturerInventoryManagementWindow,
                              text=".......................................................", fg="blue")
            dotlabel2.grid(row=10, column=1)
            dotlabel3 = Label(rootManufacturerInventoryManagementWindow,
                              text="........................................", fg="blue")
            dotlabel3.grid(row=10, column=2)

            label8 = Label(rootManufacturerInventoryManagementWindow, text="Inventory ID")
            labelOr = Label(rootManufacturerInventoryManagementWindow, text="OR")
            label9 = Label(rootManufacturerInventoryManagementWindow, text="Manufacturer ID")

            entry8 = Entry(rootManufacturerInventoryManagementWindow)
            entry9 = Entry(rootManufacturerInventoryManagementWindow)

            label8.grid(row=11, column=0, sticky=E)
            labelOr.grid(row=12, column=1)
            label9.grid(row=13, column=0, sticky=E)

            entry8.grid(row=11, column=1)
            entry9.grid(row=13, column=1)

            searchButton = Button(rootManufacturerInventoryManagementWindow, text="SEARCH", fg="green")
            searchButton.grid(row=12, column=2, sticky=W)

            dotlabel1 = Label(rootManufacturerInventoryManagementWindow,
                              text=".......................................................", fg="blue")
            dotlabel1.grid(row=14, column=0)
            dotlabel2 = Label(rootManufacturerInventoryManagementWindow,
                              text=".......................................................", fg="blue")
            dotlabel2.grid(row=14, column=1)
            dotlabel3 = Label(rootManufacturerInventoryManagementWindow,
                              text="........................................", fg="blue")
            dotlabel3.grid(row=14, column=2)

            label10 = Label(rootManufacturerInventoryManagementWindow, text="Inventory ID")
            entry10 = Entry(rootManufacturerInventoryManagementWindow)

            label10.grid(row=15, column=0, sticky=E)
            entry10.grid(row=15, column=1)

            deleteButton = Button(rootManufacturerInventoryManagementWindow, text="DELETE", fg="green")
            deleteButton.grid(row=15, column=2, sticky=W)

            dotlabel1 = Label(rootManufacturerInventoryManagementWindow,
                              text=".......................................................", fg="blue")
            dotlabel1.grid(row=16, column=0)
            dotlabel2 = Label(rootManufacturerInventoryManagementWindow,
                              text=".......................................................", fg="blue")
            dotlabel2.grid(row=16, column=1)
            dotlabel3 = Label(rootManufacturerInventoryManagementWindow,
                              text="........................................", fg="blue")
            dotlabel3.grid(row=16, column=2)

            list1 = Listbox(rootManufacturerInventoryManagementWindow, height=6, width=80)
            list1.grid(row=17, column=0, columnspan=4)

            sb1 = Scrollbar(rootManufacturerInventoryManagementWindow)
            sb1.grid(row=17, column=4, rowspan=6)

            list1.configure(yscrollcommand=sb1.set)
            sb1.configure(command=list1.yview())

            dotlabel1 = Label(rootManufacturerInventoryManagementWindow,
                              text=".......................................................", fg="blue")
            dotlabel1.grid(row=18, column=0)
            dotlabel2 = Label(rootManufacturerInventoryManagementWindow,
                              text=".......................................................", fg="blue")
            dotlabel2.grid(row=18, column=1)
            dotlabel3 = Label(rootManufacturerInventoryManagementWindow,
                              text="........................................", fg="blue")
            dotlabel3.grid(row=18, column=2)

            setresetButton = Button(rootManufacturerInventoryManagementWindow, text="SET/RESET DB", fg="red")
            setresetButton.grid(row=19, column=1)

            def insert(event):
                try:
                    conn = mysql.connector.connect(host="localhost", user="root", password="root", db="WholeSale_Services")
                    print(conn)
                    mycursor = conn.cursor()
                    query = 'insert into Manufacture_side_inventory_import_management(Inv_id, Manf_id, Per_inv_cost, Inv_qty) values(%s,%s,%s,%s);'
                    ip = (entry1.get(), entry2.get(), int(entry3.get()), int(entry4.get()))
                    mycursor.execute(query, ip)
                    conn.commit()
                    tkinter.messagebox.showinfo("", "Inserted Successfully")

                except Error as error:
                    print(error)

                finally:
                    mycursor.close()
                    conn.close()

            def update(event):
                conn = mysql.connector.connect(host="localhost", user="root", password="root", db="WholeSale_Services")
                print(conn)
                mycursor = conn.cursor()

                i5_id = entry5.get()
                i6_cost = entry6.get()
                i7_qty = entry7.get()

                try:
                    if (i6_cost != "" and i7_qty == ""):
                        query = 'update Manufacture_side_inventory_import_management set Per_inv_cost = %s where Inv_id = %s;'
                        ip = (int(i6_cost), i5_id)
                        mycursor.execute(query, ip)
                        conn.commit()
                        tkinter.messagebox.showinfo("", "Updated Successfully")

                    elif (i6_cost == "" and i7_qty != ""):
                        query = 'update Manufacture_side_inventory_import_management set Inv_qty = %s where Inv_id = %s;'
                        ip = (int(i7_qty), i5_id)
                        mycursor.execute(query, ip)
                        conn.commit()
                        tkinter.messagebox.showinfo("", "Updated Successfully")

                    elif (i6_cost != "" and i7_qty != ""):
                        query = 'update Manufacture_side_inventory_import_management set Per_inv_cost = %s, Inv_qty = %s where Inv_id = %s;'
                        ip = (int(i6_cost), int(i7_qty), i5_id)
                        mycursor.execute(query, ip)
                        conn.commit()
                        tkinter.messagebox.showinfo("", "Updated Successfully")

                    else:
                        tkinter.messagebox.showinfo("", "Nothing Updated")

                except Error as error:
                    print(error)

                finally:
                    mycursor.close()
                    conn.close()

            def delete(event):
                try:
                    conn = mysql.connector.connect(host="localhost", user="root", password="root",  db="WholeSale_Services")
                    print(conn)
                    mycursor = conn.cursor()
                    lastid = entry10.get()
                    query = 'delete from Manufacture_side_inventory_import_management where Inv_id = %s;'
                    ip = (lastid)
                    mycursor.execute(query, (ip, ))
                    conn.commit()
                    tkinter.messagebox.showinfo("", "Deleted Successfully")

                except Error as error:
                    print(error)

                finally:
                    mycursor.close()
                    conn.close()

            def search(event):
                list1.delete(0, 'end')
                try:
                    conn = mysql.connector.connect(host="localhost", user="root", password="root", db="WholeSale_Services")
                    print(conn)
                    mycursor = conn.cursor()

                    if (entry8.get() != "" and entry9.get() != ""):
                        doToastMessage("Please enter only in either of the fields")
                        return

                    elif(entry8.get() != "" and entry9.get() == ""):
                        lastid = entry8.get()
                        query = 'select Inventory_superset.*, Manufacture_side_inventory_import_management.Per_inv_cost, Manufacture_side_inventory_import_management.Inv_qty, Manufacture_side_inventory_import_management.Tot_inv_cost, Manufacturer_superset.* from Inventory_superset inner join Manufacture_side_inventory_import_management on Inventory_superset.Inv_id = %s and Manufacture_side_inventory_import_management.Inv_id = %s inner join Manufacturer_superset on Manufacture_side_inventory_import_management.Manf_id = (select Manf_id from Manufacture_side_inventory_import_management where Inv_id = %s) and Manufacturer_superset.Manf_id = (select Manf_id from Manufacture_side_inventory_import_management where Inv_id = %s);'
                        ip = (lastid, lastid, lastid, lastid)
                        mycursor.execute(query, ip)
                        records = mycursor.fetchall()
                        for record in records:
                            print(record)
                            arg = '  Inv_id:- ' + str(record[0]) + '  Inv_name:- ' + str(record[1]) + '  Description:- ' + str(record[2]) + '  Per_inv_cost:- ' + str(record[3]) + '  Inv_qty:- ' + str(record[4]) + '  Tot_inv_cost:- ' + str(record[5]) + '  Manf_id:- ' + str(record[6]) + '  Manf_name:- ' + str(record[7]) + '  Addr:- ' + str(record[8]) + '  City:- ' + str(record[9]) + '  Cont:- ' + str(record[10])
                            list1.insert(END, arg)
                        conn.commit()

                    elif(entry8.get() == "" and entry9.get() != ""):
                        lastid = entry9.get()
                        query = 'select Manufacturer_superset.*, Manufacture_side_inventory_import_management.Inv_id, Manufacture_side_inventory_import_management.Per_inv_cost, Manufacture_side_inventory_import_management.Inv_qty, Manufacture_side_inventory_import_management.Tot_inv_cost from Manufacturer_superset inner join Manufacture_side_inventory_import_management on Manufacturer_superset.Manf_id = %s and Manufacture_side_inventory_import_management.Manf_id = %s;'
                        ip = (lastid, lastid)
                        mycursor.execute(query, ip)
                        records = mycursor.fetchall()
                        for record in records:
                            print(record)
                            arg = '  Manf_id:- ' + str(record[0]) + '  Manf_name:- ' + str(record[1]) + '  Addr:- ' + str(record[2]) + '  City:- ' + str(record[3]) + '  Cont:- ' + str(record[4]) + '  Inv_id:- ' + str(record[5]) + '  Per_inv_cost:- ' + str(record[6]) + '  Inv_qty:- ' + str(record[7]) + '  Tot_inv_cost:- ' + str(record[8])
                            list1.insert(END, arg)
                        conn.commit()

                    else:
                        list1.delete(0, 'end')
                        try:
                            conn = mysql.connector.connect(host="localhost", user="root", password="root", db="WholeSale_Services")
                            print(conn)
                            mycursor = conn.cursor()

                            query = 'SELECT Inv_id, Manf_id FROM manufacture_side_inventory_import_management;'
                            mycursor.execute(query)
                            records = mycursor.fetchall()
                            for record in records:
                                print(record)
                                arg = '  Inv_id:- ' + str(record[0]) + '  Manf_id:- ' + str(record[1])
                                list1.insert(END, arg)
                                conn.commit()

                                # tkinter.messagebox.showinfo("", "Records Searched if exists")

                        except Error as error:
                            print(error)

                        finally:
                            mycursor.close()
                            conn.close()

                        doToastMessage("Please enter only in either of the fields")
                        return

                    tkinter.messagebox.showinfo("", "Records Searched if exists")

                except Error as error:
                    print(error)

                finally:
                    mycursor.close()
                    conn.close()

            def setreset(event):
                ans = tkinter.messagebox.askquestion("", "This will SET/RESET the Manufacture_side_inventory_import_management System!! Proceed with Caution...")
                if ans == "yes":
                    try:
                        conn = mysql.connector.connect(host="localhost", user="root", password="root", db="WholeSale_Services")
                        print(conn)
                        mycursor = conn.cursor()
                        mycursor.execute('truncate table Manufacture_side_inventory_import_management;')
                        tkinter.messagebox.showinfo("", "Manufacture_side_inventory_import_management System Successfully SET/RESET")

                    except Error as error:
                        print(error)

                    finally:
                        mycursor.close()
                        conn.close()

            def doClose_rootManufacturerInventoryManagementWindow():
                rootManufacturerInventoryManagementWindow.destroy()
                rootManufacturerActivityWindow.update()
                rootManufacturerActivityWindow.deiconify()

            insertButton.bind("<Button-1>", insert)
            updateButton.bind("<Button-1>", update)
            deleteButton.bind("<Button-1>", delete)
            searchButton.bind("<Button-1>", search)
            setresetButton.bind("<Button-1>", setreset)
            rootManufacturerInventoryManagementWindow.protocol("WM_DELETE_WINDOW", doClose_rootManufacturerInventoryManagementWindow)

        def doManufacturerMonetaryTransaction(event):
            rootManufacturerActivityWindow.withdraw()
            rootManufacturerMonetaryTransactionWindow = Tk("main")
            rootManufacturerMonetaryTransactionWindow.geometry('520x400')
            rootManufacturerMonetaryTransactionWindow.title("Manufacture Monetary Transaction")

            label1 = Label(rootManufacturerMonetaryTransactionWindow, text="Manufacturer ID*")
            label2 = Label(rootManufacturerMonetaryTransactionWindow, text="Paid Amount")

            entry1 = Entry(rootManufacturerMonetaryTransactionWindow)
            entry2 = Entry(rootManufacturerMonetaryTransactionWindow)

            label1.grid(row=1, column=0, sticky=E)
            label2.grid(row=2, column=0, sticky=E)

            entry1.grid(row=1, column=1)
            entry2.grid(row=2, column=1)

            insertButton = Button(rootManufacturerMonetaryTransactionWindow, text="INSERT", fg="green")
            insertButton.grid(row=2, column=2, sticky=W)

            dotlabel1 = Label(rootManufacturerMonetaryTransactionWindow,
                              text=".......................................................", fg="blue")
            dotlabel1.grid(row=3, column=0)
            dotlabel2 = Label(rootManufacturerMonetaryTransactionWindow,
                              text=".......................................................", fg="blue")
            dotlabel2.grid(row=3, column=1)
            dotlabel3 = Label(rootManufacturerMonetaryTransactionWindow,
                              text="........................................", fg="blue")
            dotlabel3.grid(row=3, column=2)

            label3 = Label(rootManufacturerMonetaryTransactionWindow, text="Transaction No.")
            label4 = Label(rootManufacturerMonetaryTransactionWindow, text="Paid Amount")
            label5 = Label(rootManufacturerMonetaryTransactionWindow, text="Date")

            entry3 = Entry(rootManufacturerMonetaryTransactionWindow)
            entry4 = Entry(rootManufacturerMonetaryTransactionWindow)
            entry5 = Entry(rootManufacturerMonetaryTransactionWindow)

            label3.grid(row=4, column=0, sticky=E)
            label4.grid(row=5, column=0, sticky=E)
            label5.grid(row=6, column=0, sticky=E)

            entry3.grid(row=4, column=1)
            entry4.grid(row=5, column=1)
            entry5.grid(row=6, column=1)

            updateButton = Button(rootManufacturerMonetaryTransactionWindow, text="UPDATE", fg="green")
            updateButton.grid(row=5, column=2, sticky=W)

            dotlabel1 = Label(rootManufacturerMonetaryTransactionWindow,
                              text=".......................................................", fg="blue")
            dotlabel1.grid(row=7, column=0)
            dotlabel2 = Label(rootManufacturerMonetaryTransactionWindow,
                              text=".......................................................", fg="blue")
            dotlabel2.grid(row=7, column=1)
            dotlabel3 = Label(rootManufacturerMonetaryTransactionWindow,
                              text="........................................", fg="blue")
            dotlabel3.grid(row=7, column=2)

            label6 = Label(rootManufacturerMonetaryTransactionWindow, text="Manufacturer ID")
            entry6 = Entry(rootManufacturerMonetaryTransactionWindow)

            label6.grid(row=8, column=0, sticky=E)
            entry6.grid(row=8, column=1)

            searchButton = Button(rootManufacturerMonetaryTransactionWindow, text="SEARCH", fg="green")
            searchButton.grid(row=8, column=2, sticky=W)

            dotlabel1 = Label(rootManufacturerMonetaryTransactionWindow,
                              text=".......................................................", fg="blue")
            dotlabel1.grid(row=9, column=0)
            dotlabel2 = Label(rootManufacturerMonetaryTransactionWindow,
                              text=".......................................................", fg="blue")
            dotlabel2.grid(row=9, column=1)
            dotlabel3 = Label(rootManufacturerMonetaryTransactionWindow,
                              text="........................................", fg="blue")
            dotlabel3.grid(row=9, column=2)

            label7 = Label(rootManufacturerMonetaryTransactionWindow, text="Transaction No.")
            entry7 = Entry(rootManufacturerMonetaryTransactionWindow)

            label7.grid(row=10, column=0, sticky=E)
            entry7.grid(row=10, column=1)

            deleteButton = Button(rootManufacturerMonetaryTransactionWindow, text="DELETE", fg="green")
            deleteButton.grid(row=10, column=2, sticky=W)

            dotlabel1 = Label(rootManufacturerMonetaryTransactionWindow,
                              text=".......................................................", fg="blue")
            dotlabel1.grid(row=11, column=0)
            dotlabel2 = Label(rootManufacturerMonetaryTransactionWindow,
                              text=".......................................................", fg="blue")
            dotlabel2.grid(row=11, column=1)
            dotlabel3 = Label(rootManufacturerMonetaryTransactionWindow,
                              text="........................................", fg="blue")
            dotlabel3.grid(row=11, column=2)

            list1 = Listbox(rootManufacturerMonetaryTransactionWindow, height=6, width=80)
            list1.grid(row=12, column=0, columnspan=4)

            sb1 = Scrollbar(rootManufacturerMonetaryTransactionWindow)
            sb1.grid(row=12, column=4, rowspan=6)

            list1.configure(yscrollcommand=sb1.set)
            sb1.configure(command=list1.yview())

            dotlabel1 = Label(rootManufacturerMonetaryTransactionWindow,
                              text=".......................................................", fg="blue")
            dotlabel1.grid(row=13, column=0)
            dotlabel2 = Label(rootManufacturerMonetaryTransactionWindow,
                              text=".......................................................", fg="blue")
            dotlabel2.grid(row=13, column=1)
            dotlabel3 = Label(rootManufacturerMonetaryTransactionWindow,
                              text="........................................", fg="blue")
            dotlabel3.grid(row=13, column=2)

            setresetButton = Button(rootManufacturerMonetaryTransactionWindow, text="SET/RESET DB", fg="red")
            setresetButton.grid(row=14, column=1)

            def insert(event):
                try:
                    conn = mysql.connector.connect(host="localhost", user="root", password="root", db="WholeSale_Services")
                    print(conn)
                    mycursor = conn.cursor()
                    query = 'insert into Manufacture_side_monetary_transaction(Manf_id, PaidAmt, Occasion) values(%s,%s,sysdate());'
                    ip = (entry1.get(), int(entry2.get()))
                    mycursor.execute(query, ip)
                    conn.commit()
                    tkinter.messagebox.showinfo("", "Inserted Successfully")

                except Error as error:
                    print(error)

                finally:
                    mycursor.close()
                    conn.close()

            def update(event):
                conn = mysql.connector.connect(host="localhost", user="root", password="root", db="WholeSale_Services")
                print(conn)
                mycursor = conn.cursor()

                i3_Tnno = entry3.get()
                i4_paidAmt = entry4.get()
                i5_date = entry5.get()

                try:
                    if (i4_paidAmt != "" and i5_date == ""):
                        query = 'update Manufacture_side_monetary_transaction set PaidAmt = %s where Tn_no = %s;'
                        ip = (int(i4_paidAmt), int(i3_Tnno))
                        mycursor.execute(query, ip)
                        conn.commit()
                        tkinter.messagebox.showinfo("", "Updated Successfully")

                    elif (i4_paidAmt == "" and i5_date != ""):
                        query = 'update Manufacture_side_monetary_transaction set Occasion = %s where Tn_no = %s;'
                        ip = (i5_date, int(i3_Tnno))
                        mycursor.execute(query, ip)
                        conn.commit()
                        tkinter.messagebox.showinfo("", "Updated Successfully")

                    elif (i4_paidAmt != "" and i5_date != ""):
                        query = 'update Manufacture_side_monetary_transaction set PaidAmt = %s, Occasion = %s where Tn_no = %s;'
                        ip = (int(i4_paidAmt), i5_date, int(i3_Tnno))
                        mycursor.execute(query, ip)
                        conn.commit()
                        tkinter.messagebox.showinfo("", "Updated Successfully")

                    else:
                        tkinter.messagebox.showinfo("", "Nothing Updated")

                except Error as error:
                    print(error)

                finally:
                    mycursor.close()
                    conn.close()

            def delete(event):
                try:
                    conn = mysql.connector.connect(host="localhost", user="root", password="root",  db="WholeSale_Services")
                    print(conn)
                    mycursor = conn.cursor()
                    lastid = entry7.get()
                    query = 'delete from Manufacture_side_monetary_transaction where Tn_no = %s;'
                    ip = (lastid)
                    mycursor.execute(query, (ip, ))
                    conn.commit()
                    tkinter.messagebox.showinfo("", "Deleted Successfully")

                except Error as error:
                    print(error)

                finally:
                    mycursor.close()
                    conn.close()

            def search(event):
                list1.delete(0, 'end')
                try:
                    conn = mysql.connector.connect(host="localhost", user="root", password="root", db="WholeSale_Services")
                    print(conn)
                    mycursor = conn.cursor()

                    if (entry6.get() == ""):
                        list1.delete(0, 'end')
                        try:
                            conn = mysql.connector.connect(host="localhost", user="root", password="root", db="WholeSale_Services")
                            print(conn)
                            mycursor = conn.cursor()

                            query = 'SELECT Manf_id FROM manufacture_side_monetary_transaction;'
                            mycursor.execute(query)
                            records = mycursor.fetchall()
                            for record in records:
                                print(record)
                                arg = '  Manf_id:- ' + str(record[0])
                                list1.insert(END, arg)
                                conn.commit()

                                # tkinter.messagebox.showinfo("", "Records Searched if exists")

                        except Error as error:
                            print(error)

                        finally:
                            mycursor.close()
                            conn.close()

                        doToastMessage("Please enter Manf_id")
                        return

                    else:
                        lastid = entry6.get()
                        query = 'select Manufacture_side_monetary_transaction.*, Manufacturer_superset.Manf_name, Manufacturer_superset.Addr, Manufacturer_superset.City, Manufacturer_superset.Cont from Manufacturer_superset inner join Manufacture_side_monetary_transaction on Manufacturer_superset.Manf_id = %s and Manufacture_side_monetary_transaction.Manf_id = %s;'
                        ip = (lastid, lastid)
                        mycursor.execute(query, ip)
                        records = mycursor.fetchall()
                        for record in records:
                            print(record)
                            arg = '  Tn_no:- ' + str(record[0]) + '  Manf_id:- ' + str(record[1]) + '  Paid_amt:- ' + str(record[2]) + '  Occasion:- ' + str(record[3]) + '  Manf_name:- ' + str(record[4]) + '  Addr:- ' + str(record[5]) + '  City:- ' + str(record[6]) + '  Cont:- ' + str(record[7])
                            list1.insert(END, arg)
                        conn.commit()

                    tkinter.messagebox.showinfo("", "Records Searched if exists")

                except Error as error:
                    print(error)

                finally:
                    mycursor.close()
                    conn.close()

            def setreset(event):
                ans = tkinter.messagebox.askquestion("", "This will SET/RESET the Manufacture_side_monetary_transaction System!! Proceed with Caution...")
                if ans == "yes":
                    try:
                        conn = mysql.connector.connect(host="localhost", user="root", password="root", db="WholeSale_Services")
                        print(conn)
                        mycursor = conn.cursor()
                        mycursor.execute('truncate table Manufacture_side_monetary_transaction;')
                        tkinter.messagebox.showinfo("", "Manufacture_side_monetary_transaction System Successfully SET/RESET")

                    except Error as error:
                        print(error)

                    finally:
                        mycursor.close()
                        conn.close()

            def doClose_rootManufacturerMonetaryTransactionWindow():
                rootManufacturerMonetaryTransactionWindow.destroy()
                rootManufacturerActivityWindow.update()
                rootManufacturerActivityWindow.deiconify()

            insertButton.bind("<Button-1>", insert)
            updateButton.bind("<Button-1>", update)
            deleteButton.bind("<Button-1>", delete)
            searchButton.bind("<Button-1>", search)
            setresetButton.bind("<Button-1>", setreset)
            rootManufacturerMonetaryTransactionWindow.protocol("WM_DELETE_WINDOW", doClose_rootManufacturerMonetaryTransactionWindow)


        def doClose_rootManufacturerActivityWindow():
            rootManufacturerActivityWindow.destroy()
            rootHomeWindow.update()
            rootHomeWindow.deiconify()

        rootManufacturerActivityWindow.protocol("WM_DELETE_WINDOW", doClose_rootManufacturerActivityWindow)

        button1.bind("<Button-1>", doManufacturerInventoryManagement)
        button2.bind("<Button-1>", doManufacturerMonetaryTransaction)

        rootManufacturerActivityWindow.mainloop()

    def doWholesale(event):
        rootHomeWindow.withdraw()
        rootWholesaleActivityWindow = Tk("main")
        rootWholesaleActivityWindow.geometry('520x480')
        rootWholesaleActivityWindow.title("Wholesale Activity")

        label1 = Label(rootWholesaleActivityWindow, text="Inventory ID*")
        label2 = Label(rootWholesaleActivityWindow, text="Per Inventory Cost")
        label3 = Label(rootWholesaleActivityWindow, text="Inventory Qty")
        label4 = Label(rootWholesaleActivityWindow, text="Store Section")

        entry1 = Entry(rootWholesaleActivityWindow)
        entry2 = Entry(rootWholesaleActivityWindow)
        entry3 = Entry(rootWholesaleActivityWindow)
        entry4 = Entry(rootWholesaleActivityWindow)

        label1.grid(row=1, column=0, sticky=E)
        label2.grid(row=2, column=0, sticky=E)
        label3.grid(row=3, column=0, sticky=E)
        label4.grid(row=4, column=0, sticky=E)

        entry1.grid(row=1, column=1)
        entry2.grid(row=2, column=1)
        entry3.grid(row=3, column=1)
        entry4.grid(row=4, column=1)

        insertButton = Button(rootWholesaleActivityWindow, text="INSERT", fg="green")
        insertButton.grid(row=2, column=2, sticky=W)

        dotlabel1 = Label(rootWholesaleActivityWindow,
                          text=".......................................................", fg="blue")
        dotlabel1.grid(row=5, column=0)
        dotlabel2 = Label(rootWholesaleActivityWindow,
                          text=".......................................................", fg="blue")
        dotlabel2.grid(row=5, column=1)
        dotlabel3 = Label(rootWholesaleActivityWindow,
                          text="........................................", fg="blue")
        dotlabel3.grid(row=5, column=2)

        label5 = Label(rootWholesaleActivityWindow, text="Inventory ID*")
        label6 = Label(rootWholesaleActivityWindow, text="Per Inventory Cost")
        label7 = Label(rootWholesaleActivityWindow, text="Inventory Qty")
        label8 = Label(rootWholesaleActivityWindow, text="Store Section")

        entry5 = Entry(rootWholesaleActivityWindow)
        entry6 = Entry(rootWholesaleActivityWindow)
        entry7 = Entry(rootWholesaleActivityWindow)
        entry8 = Entry(rootWholesaleActivityWindow)

        label5.grid(row=6, column=0, sticky=E)
        label6.grid(row=7, column=0, sticky=E)
        label7.grid(row=8, column=0, sticky=E)
        label8.grid(row=9, column=0, sticky=E)

        entry5.grid(row=6, column=1)
        entry6.grid(row=7, column=1)
        entry7.grid(row=8, column=1)
        entry8.grid(row=9, column=1)

        updateButton = Button(rootWholesaleActivityWindow, text="UPDATE", fg="green")
        updateButton.grid(row=7, column=2, sticky=W)

        dotlabel1 = Label(rootWholesaleActivityWindow,
                          text=".......................................................", fg="blue")
        dotlabel1.grid(row=10, column=0)
        dotlabel2 = Label(rootWholesaleActivityWindow,
                          text=".......................................................", fg="blue")
        dotlabel2.grid(row=10, column=1)
        dotlabel3 = Label(rootWholesaleActivityWindow,
                          text="........................................", fg="blue")
        dotlabel3.grid(row=10, column=2)

        label9 = Label(rootWholesaleActivityWindow, text="Inventory ID")
        entry9 = Entry(rootWholesaleActivityWindow)

        label9.grid(row=11, column=0, sticky=E)
        entry9.grid(row=11, column=1)

        searchButton = Button(rootWholesaleActivityWindow, text="SEARCH", fg="green")
        searchButton.grid(row=11, column=2, sticky=W)

        dotlabel1 = Label(rootWholesaleActivityWindow,
                          text=".......................................................", fg="blue")
        dotlabel1.grid(row=12, column=0)
        dotlabel2 = Label(rootWholesaleActivityWindow,
                          text=".......................................................", fg="blue")
        dotlabel2.grid(row=12, column=1)
        dotlabel3 = Label(rootWholesaleActivityWindow,
                          text="........................................", fg="blue")
        dotlabel3.grid(row=12, column=2)

        label10 = Label(rootWholesaleActivityWindow, text="Inventory ID")
        entry10 = Entry(rootWholesaleActivityWindow)

        label10.grid(row=13, column=0, sticky=E)
        entry10.grid(row=13, column=1)

        deleteButton = Button(rootWholesaleActivityWindow, text="DELETE", fg="green")
        deleteButton.grid(row=13, column=2, sticky=W)

        dotlabel1 = Label(rootWholesaleActivityWindow,
                          text=".......................................................", fg="blue")
        dotlabel1.grid(row=14, column=0)
        dotlabel2 = Label(rootWholesaleActivityWindow,
                          text=".......................................................", fg="blue")
        dotlabel2.grid(row=14, column=1)
        dotlabel3 = Label(rootWholesaleActivityWindow,
                          text="........................................", fg="blue")
        dotlabel3.grid(row=14, column=2)

        list1 = Listbox(rootWholesaleActivityWindow, height=6, width=80)
        list1.grid(row=15, column=0, columnspan=4)

        sb1 = Scrollbar(rootWholesaleActivityWindow)
        sb1.grid(row=15, column=4, rowspan=6)

        list1.configure(yscrollcommand=sb1.set)
        sb1.configure(command=list1.yview())

        dotlabel1 = Label(rootWholesaleActivityWindow,
                          text=".......................................................", fg="blue")
        dotlabel1.grid(row=16, column=0)
        dotlabel2 = Label(rootWholesaleActivityWindow,
                          text=".......................................................", fg="blue")
        dotlabel2.grid(row=16, column=1)
        dotlabel3 = Label(rootWholesaleActivityWindow,
                          text="........................................", fg="blue")
        dotlabel3.grid(row=16, column=2)

        setresetButton = Button(rootWholesaleActivityWindow, text="SET/RESET DB", fg="red")
        setresetButton.grid(row=17, column=1)

        def insert(event):
            try:
                conn = mysql.connector.connect(host="localhost", user="root", password="root", db="WholeSale_Services")
                print(conn)
                mycursor = conn.cursor()
                query = 'insert into Wholesale_station(Inv_id, Per_inv_cost, Inv_qty, Store_sec) values(%s,%s,%s,%s);'
                ip = (entry1.get(), int(entry2.get()), int(entry3.get()), entry4.get())
                mycursor.execute(query, ip)
                conn.commit()
                tkinter.messagebox.showinfo("", "Inserted Successfully")

            except Error as error:
                print(error)

            finally:
                mycursor.close()
                conn.close()

        def update(event):
            conn = mysql.connector.connect(host="localhost", user="root", password="root", db="WholeSale_Services")
            print(conn)
            mycursor = conn.cursor()

            i5_id = entry5.get()
            i6_cost = entry6.get()
            i7_qty = entry7.get()
            i8_stsec = entry8.get()

            try:
                if (i6_cost != "" and i7_qty == "" and i8_stsec == ""):
                    query = 'update Wholesale_station set Per_inv_cost = %s where Inv_id = %s;'
                    ip = (int(i6_cost), i5_id)
                    mycursor.execute(query, ip)
                    conn.commit()
                    tkinter.messagebox.showinfo("", "Updated Successfully")

                elif (i6_cost == "" and i7_qty != "" and i8_stsec == ""):
                    query = 'update Wholesale_station set Inv_qty = %s where Inv_id = %s;'
                    ip = (int(i7_qty), i5_id)
                    mycursor.execute(query, ip)
                    conn.commit()
                    tkinter.messagebox.showinfo("", "Updated Successfully")

                elif (i6_cost == "" and i7_qty == "" and i8_stsec != ""):
                    query = 'update Wholesale_station set Store_sec = %s where Inv_id = %s;'
                    ip = (i8_stsec, i5_id)
                    mycursor.execute(query, ip)
                    conn.commit()
                    tkinter.messagebox.showinfo("", "Updated Successfully")

                elif (i6_cost != "" and i7_qty != "" and i8_stsec == ""):
                    query = 'update Wholesale_station set Inv_qty = %s, Per_inv_cost = %s where Inv_id = %s;'
                    ip = (int(i7_qty), int(i6_cost), i5_id)
                    mycursor.execute(query, ip)
                    conn.commit()
                    tkinter.messagebox.showinfo("", "Updated Successfully")

                elif (i6_cost == "" and i7_qty != "" and i8_stsec != ""):
                    query = 'update Wholesale_station set Inv_qty = %s, Store_sec = %s where Inv_id = %s;'
                    ip = (int(i7_qty), i8_stsec, i5_id)
                    mycursor.execute(query, ip)
                    conn.commit()
                    tkinter.messagebox.showinfo("", "Updated Successfully")

                elif (i6_cost != "" and i7_qty == "" and i8_stsec != ""):
                    query = 'update Wholesale_station set Per_inv_cost = %s, Store_sec = %s where Inv_id = %s;'
                    ip = (int(i6_cost), i8_stsec, i5_id)
                    mycursor.execute(query, ip)
                    conn.commit()
                    tkinter.messagebox.showinfo("", "Updated Successfully")

                elif (i6_cost != "" and i7_qty != "" and i8_stsec != ""):
                    query = 'update Wholesale_station set Inv_qty = %s, Per_inv_cost = %s, Store_sec = %s where Inv_id = %s;'
                    ip = (int(i7_qty), int(i6_cost), i8_stsec, i5_id)
                    mycursor.execute(query, ip)
                    conn.commit()
                    tkinter.messagebox.showinfo("", "Updated Successfully")

                else:
                    tkinter.messagebox.showinfo("", "Nothing Updated")

            except Error as error:
                print(error)

            finally:
                mycursor.close()
                conn.close()

        def delete(event):
            try:
                conn = mysql.connector.connect(host="localhost", user="root", password="root", db="WholeSale_Services")
                print(conn)
                mycursor = conn.cursor()
                lastid = entry10.get()
                query = 'delete from Wholesale_station where Inv_id = %s;'
                ip = (lastid)
                mycursor.execute(query, (ip, ))
                conn.commit()
                tkinter.messagebox.showinfo("", "Deleted Successfully")

            except Error as error:
                print(error)

            finally:
                mycursor.close()
                conn.close()

        def search(event):
            list1.delete(0, 'end')
            try:
                conn = mysql.connector.connect(host="localhost", user="root", password="root", db="WholeSale_Services")
                print(conn)
                mycursor = conn.cursor()

                if (entry9.get() == ""):
                    list1.delete(0, 'end')
                    try:
                        conn = mysql.connector.connect(host="localhost", user="root", password="root", db="WholeSale_Services")
                        print(conn)
                        mycursor = conn.cursor()

                        query = 'SELECT Inv_id from wholesale_station;'
                        mycursor.execute(query)
                        records = mycursor.fetchall()
                        for record in records:
                            print(record)
                            arg = '  Inv_id:- ' + str(record[0])
                            list1.insert(END, arg)
                            conn.commit()

                            # tkinter.messagebox.showinfo("", "Records Searched if exists")

                    except Error as error:
                        print(error)

                    finally:
                        mycursor.close()
                        conn.close()

                    doToastMessage("Please enter Inv_id")
                    return

                else:
                    lastid = entry9.get()
                    query = 'select Wholesale_station.*, Inventory_superset.Inv_name,Inventory_superset.Description, Manufacturer_superset.* from Wholesale_station inner join Inventory_superset on Wholesale_station.Inv_id = %s and Inventory_superset.Inv_id = %s inner join Manufacturer_superset on Manufacturer_superset.Manf_id = (select Manf_id from Manufacture_side_inventory_import_management where Inv_id = %s);'
                    ip = (lastid, lastid, lastid)
                    mycursor.execute(query, ip)
                    records = mycursor.fetchall()
                    for record in records:
                        print(record)
                        arg = '  Inv_id:- ' + str(record[0]) + '  Per_inv_cost:- ' + str(record[1]) + '  Inv_qty:- ' + str(record[2]) + '  Store_sec:- ' + str(record[3]) + '  Tot_inv_cost:- ' + str(record[4]) + '  Inv_name:- ' + str(record[5]) + '  Description:- ' + str(record[6]) + '  Manf_id:- ' + str(record[7]) + '  Manf_name:- ' + str(record[8]) + '  Addr:- ' + str(record[9]) + '  City:- ' + str(record[10]) + '  Cont:- ' + str(record[11])
                        list1.insert(END, arg)
                    conn.commit()

                tkinter.messagebox.showinfo("", "Records Searched if exists")

            except Error as error:
                print(error)

            finally:
                mycursor.close()
                conn.close()

        def setreset(event):
            ans = tkinter.messagebox.askquestion("", "This will SET/RESET the Wholesale Station System!! Proceed with Caution...")
            if ans == "yes":
                try:
                    conn = mysql.connector.connect(host="localhost", user="root", password="root", db="WholeSale_Services")
                    print(conn)
                    mycursor = conn.cursor()
                    mycursor.execute('truncate table Wholesale_station;')
                    tkinter.messagebox.showinfo("", "Wholesale Station System Successfully SET/RESET")

                except Error as error:
                    print(error)

                finally:
                    mycursor.close()
                    conn.close()

        def doClose_rootWholesaleActivityWindow():
            rootWholesaleActivityWindow.destroy()
            rootHomeWindow.update()
            rootHomeWindow.deiconify()

        insertButton.bind("<Button-1>", insert)
        updateButton.bind("<Button-1>", update)
        deleteButton.bind("<Button-1>", delete)
        searchButton.bind("<Button-1>", search)
        setresetButton.bind("<Button-1>", setreset)
        rootWholesaleActivityWindow.protocol("WM_DELETE_WINDOW", doClose_rootWholesaleActivityWindow)

    def doVendor(event):
        rootHomeWindow.withdraw()
        rootVendorActivityWindow = Tk("main")
        rootVendorActivityWindow.configure(background="#BFBFBF")
        rootVendorActivityWindow.title("Vendor Activity")

        labelJust = Label(rootVendorActivityWindow, bg="#bfbfbf")
        labelJust.grid(row=0, column=1)
        labeltitle = Label(rootVendorActivityWindow, bg="dark green", text="**Vendor Services**", font=("Helvetica 16 bold italic"), fg="light green")
        labeltitle.grid(row=1, column=1)

        labelJust = Label(rootVendorActivityWindow, bg="#bfbfbf")
        labelJust.grid(row=2, column=1)
        button1 = Button(rootVendorActivityWindow, text="Vendor Inventory Management", fg="blue", font=14)
        button1.grid(row=3, column=1, sticky=N + S + E + W)

        labelJust = Label(rootVendorActivityWindow, bg="#bfbfbf")
        labelJust.grid(row=4, column=1)
        button2 = Button(rootVendorActivityWindow, text="Vendor Monetary Transaction", fg="blue", font=14)
        button2.grid(row=5, column=1, sticky=N + S + E + W)

        labelJust = Label(rootVendorActivityWindow, bg="#bfbfbf")
        labelJust.grid(row=6, column=1)

        def doVendorInventoryManagement(event):
            rootVendorActivityWindow.withdraw()
            rootVendorInventoryManagementWindow = Tk("main")
            rootVendorInventoryManagementWindow.geometry('520x500')
            rootVendorInventoryManagementWindow.title("Vendor Inventory Management")

            label1 = Label(rootVendorInventoryManagementWindow, text="Inventory ID*")
            label2 = Label(rootVendorInventoryManagementWindow, text="Vendor ID")
            label3 = Label(rootVendorInventoryManagementWindow, text="Per Inventory Cost")
            label4 = Label(rootVendorInventoryManagementWindow, text="Inventory Qty")

            entry1 = Entry(rootVendorInventoryManagementWindow)
            entry2 = Entry(rootVendorInventoryManagementWindow)
            entry3 = Entry(rootVendorInventoryManagementWindow)
            entry4 = Entry(rootVendorInventoryManagementWindow)

            label1.grid(row=1, column=0, sticky=E)
            label2.grid(row=2, column=0, sticky=E)
            label3.grid(row=3, column=0, sticky=E)
            label4.grid(row=4, column=0, sticky=E)

            entry1.grid(row=1, column=1)
            entry2.grid(row=2, column=1)
            entry3.grid(row=3, column=1)
            entry4.grid(row=4, column=1)

            insertButton = Button(rootVendorInventoryManagementWindow, text="INSERT", fg="green")
            insertButton.grid(row=2, column=2, sticky=W)

            dotlabel1 = Label(rootVendorInventoryManagementWindow,
                              text=".......................................................", fg="blue")
            dotlabel1.grid(row=6, column=0)
            dotlabel2 = Label(rootVendorInventoryManagementWindow,
                              text=".......................................................", fg="blue")
            dotlabel2.grid(row=6, column=1)
            dotlabel3 = Label(rootVendorInventoryManagementWindow,
                              text="........................................", fg="blue")
            dotlabel3.grid(row=6, column=2)

            label5 = Label(rootVendorInventoryManagementWindow, text="Inventory ID*")
            label6 = Label(rootVendorInventoryManagementWindow, text="Inventory Qty")
            label7 = Label(rootVendorInventoryManagementWindow, text="Per Inventory Cost")

            entry5 = Entry(rootVendorInventoryManagementWindow)
            entry6 = Entry(rootVendorInventoryManagementWindow)
            entry7 = Entry(rootVendorInventoryManagementWindow)

            label5.grid(row=7, column=0, sticky=E)
            label6.grid(row=8, column=0, sticky=E)
            label7.grid(row=9, column=0, sticky=E)

            entry5.grid(row=7, column=1)
            entry6.grid(row=8, column=1)
            entry7.grid(row=9, column=1)

            updateButton = Button(rootVendorInventoryManagementWindow, text="UPDATE", fg="green")
            updateButton.grid(row=8, column=2, sticky=W)

            dotlabel1 = Label(rootVendorInventoryManagementWindow,
                              text=".......................................................", fg="blue")
            dotlabel1.grid(row=10, column=0)
            dotlabel2 = Label(rootVendorInventoryManagementWindow,
                              text=".......................................................", fg="blue")
            dotlabel2.grid(row=10, column=1)
            dotlabel3 = Label(rootVendorInventoryManagementWindow,
                              text="........................................", fg="blue")
            dotlabel3.grid(row=10, column=2)

            label8 = Label(rootVendorInventoryManagementWindow, text="Inventory ID")
            labelOr = Label(rootVendorInventoryManagementWindow, text="OR")
            label9 = Label(rootVendorInventoryManagementWindow, text="Vendor ID")

            entry8 = Entry(rootVendorInventoryManagementWindow)
            entry9 = Entry(rootVendorInventoryManagementWindow)

            label8.grid(row=11, column=0, sticky=E)
            labelOr.grid(row=12, column=1)
            label9.grid(row=13, column=0, sticky=E)

            entry8.grid(row=11, column=1)
            entry9.grid(row=13, column=1)

            searchButton = Button(rootVendorInventoryManagementWindow, text="SEARCH", fg="green")
            searchButton.grid(row=12, column=2, sticky=W)

            dotlabel1 = Label(rootVendorInventoryManagementWindow,
                              text=".......................................................", fg="blue")
            dotlabel1.grid(row=14, column=0)
            dotlabel2 = Label(rootVendorInventoryManagementWindow,
                              text=".......................................................", fg="blue")
            dotlabel2.grid(row=14, column=1)
            dotlabel3 = Label(rootVendorInventoryManagementWindow,
                              text="........................................", fg="blue")
            dotlabel3.grid(row=14, column=2)

            label10 = Label(rootVendorInventoryManagementWindow, text="Inventory ID")
            entry10 = Entry(rootVendorInventoryManagementWindow)

            label10.grid(row=15, column=0, sticky=E)
            entry10.grid(row=15, column=1)

            deleteButton = Button(rootVendorInventoryManagementWindow, text="DELETE", fg="green")
            deleteButton.grid(row=15, column=2, sticky=W)

            dotlabel1 = Label(rootVendorInventoryManagementWindow,
                              text=".......................................................", fg="blue")
            dotlabel1.grid(row=16, column=0)
            dotlabel2 = Label(rootVendorInventoryManagementWindow,
                              text=".......................................................", fg="blue")
            dotlabel2.grid(row=16, column=1)
            dotlabel3 = Label(rootVendorInventoryManagementWindow,
                              text="........................................", fg="blue")
            dotlabel3.grid(row=16, column=2)

            list1 = Listbox(rootVendorInventoryManagementWindow, height=6, width=80)
            list1.grid(row=17, column=0, columnspan=4)

            sb1 = Scrollbar(rootVendorInventoryManagementWindow)
            sb1.grid(row=17, column=4, rowspan=6)

            list1.configure(yscrollcommand=sb1.set)
            sb1.configure(command=list1.yview())

            dotlabel1 = Label(rootVendorInventoryManagementWindow,
                              text=".......................................................", fg="blue")
            dotlabel1.grid(row=18, column=0)
            dotlabel2 = Label(rootVendorInventoryManagementWindow,
                              text=".......................................................", fg="blue")
            dotlabel2.grid(row=18, column=1)
            dotlabel3 = Label(rootVendorInventoryManagementWindow,
                              text="........................................", fg="blue")
            dotlabel3.grid(row=18, column=2)

            setresetButton = Button(rootVendorInventoryManagementWindow, text="SET/RESET DB", fg="red")
            setresetButton.grid(row=19, column=1)

            def insert(event):
                try:
                    conn = mysql.connector.connect(host="localhost", user="root", password="root", db="WholeSale_Services")
                    print(conn)
                    mycursor = conn.cursor()
                    query = 'insert into Vendor_side_inventory_export_management(Inv_id, Vend_id, Per_inv_cost, Inv_qty) values(%s,%s,%s,%s);'
                    ip = (entry1.get(), entry2.get(), int(entry3.get()), int(entry4.get()))
                    mycursor.execute(query, ip)
                    conn.commit()
                    tkinter.messagebox.showinfo("", "Inserted Successfully")

                except Error as error:
                    print(error)

                finally:
                    mycursor.close()
                    conn.close()

            def update(event):
                conn = mysql.connector.connect(host="localhost", user="root", password="root", db="WholeSale_Services")
                print(conn)
                mycursor = conn.cursor()

                i5_id = entry5.get()
                i6_cost = entry6.get()
                i7_qty = entry7.get()

                try:
                    if (i6_cost != "" and i7_qty == ""):
                        query = 'update Vendor_side_inventory_export_management set Per_inv_cost = %s where Inv_id = %s;'
                        ip = (int(i6_cost), i5_id)
                        mycursor.execute(query, ip)
                        conn.commit()
                        tkinter.messagebox.showinfo("", "Updated Successfully")

                    elif (i6_cost == "" and i7_qty != ""):
                        query = 'update Vendor_side_inventory_export_management set Inv_qty = %s where Inv_id = %s;'
                        ip = (int(i7_qty), i5_id)
                        mycursor.execute(query, ip)
                        conn.commit()
                        tkinter.messagebox.showinfo("", "Updated Successfully")

                    elif (i6_cost != "" and i7_qty != ""):
                        query = 'update Vendor_side_inventory_export_management set Per_inv_cost = %s, Inv_qty = %s where Inv_id = %s;'
                        ip = (int(i6_cost), int(i7_qty), i5_id)
                        mycursor.execute(query, ip)
                        conn.commit()
                        tkinter.messagebox.showinfo("", "Updated Successfully")

                    else:
                        tkinter.messagebox.showinfo("", "Nothing Updated")

                except Error as error:
                    print(error)

                finally:
                    mycursor.close()
                    conn.close()

            def delete(event):
                try:
                    conn = mysql.connector.connect(host="localhost", user="root", password="root",  db="WholeSale_Services")
                    print(conn)
                    mycursor = conn.cursor()
                    lastid = entry10.get()
                    query = 'delete from Vendor_side_inventory_export_management where Inv_id = %s;'
                    ip = (lastid)
                    mycursor.execute(query, (ip, ))
                    conn.commit()
                    tkinter.messagebox.showinfo("", "Deleted Successfully")

                except Error as error:
                    print(error)

                finally:
                    mycursor.close()
                    conn.close()

            def search(event):
                list1.delete(0, 'end')
                try:
                    conn = mysql.connector.connect(host="localhost", user="root", password="root", db="WholeSale_Services")
                    print(conn)
                    mycursor = conn.cursor()

                    if (entry8.get() != "" and entry9.get() != ""):
                        doToastMessage("Please enter only in either of the fields")
                        return

                    elif (entry8.get() != "" and entry9.get() == ""):
                        lastid = entry8.get()
                        query = 'select Inventory_superset.*, Vendor_side_inventory_export_management.Per_inv_cost, Vendor_side_inventory_export_management.Inv_qty, Vendor_side_inventory_export_management.Tot_inv_cost, Vendor_superset.* from Inventory_superset inner join Vendor_side_inventory_export_management on Inventory_superset.Inv_id = %s and Vendor_side_inventory_export_management.Inv_id = %s inner join Vendor_superset on Vendor_side_inventory_export_management.Vend_id = (select Vend_id from Vendor_side_inventory_export_management where Inv_id = %s) and Vendor_superset.Vend_id = (select Vend_id from Vendor_side_inventory_export_management where Inv_id = %s);'
                        ip = (lastid, lastid, lastid, lastid)
                        mycursor.execute(query, ip)
                        records = mycursor.fetchall()
                        for record in records:
                            print(record)
                            arg = '  Inv_id:- ' + str(record[0]) + '  Inv_name:- ' + str(record[1]) + '  Description:- ' + str(record[2]) + '  Per_inv_cost:- ' + str(record[3]) + '  Inv_qty:- ' + str(record[4]) + '  Tot_inv_cost:- ' + str(record[5]) + '  Vend_id:- ' + str(record[6]) + '  Vend_name:- ' + str(record[7]) + '  Addr:- ' + str(record[8]) + '  City:- ' + str(record[9]) + '  Cont:- ' + str(record[10])
                            list1.insert(END, arg)
                        conn.commit()

                    elif (entry8.get() == "" and entry9.get() != ""):
                        lastid = entry9.get()
                        query = 'select Vendor_superset.*, Vendor_side_inventory_export_management.Inv_id, Vendor_side_inventory_export_management.Per_inv_cost, Vendor_side_inventory_export_management.Inv_qty, Vendor_side_inventory_export_management.Tot_inv_cost from Vendor_superset inner join Vendor_side_inventory_export_management on Vendor_superset.Vend_id = %s and Vendor_side_inventory_export_management.Vend_id = %s;'
                        ip = (lastid, lastid)
                        mycursor.execute(query, ip)
                        records = mycursor.fetchall()
                        for record in records:
                            print(record)
                            arg = '  Vend_id:- ' + str(record[0]) + '  Vend_name:- ' + str(record[1]) + '  Addr:- ' + str(record[2]) + '  City:- ' + str(record[3]) + '  Cont:- ' + str(record[4]) + '  Inv_id:- ' + str(record[5]) + '  Per_inv_cost:- ' + str(record[6]) + '  Inv_qty:- ' + str(record[7]) + '  Tot_inv_cost:- ' + str(record[8])
                            list1.insert(END, arg)
                        conn.commit()

                    else:
                        list1.delete(0, 'end')
                        try:
                            conn = mysql.connector.connect(host="localhost", user="root", password="root", db="WholeSale_Services")
                            print(conn)
                            mycursor = conn.cursor()

                            query = 'SELECT Inv_id, Vend_id FROM vendor_side_inventory_export_management;'
                            mycursor.execute(query)
                            records = mycursor.fetchall()
                            for record in records:
                                print(record)
                                arg = '  Inv_id:- ' + str(record[0]) + '  Vend_id:- ' + str(record[1])
                                list1.insert(END, arg)
                                conn.commit()

                                # tkinter.messagebox.showinfo("", "Records Searched if exists")

                        except Error as error:
                            print(error)

                        finally:
                            mycursor.close()
                            conn.close()

                        doToastMessage("Please enter only in either of the fields")
                        return

                    tkinter.messagebox.showinfo("", "Records Searched if exists")

                except Error as error:
                    print(error)

                finally:
                    mycursor.close()
                    conn.close()

            def setreset(event):
                ans = tkinter.messagebox.askquestion("", "This will SET/RESET the Vendor_side_inventory_export_management System!! Proceed with Caution...")
                if ans == "yes":
                    try:
                        conn = mysql.connector.connect(host="localhost", user="root", password="root", db="WholeSale_Services")
                        print(conn)
                        mycursor = conn.cursor()
                        mycursor.execute('truncate table Vendor_side_inventory_export_management;')
                        tkinter.messagebox.showinfo("", "Vendor_side_inventory_export_management System Successfully SET/RESET")

                    except Error as error:
                        print(error)

                    finally:
                        mycursor.close()
                        conn.close()

            def doClose_rootVendorInventoryManagementWindow():
                rootVendorInventoryManagementWindow.destroy()
                rootVendorActivityWindow.update()
                rootVendorActivityWindow.deiconify()

            insertButton.bind("<Button-1>", insert)
            updateButton.bind("<Button-1>", update)
            deleteButton.bind("<Button-1>", delete)
            searchButton.bind("<Button-1>", search)
            setresetButton.bind("<Button-1>", setreset)
            rootVendorInventoryManagementWindow.protocol("WM_DELETE_WINDOW", doClose_rootVendorInventoryManagementWindow)


        def doVendorMonetaryTransaction(event):
            rootVendorActivityWindow.withdraw()
            rootVendorMonetaryTransactionWindow = Tk("main")
            rootVendorMonetaryTransactionWindow.geometry('520x400')
            rootVendorMonetaryTransactionWindow.title("Vendor Monetary Transaction")

            label1 = Label(rootVendorMonetaryTransactionWindow, text="Vendor ID*")
            label2 = Label(rootVendorMonetaryTransactionWindow, text="Paid Amount")

            entry1 = Entry(rootVendorMonetaryTransactionWindow)
            entry2 = Entry(rootVendorMonetaryTransactionWindow)

            label1.grid(row=1, column=0, sticky=E)
            label2.grid(row=2, column=0, sticky=E)

            entry1.grid(row=1, column=1)
            entry2.grid(row=2, column=1)

            insertButton = Button(rootVendorMonetaryTransactionWindow, text="INSERT", fg="green")
            insertButton.grid(row=2, column=2, sticky=W)

            dotlabel1 = Label(rootVendorMonetaryTransactionWindow,
                              text=".......................................................", fg="blue")
            dotlabel1.grid(row=3, column=0)
            dotlabel2 = Label(rootVendorMonetaryTransactionWindow,
                              text=".......................................................", fg="blue")
            dotlabel2.grid(row=3, column=1)
            dotlabel3 = Label(rootVendorMonetaryTransactionWindow,
                              text="........................................", fg="blue")
            dotlabel3.grid(row=3, column=2)

            label3 = Label(rootVendorMonetaryTransactionWindow, text="Transaction No.")
            label4 = Label(rootVendorMonetaryTransactionWindow, text="Paid Amount")
            label5 = Label(rootVendorMonetaryTransactionWindow, text="Date")

            entry3 = Entry(rootVendorMonetaryTransactionWindow)
            entry4 = Entry(rootVendorMonetaryTransactionWindow)
            entry5 = Entry(rootVendorMonetaryTransactionWindow)

            label3.grid(row=4, column=0, sticky=E)
            label4.grid(row=5, column=0, sticky=E)
            label5.grid(row=6, column=0, sticky=E)

            entry3.grid(row=4, column=1)
            entry4.grid(row=5, column=1)
            entry5.grid(row=6, column=1)

            updateButton = Button(rootVendorMonetaryTransactionWindow, text="UPDATE", fg="green")
            updateButton.grid(row=5, column=2, sticky=W)

            dotlabel1 = Label(rootVendorMonetaryTransactionWindow,
                              text=".......................................................", fg="blue")
            dotlabel1.grid(row=7, column=0)
            dotlabel2 = Label(rootVendorMonetaryTransactionWindow,
                              text=".......................................................", fg="blue")
            dotlabel2.grid(row=7, column=1)
            dotlabel3 = Label(rootVendorMonetaryTransactionWindow,
                              text="........................................", fg="blue")
            dotlabel3.grid(row=7, column=2)

            label6 = Label(rootVendorMonetaryTransactionWindow, text="Vendor ID")
            entry6 = Entry(rootVendorMonetaryTransactionWindow)

            label6.grid(row=8, column=0, sticky=E)
            entry6.grid(row=8, column=1)

            searchButton = Button(rootVendorMonetaryTransactionWindow, text="SEARCH", fg="green")
            searchButton.grid(row=8, column=2, sticky=W)

            dotlabel1 = Label(rootVendorMonetaryTransactionWindow,
                              text=".......................................................", fg="blue")
            dotlabel1.grid(row=9, column=0)
            dotlabel2 = Label(rootVendorMonetaryTransactionWindow,
                              text=".......................................................", fg="blue")
            dotlabel2.grid(row=9, column=1)
            dotlabel3 = Label(rootVendorMonetaryTransactionWindow,
                              text="........................................", fg="blue")
            dotlabel3.grid(row=9, column=2)

            label7 = Label(rootVendorMonetaryTransactionWindow, text="Transaction No.")
            entry7 = Entry(rootVendorMonetaryTransactionWindow)

            label7.grid(row=10, column=0, sticky=E)
            entry7.grid(row=10, column=1)

            deleteButton = Button(rootVendorMonetaryTransactionWindow, text="DELETE", fg="green")
            deleteButton.grid(row=10, column=2, sticky=W)

            dotlabel1 = Label(rootVendorMonetaryTransactionWindow,
                              text=".......................................................", fg="blue")
            dotlabel1.grid(row=11, column=0)
            dotlabel2 = Label(rootVendorMonetaryTransactionWindow,
                              text=".......................................................", fg="blue")
            dotlabel2.grid(row=11, column=1)
            dotlabel3 = Label(rootVendorMonetaryTransactionWindow,
                              text="........................................", fg="blue")
            dotlabel3.grid(row=11, column=2)

            list1 = Listbox(rootVendorMonetaryTransactionWindow, height=6, width=80)
            list1.grid(row=12, column=0, columnspan=4)

            sb1 = Scrollbar(rootVendorMonetaryTransactionWindow)
            sb1.grid(row=12, column=4, rowspan=6)

            list1.configure(yscrollcommand=sb1.set)
            sb1.configure(command=list1.yview())

            dotlabel1 = Label(rootVendorMonetaryTransactionWindow,
                              text=".......................................................", fg="blue")
            dotlabel1.grid(row=13, column=0)
            dotlabel2 = Label(rootVendorMonetaryTransactionWindow,
                              text=".......................................................", fg="blue")
            dotlabel2.grid(row=13, column=1)
            dotlabel3 = Label(rootVendorMonetaryTransactionWindow,
                              text="........................................", fg="blue")
            dotlabel3.grid(row=13, column=2)

            setresetButton = Button(rootVendorMonetaryTransactionWindow, text="SET/RESET DB", fg="red")
            setresetButton.grid(row=14, column=1)

            def insert(event):
                try:
                    conn = mysql.connector.connect(host="localhost", user="root", password="root", db="WholeSale_Services")
                    print(conn)
                    mycursor = conn.cursor()
                    query = 'insert into Vendor_side_monetary_transaction(Vend_id, PaidAmt, Occasion) values(%s,%s,sysdate());'
                    ip = (entry1.get(), int(entry2.get()))
                    mycursor.execute(query, ip)
                    conn.commit()
                    tkinter.messagebox.showinfo("", "Inserted Successfully")

                except Error as error:
                    print(error)

                finally:
                    mycursor.close()
                    conn.close()

            def update(event):
                conn = mysql.connector.connect(host="localhost", user="root", password="root", db="WholeSale_Services")
                print(conn)
                mycursor = conn.cursor()

                i3_Tnno = entry3.get()
                i4_paidAmt = entry4.get()
                i5_date = entry5.get()

                try:
                    if (i4_paidAmt != "" and i5_date == ""):
                        query = 'update Vendor_side_monetary_transaction set PaidAmt = %s where Tn_no = %s;'
                        ip = (int(i4_paidAmt), int(i3_Tnno))
                        mycursor.execute(query, ip)
                        conn.commit()
                        tkinter.messagebox.showinfo("", "Updated Successfully")

                    elif (i4_paidAmt == "" and i5_date != ""):
                        query = 'update Vendor_side_monetary_transaction set Occasion = %s where Tn_no = %s;'
                        ip = (i5_date, int(i3_Tnno))
                        mycursor.execute(query, ip)
                        conn.commit()
                        tkinter.messagebox.showinfo("", "Updated Successfully")

                    elif (i4_paidAmt != "" and i5_date != ""):
                        query = 'update Vendor_side_monetary_transaction set PaidAmt = %s, Occasion = %s where Tn_no = %s;'
                        ip = (int(i4_paidAmt), i5_date, int(i3_Tnno))
                        mycursor.execute(query, ip)
                        conn.commit()
                        tkinter.messagebox.showinfo("", "Updated Successfully")

                    else:
                        tkinter.messagebox.showinfo("", "Nothing Updated")

                except Error as error:
                    print(error)

                finally:
                    mycursor.close()
                    conn.close()

            def delete(event):
                try:
                    conn = mysql.connector.connect(host="localhost", user="root", password="root",  db="WholeSale_Services")
                    print(conn)
                    mycursor = conn.cursor()
                    lastid = entry7.get()
                    query = 'delete from Vendor_side_monetary_transaction where Tn_no = %s;'
                    ip = (lastid)
                    mycursor.execute(query, (ip, ))
                    conn.commit()
                    tkinter.messagebox.showinfo("", "Deleted Successfully")

                except Error as error:
                    print(error)

                finally:
                    mycursor.close()
                    conn.close()

            def search(event):
                list1.delete(0, 'end')
                try:
                    conn = mysql.connector.connect(host="localhost", user="root", password="root", db="WholeSale_Services")
                    print(conn)
                    mycursor = conn.cursor()

                    if (entry6.get() == ""):
                        list1.delete(0, 'end')
                        try:
                            conn = mysql.connector.connect(host="localhost", user="root", password="root", db="WholeSale_Services")
                            print(conn)
                            mycursor = conn.cursor()

                            query = 'SELECT Vend_id FROM vendor_side_monetary_transaction;'
                            mycursor.execute(query)
                            records = mycursor.fetchall()
                            for record in records:
                                print(record)
                                arg = '  Vend_id:- ' + str(record[0])
                                list1.insert(END, arg)
                                conn.commit()

                            #tkinter.messagebox.showinfo("", "Records Searched if exists")

                        except Error as error:
                            print(error)

                        finally:
                            mycursor.close()
                            conn.close()

                        doToastMessage("Please enter Vend_id")
                        return

                    else:
                        lastid = entry6.get()
                        query = 'select Vendor_superset.*, Vendor_side_inventory_export_management.Inv_id, Vendor_side_inventory_export_management.Per_inv_cost, Vendor_side_inventory_export_management.Inv_qty, Vendor_side_inventory_export_management.Tot_inv_cost from Vendor_superset inner join Vendor_side_inventory_export_management on Vendor_superset.Vend_id = %s and Vendor_side_inventory_export_management.Vend_id = %s;'
                        ip = (lastid, lastid)
                        mycursor.execute(query, ip)
                        records = mycursor.fetchall()
                        for record in records:
                            print(record)
                            arg = '  Tn_no:- ' + str(record[0]) + '  Vend_id:- ' + str(record[1]) + '  Paid_amt:- ' + str(record[2]) + '  Occasion:- ' + str(record[3]) + '  Vend_name:- ' + str(record[4]) + '  Addr:- ' + str(record[5]) + '  City:- ' + str(record[6]) + '  Cont:- ' + str(record[7])
                            list1.insert(END, arg)
                        conn.commit()

                    tkinter.messagebox.showinfo("", "Records Searched if exists")

                except Error as error:
                    print(error)

                finally:
                    mycursor.close()
                    conn.close()

            def setreset(event):
                ans = tkinter.messagebox.askquestion("", "This will SET/RESET the Vendor_side_monetary_transaction System!! Proceed with Caution...")
                if ans == "yes":
                    try:
                        conn = mysql.connector.connect(host="localhost", user="root", password="root", db="WholeSale_Services")
                        print(conn)
                        mycursor = conn.cursor()
                        mycursor.execute('truncate table Vendor_side_monetary_transaction;')
                        tkinter.messagebox.showinfo("", "Vendor_side_monetary_transaction System Successfully SET/RESET")

                    except Error as error:
                        print(error)

                    finally:
                        mycursor.close()
                        conn.close()

            def doClose_rootVendorMonetaryTransactionWindow():
                rootVendorMonetaryTransactionWindow.destroy()
                rootVendorActivityWindow.update()
                rootVendorActivityWindow.deiconify()

            insertButton.bind("<Button-1>", insert)
            updateButton.bind("<Button-1>", update)
            deleteButton.bind("<Button-1>", delete)
            searchButton.bind("<Button-1>", search)
            setresetButton.bind("<Button-1>", setreset)
            rootVendorMonetaryTransactionWindow.protocol("WM_DELETE_WINDOW", doClose_rootVendorMonetaryTransactionWindow)

        def doClose_VendorActivityWindow():
            rootVendorActivityWindow.destroy()
            rootHomeWindow.update()
            rootHomeWindow.deiconify()

        rootVendorActivityWindow.protocol("WM_DELETE_WINDOW", doClose_VendorActivityWindow)

        button1.bind("<Button-1>", doVendorInventoryManagement)
        button2.bind("<Button-1>", doVendorMonetaryTransaction)

        rootVendorActivityWindow.mainloop()

    def doParent(event):
        rootHomeWindow.withdraw()
        rootParDBActivityWindow = Tk("main")
        rootParDBActivityWindow.configure(background="#BFBFBF")
        rootParDBActivityWindow.title("Parent DB Activity")

        labelJust = Label(rootParDBActivityWindow, bg="#bfbfbf")
        labelJust.grid(row=0, column=1)
        labeltitle = Label(rootParDBActivityWindow, bg="dark green", text="**Parent DataBase Superset**", font=("Helvetica 16 bold italic"), fg="light green")
        labeltitle.grid(row=1, column=1)

        labelJust = Label(rootParDBActivityWindow, bg="#bfbfbf")
        labelJust.grid(row=2, column=1)
        button1 = Button(rootParDBActivityWindow, text="Manufacturer Superset", fg="blue", font=14)
        button1.grid(row=3, column=1, sticky=N + S + E + W)

        labelJust = Label(rootParDBActivityWindow, bg="#bfbfbf")
        labelJust.grid(row=4, column=1)
        button2 = Button(rootParDBActivityWindow, text="Vendor Superset", fg="blue", font=14)
        button2.grid(row=5, column=1, sticky=N + S + E + W)

        labelJust = Label(rootParDBActivityWindow, bg="#bfbfbf")
        labelJust.grid(row=6, column=1)
        button3 = Button(rootParDBActivityWindow, text="Inventory Superset", fg="blue", font=14)
        button3.grid(row=7, column=1, sticky=N + S + E + W)

        labelJust = Label(rootParDBActivityWindow, bg="#bfbfbf")
        labelJust.grid(row=8, column=1)

        def doManufacturerSuperset(event):
            rootParDBActivityWindow.withdraw()
            rootManufacturerSupersetWindow = Tk("main")
            rootManufacturerSupersetWindow.geometry('520x320')
            rootManufacturerSupersetWindow.title("Manufacturer Superset")

            label1 = Label(rootManufacturerSupersetWindow, text="Manufacturer ID*")
            label2 = Label(rootManufacturerSupersetWindow, text="Name")
            label3 = Label(rootManufacturerSupersetWindow, text="Address")
            label4 = Label(rootManufacturerSupersetWindow, text="City")
            label5 = Label(rootManufacturerSupersetWindow, text="Contact")

            entry1 = Entry(rootManufacturerSupersetWindow)
            entry2 = Entry(rootManufacturerSupersetWindow)
            entry3 = Entry(rootManufacturerSupersetWindow)
            entry4 = Entry(rootManufacturerSupersetWindow)
            entry5 = Entry(rootManufacturerSupersetWindow)

            label1.grid(row=1, column=0, sticky=E)
            label2.grid(row=2, column=0, sticky=E)
            label3.grid(row=3, column=0, sticky=E)
            label4.grid(row=4, column=0, sticky=E)
            label5.grid(row=5, column=0, sticky=E)

            entry1.grid(row=1, column=1)
            entry2.grid(row=2, column=1)
            entry3.grid(row=3, column=1)
            entry4.grid(row=4, column=1)
            entry5.grid(row=5, column=1)

            insertButton = Button(rootManufacturerSupersetWindow, text="INSERT", fg="green")
            insertButton.grid(row=3, column=2, sticky=W)

            dotlabel1 = Label(rootManufacturerSupersetWindow,
                              text=".......................................................", fg="blue")
            dotlabel1.grid(row=6, column=0)
            dotlabel2 = Label(rootManufacturerSupersetWindow,
                              text=".......................................................", fg="blue")
            dotlabel2.grid(row=6, column=1)
            dotlabel3 = Label(rootManufacturerSupersetWindow,
                              text="........................................", fg="blue")
            dotlabel3.grid(row=6, column=2)

            label6 = Label(rootManufacturerSupersetWindow, text="Manufacturer ID")
            entry6 = Entry(rootManufacturerSupersetWindow)

            label6.grid(row=7, column=0, sticky=E)
            entry6.grid(row=7, column=1)

            searchButton = Button(rootManufacturerSupersetWindow, text="SEARCH", fg="green")
            searchButton.grid(row=7, column=2, sticky=W)

            dotlabel1 = Label(rootManufacturerSupersetWindow,
                              text=".......................................................", fg="blue")
            dotlabel1.grid(row=8, column=0)
            dotlabel2 = Label(rootManufacturerSupersetWindow,
                              text=".......................................................", fg="blue")
            dotlabel2.grid(row=8, column=1)
            dotlabel3 = Label(rootManufacturerSupersetWindow,
                              text="........................................", fg="blue")
            dotlabel3.grid(row=8, column=2)

            list1 = Listbox(rootManufacturerSupersetWindow, height=6, width=80)
            list1.grid(row=9, column=0, columnspan=4)

            sb1 = Scrollbar(rootManufacturerSupersetWindow)
            sb1.grid(row=9, column=4, rowspan=6)

            list1.configure(yscrollcommand=sb1.set)
            sb1.configure(command=list1.yview())

            dotlabel1 = Label(rootManufacturerSupersetWindow,
                              text=".......................................................", fg="blue")
            dotlabel1.grid(row=10, column=0)
            dotlabel2 = Label(rootManufacturerSupersetWindow,
                              text=".......................................................", fg="blue")
            dotlabel2.grid(row=10, column=1)
            dotlabel3 = Label(rootManufacturerSupersetWindow,
                              text="........................................", fg="blue")
            dotlabel3.grid(row=10, column=2)

            def insert(event):
                try:
                    conn = mysql.connector.connect(host="localhost", user="root", password="root", db="WholeSale_Services")
                    print(conn)
                    mycursor = conn.cursor()
                    query = 'insert into Manufacturer_superset(Manf_id, Manf_name, Addr, City, Cont) values(%s,%s,%s,%s,%s);'
                    ip = (entry1.get(), entry2.get(), entry3.get(), entry4.get(), entry5.get())
                    mycursor.execute(query, ip)
                    conn.commit()
                    tkinter.messagebox.showinfo("", "Inserted Successfully")

                except Error as error:
                    print(error)

                finally:
                    mycursor.close()
                    conn.close()

            def search(event):
                list1.delete(0, 'end')
                try:
                    conn = mysql.connector.connect(host="localhost", user="root", password="root", db="WholeSale_Services")
                    print(conn)
                    mycursor = conn.cursor()

                    if (entry6.get() == ""):
                        query = 'select * from Manufacturer_superset;'
                        mycursor.execute(query)
                        records = mycursor.fetchall()
                        for record in records:
                            print(record)
                            arg = '  Manf_id:- ' + str(record[0]) + '  Manf_name:- ' + str(record[1]) + '  Addr:- ' + str(record[2]) + '  City:- ' + str(record[3]) + '  Cont:- ' + str(record[4])
                            list1.insert(END, arg)
                        conn.commit()
                    else:
                        lastid = entry6.get()
                        query = 'select * from Manufacturer_superset where Manf_id = %s;'
                        ip = (lastid)
                        mycursor.execute(query, (ip, ))
                        records = mycursor.fetchall()
                        for record in records:
                            print(record)
                            arg = '  Manf_id:- ' + str(record[0]) + '  Manf_name:- ' + str(record[1]) + '  Addr:- ' + str(record[2]) + '  City:- ' + str(record[3]) + '  Cont:- ' + str(record[4])
                            list1.insert(END, arg)
                        conn.commit()

                    tkinter.messagebox.showinfo("", "Records Searched if exists")

                except Error as error:
                    print(error)

                finally:
                    mycursor.close()
                    conn.close()

            def doClose_rootManufacturerSupersetWindow():
                rootManufacturerSupersetWindow.destroy()
                rootParDBActivityWindow.update()
                rootParDBActivityWindow.deiconify()

            insertButton.bind("<Button-1>", insert)
            searchButton.bind("<Button-1>", search)
            rootManufacturerSupersetWindow.protocol("WM_DELETE_WINDOW", doClose_rootManufacturerSupersetWindow)

        def doVendorSuperset(event):
            rootParDBActivityWindow.withdraw()
            rootVendorSupersetWindow = Tk("main")
            rootVendorSupersetWindow.geometry('520x320')
            rootVendorSupersetWindow.title("Vendor Superset")

            label1 = Label(rootVendorSupersetWindow, text="Vendor ID*")
            label2 = Label(rootVendorSupersetWindow, text="Name")
            label3 = Label(rootVendorSupersetWindow, text="Address")
            label4 = Label(rootVendorSupersetWindow, text="City")
            label5 = Label(rootVendorSupersetWindow, text="Contact")

            entry1 = Entry(rootVendorSupersetWindow)
            entry2 = Entry(rootVendorSupersetWindow)
            entry3 = Entry(rootVendorSupersetWindow)
            entry4 = Entry(rootVendorSupersetWindow)
            entry5 = Entry(rootVendorSupersetWindow)

            label1.grid(row=1, column=0, sticky=E)
            label2.grid(row=2, column=0, sticky=E)
            label3.grid(row=3, column=0, sticky=E)
            label4.grid(row=4, column=0, sticky=E)
            label5.grid(row=5, column=0, sticky=E)

            entry1.grid(row=1, column=1)
            entry2.grid(row=2, column=1)
            entry3.grid(row=3, column=1)
            entry4.grid(row=4, column=1)
            entry5.grid(row=5, column=1)

            insertButton = Button(rootVendorSupersetWindow, text="INSERT", fg="green")
            insertButton.grid(row=3, column=2, sticky=W)

            dotlabel1 = Label(rootVendorSupersetWindow,
                              text=".......................................................", fg="blue")
            dotlabel1.grid(row=6, column=0)
            dotlabel2 = Label(rootVendorSupersetWindow,
                              text=".......................................................", fg="blue")
            dotlabel2.grid(row=6, column=1)
            dotlabel3 = Label(rootVendorSupersetWindow,
                              text="........................................", fg="blue")
            dotlabel3.grid(row=6, column=2)

            label6 = Label(rootVendorSupersetWindow, text="Vendor ID")
            entry6 = Entry(rootVendorSupersetWindow)

            label6.grid(row=7, column=0, sticky=E)
            entry6.grid(row=7, column=1)

            searchButton = Button(rootVendorSupersetWindow, text="SEARCH", fg="green")
            searchButton.grid(row=7, column=2, sticky=W)

            dotlabel1 = Label(rootVendorSupersetWindow,
                              text=".......................................................", fg="blue")
            dotlabel1.grid(row=8, column=0)
            dotlabel2 = Label(rootVendorSupersetWindow,
                              text=".......................................................", fg="blue")
            dotlabel2.grid(row=8, column=1)
            dotlabel3 = Label(rootVendorSupersetWindow,
                              text="........................................", fg="blue")
            dotlabel3.grid(row=8, column=2)

            list1 = Listbox(rootVendorSupersetWindow, height=6, width=80)
            list1.grid(row=9, column=0, columnspan=4)

            sb1 = Scrollbar(rootVendorSupersetWindow)
            sb1.grid(row=9, column=4, rowspan=6)

            list1.configure(yscrollcommand=sb1.set)
            sb1.configure(command=list1.yview())

            dotlabel1 = Label(rootVendorSupersetWindow,
                              text=".......................................................", fg="blue")
            dotlabel1.grid(row=10, column=0)
            dotlabel2 = Label(rootVendorSupersetWindow,
                              text=".......................................................", fg="blue")
            dotlabel2.grid(row=10, column=1)
            dotlabel3 = Label(rootVendorSupersetWindow,
                              text="........................................", fg="blue")
            dotlabel3.grid(row=10, column=2)

            def insert(event):
                try:
                    conn = mysql.connector.connect(host="localhost", user="root", password="root", db="WholeSale_Services")
                    print(conn)
                    mycursor = conn.cursor()
                    query = 'insert into Vendor_superset(Vend_id, Vend_name, Addr, City, Cont) values(%s,%s,%s,%s,%s);'
                    ip = (entry1.get(), entry2.get(), entry3.get(), entry4.get(), entry5.get())
                    mycursor.execute(query, ip)
                    conn.commit()
                    tkinter.messagebox.showinfo("", "Inserted Successfully")

                except Error as error:
                    print(error)

                finally:
                    mycursor.close()
                    conn.close()

            def search(event):
                list1.delete(0, 'end')
                try:
                    conn = mysql.connector.connect(host="localhost", user="root", password="root", db="WholeSale_Services")
                    print(conn)
                    mycursor = conn.cursor()

                    if (entry6.get() == ""):
                        query = 'select * from Vendor_superset;'
                        mycursor.execute(query)
                        records = mycursor.fetchall()
                        for record in records:
                            print(record)
                            arg = '  Vend_id:- ' + str(record[0]) + '  Vend_name:- ' + str(record[1]) + '  Addr:- ' + str(record[2]) + '  City:- ' + str(record[3]) + '  Cont:- ' + str(record[4])
                            list1.insert(END, arg)
                        conn.commit()
                    else:
                        lastid = entry6.get()
                        query = 'select * from Vendor_superset where Vend_id = %s;'
                        ip = (lastid)
                        mycursor.execute(query, (ip, ))
                        records = mycursor.fetchall()
                        for record in records:
                            print(record)
                            arg = '  Vend_id:- ' + str(record[0]) + '  Vend_name:- ' + str(record[1]) + '  Addr:- ' + str(record[2]) + '  City:- ' + str(record[3]) + '  Cont:- ' + str(record[4])
                            list1.insert(END, arg)
                        conn.commit()

                    tkinter.messagebox.showinfo("", "Records Searched if exists")

                except Error as error:
                    print(error)

                finally:
                    mycursor.close()
                    conn.close()

            def doClose_rootVendorSupersetWindow():
                rootVendorSupersetWindow.destroy()
                rootParDBActivityWindow.update()
                rootParDBActivityWindow.deiconify()

            insertButton.bind("<Button-1>", insert)
            searchButton.bind("<Button-1>", search)
            rootVendorSupersetWindow.protocol("WM_DELETE_WINDOW", doClose_rootVendorSupersetWindow)

        def doInventorySuperset(event):
            rootParDBActivityWindow.withdraw()
            rootInventorySupersetWindow = Tk("main")
            rootInventorySupersetWindow.geometry('520x280')
            rootInventorySupersetWindow.title("Inventory Superset")

            label1 = Label(rootInventorySupersetWindow, text="Inventory ID")
            label2 = Label(rootInventorySupersetWindow, text="Name")
            label3 = Label(rootInventorySupersetWindow, text="Desscription")

            entry1 = Entry(rootInventorySupersetWindow)
            entry2 = Entry(rootInventorySupersetWindow)
            entry3 = Entry(rootInventorySupersetWindow)

            label1.grid(row=1, column=0, sticky=E)
            label2.grid(row=2, column=0, sticky=E)
            label3.grid(row=3, column=0, sticky=E)

            entry1.grid(row=1, column=1)
            entry2.grid(row=2, column=1)
            entry3.grid(row=3, column=1)

            insertButton = Button(rootInventorySupersetWindow, text="INSERT", fg="green")
            insertButton.grid(row=2, column=2, sticky=W)

            dotlabel1 = Label(rootInventorySupersetWindow,
                              text=".......................................................", fg="blue")
            dotlabel1.grid(row=4, column=0)
            dotlabel2 = Label(rootInventorySupersetWindow,
                              text=".......................................................", fg="blue")
            dotlabel2.grid(row=4, column=1)
            dotlabel3 = Label(rootInventorySupersetWindow,
                              text="........................................", fg="blue")
            dotlabel3.grid(row=4, column=2)

            label4 = Label(rootInventorySupersetWindow, text="Inventory ID")
            entry4 = Entry(rootInventorySupersetWindow)

            label4.grid(row=5, column=0, sticky=E)
            entry4.grid(row=5, column=1)

            searchButton = Button(rootInventorySupersetWindow, text="SEARCH", fg="green")
            searchButton.grid(row=5, column=2, sticky=W)

            dotlabel1 = Label(rootInventorySupersetWindow,
                              text=".......................................................", fg="blue")
            dotlabel1.grid(row=6, column=0)
            dotlabel2 = Label(rootInventorySupersetWindow,
                              text=".......................................................", fg="blue")
            dotlabel2.grid(row=6, column=1)
            dotlabel3 = Label(rootInventorySupersetWindow,
                              text="........................................", fg="blue")
            dotlabel3.grid(row=6, column=2)

            list1 = Listbox(rootInventorySupersetWindow, height=6, width=80)
            list1.grid(row=7, column=0, columnspan=4)

            sb1 = Scrollbar(rootInventorySupersetWindow)
            sb1.grid(row=7, column=4, rowspan=6)

            list1.configure(yscrollcommand=sb1.set)
            sb1.configure(command=list1.yview())

            dotlabel1 = Label(rootInventorySupersetWindow,
                              text=".......................................................", fg="blue")
            dotlabel1.grid(row=8, column=0)
            dotlabel2 = Label(rootInventorySupersetWindow,
                              text=".......................................................", fg="blue")
            dotlabel2.grid(row=8, column=1)
            dotlabel3 = Label(rootInventorySupersetWindow,
                              text="........................................", fg="blue")
            dotlabel3.grid(row=8, column=2)

            def insert(event):
                try:
                    conn = mysql.connector.connect(host="localhost", user="root", password="root", db="WholeSale_Services")
                    print(conn)
                    mycursor = conn.cursor()
                    query = 'insert into Inventory_superset(Inv_id, Inv_name, Description) values(%s,%s,%s);'
                    ip = (entry1.get(), entry2.get(), entry3.get())
                    mycursor.execute(query, ip)
                    conn.commit()
                    tkinter.messagebox.showinfo("", "Inserted Successfully")

                except Error as error:
                    print(error)

                finally:
                    mycursor.close()
                    conn.close()

            def search(event):
                list1.delete(0, 'end')
                try:
                    conn = mysql.connector.connect(host="localhost", user="root", password="root",
                                                   db="WholeSale_Services")
                    print(conn)
                    mycursor = conn.cursor()

                    if (entry4.get() == ""):
                        query = 'select * from Inventory_superset;'
                        mycursor.execute(query)
                        records = mycursor.fetchall()
                        for record in records:
                            print(record)
                            arg = '  Inv_id:- ' + str(record[0]) + '  Inv_name:- ' + str(record[1]) + '  Description:- ' + str(record[2])
                            list1.insert(END, arg)
                        conn.commit()
                    else:
                        lastid = entry4.get()
                        query = 'select * from Inventory_superset where Inv_id = %s;'
                        ip = (lastid)
                        mycursor.execute(query, (ip, ))
                        records = mycursor.fetchall()
                        for record in records:
                            print(record)
                            arg = '  Inv_id:- ' + str(record[0]) + '  Inv_name:- ' + str(record[1]) + '  Description:- ' + str(record[2])
                            list1.insert(END, arg)
                        conn.commit()

                    tkinter.messagebox.showinfo("", "Records Searched if exists")

                except Error as error:
                    print(error)

                finally:
                    mycursor.close()
                    conn.close()

            def doClose_rootInventorySupersetWindow():
                rootInventorySupersetWindow.destroy()
                rootParDBActivityWindow.update()
                rootParDBActivityWindow.deiconify()

            insertButton.bind("<Button-1>", insert)
            searchButton.bind("<Button-1>", search)
            rootInventorySupersetWindow.protocol("WM_DELETE_WINDOW", doClose_rootInventorySupersetWindow)

        def doClose_rootParDBActivityWindow():
            rootParDBActivityWindow.destroy()
            rootHomeWindow.update()
            rootHomeWindow.deiconify()

        rootParDBActivityWindow.protocol("WM_DELETE_WINDOW", doClose_rootParDBActivityWindow)
        button1.bind("<Button-1>", doManufacturerSuperset)
        button2.bind("<Button-1>", doVendorSuperset)
        button3.bind("<Button-1>", doInventorySuperset)

        rootParDBActivityWindow.mainloop()

    def doSetResetAll(event):
        ans = tkinter.messagebox.askquestion("", "This will SET/RESET the Whole DataBase System!! Proceed with Caution...")
        if ans == "yes":
            try:
                conn = mysql.connector.connect(host="localhost", user="root", password="root")
                print(conn)
                mycursor = conn.cursor()
                mycursor.execute('drop database if exists WholeSale_Services;')
                mycursor.execute('create database WholeSale_Services;')
                mycursor.execute('use WholeSale_Services;')

                mycursor.execute('Drop table if exists Manufacturer_superset;')
                mycursor.execute('create table Manufacturer_superset(Manf_id varchar(20), Manf_name varchar(20), Addr varchar(20),City varchar(20), Cont varchar(20), primary key(Manf_id));')

                mycursor.execute('Drop table if exists Vendor_superset;')
                mycursor.execute('create table Vendor_superset(Vend_id varchar(20), Vend_name varchar(20), Addr varchar(20),City varchar(20), Cont varchar(20), primary key(Vend_id));')

                mycursor.execute('Drop table if exists Inventory_superset;')
                mycursor.execute('create table Inventory_superset(Inv_id varchar(20), Inv_name varchar(20), Description varchar(20), primary key(Inv_id));')

                mycursor.execute('Drop table if exists Manufacture_side_inventory_import_management; ')
                mycursor.execute('create table Manufacture_side_inventory_import_management(Inv_id varchar(20), Manf_id varchar(20), Per_inv_cost int(10), Inv_qty int(10), Tot_inv_cost int(10) as (Per_inv_cost * Inv_qty),foreign key(Inv_id) references Inventory_superset(Inv_id),foreign key(Manf_id) references Manufacturer_superset(Manf_id),primary key(Inv_id));')

                mycursor.execute('Drop table if exists Manufacture_side_monetary_transaction; ')
                mycursor.execute('create table Manufacture_side_monetary_transaction(Tn_no int(10) auto_increment, Manf_id varchar(20), PaidAmt int(20), Occasion Date, primary key(Tn_no), foreign key(Manf_id) references Manufacturer_superset(Manf_id));')

                mycursor.execute('Drop table if exists Wholesale_station; ')
                mycursor.execute('create table Wholesale_station(Inv_id varchar(20), Per_inv_cost int(10), Inv_qty int(10), Store_sec varchar(10), Tot_inv_cost int(10) as (Per_inv_cost * Inv_qty), foreign key(Inv_id) references Inventory_superset(Inv_id), primary key(Inv_id));')

                mycursor.execute('Drop table if exists Vendor_side_inventory_export_management; ')
                mycursor.execute('create table Vendor_side_inventory_export_management(Inv_id varchar(20), Vend_id varchar(20), Per_inv_cost int(10), Inv_qty int(10), Tot_inv_cost int(10) as (Per_inv_cost * Inv_qty), foreign key(Inv_id) references Inventory_superset(Inv_id),foreign key(Vend_id) references Vendor_superset(Vend_id),primary key(Inv_id));')

                mycursor.execute('Drop table if exists Vendor_side_monetary_transaction;')
                mycursor.execute('create table Vendor_side_monetary_transaction(Tn_no int(10) auto_increment, Vend_id varchar(20), PaidAmt int(20), Occasion Date, primary key(Tn_no), foreign key(Vend_id) references Vendor_superset(Vend_id));')

                tkinter.messagebox.showinfo("", "DataBase System Successfully SET/RESET")

            except Error as error:
                print(error)

            finally:
                mycursor.close()
                conn.close()

    def doClose_HomeActivity():
        rootHomeWindow.destroy()
        rootWindow.update()
        rootWindow.deiconify()

    rootHomeWindow.protocol("WM_DELETE_WINDOW", doClose_HomeActivity)
    button1.bind("<Button-1>", doManufacturer)
    button2.bind("<Button-1>", doWholesale)
    button3.bind("<Button-1>", doVendor)
    button4.bind("<Button-1>", doParent)
    button5.bind("<Button-1>", doSetResetAll)

    rootHomeWindow.mainloop()


def doToastMessage(arg):
    tkinter.messagebox.showinfo("", arg)

def doAskQuestion(arg):
    ans = tkinter.messagebox.askquestion("", arg)
    return ans

def doLoginActivity(event):
    #doToastMessage("Please Wait...")
    try:
        conn = mysql.connector.connect(host="localhost", user="root", password="root", db = "WholeSale_Services_Authentication")
        print(conn)
        mycursor = conn.cursor()
        query = 'SELECT * from authentication;'
        mycursor.execute(query)
        record = mycursor.fetchone()
        #if(record[0] == entryUsername.get() and record[1] == entryPassword.get()):
        if(record[0] == "1" and record[1] == "1"):
            doHomeActivity()
        conn.commit()


    except Error as error:
        print(error)

    finally:
        mycursor.close()
        conn.close()

def doClose_rootWindow():
    ans = doAskQuestion("Do you want to Quit?")
    if(ans == "yes"):
        rootWindow.destroy()

loginButton.bind("<Button-1>", doLoginActivity)
rootWindow.protocol("WM_DELETE_WINDOW", doClose_rootWindow)
rootWindow.mainloop()