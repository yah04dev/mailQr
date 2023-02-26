import os
import sqlite3
import qrcode

    

 
import tkinter as tk
  
root=tk.Tk()
 
# setting the windows size
root.geometry("300x100")
root.title('email to qr')
root.iconbitmap('search.ico')  
# declaring string variable
# for storing name and password
idt=tk.StringVar()

 
  
# defining a function that will
# get the name and password and
# print them on the screen
def submit():
    def printqrc(email,passd):
        file_path = "output.png"
        if os.path.exists(file_path):
          os.remove(file_path)
        text = email+"/"+passd
        qr_code = qrcode.make(text)
        qr_code.save("output.png")
        os.system("mspaint /pt output.png")
        print("QR code generated successfully.")


# Open a connection to the database file
    conn = sqlite3.connect("emails.db")

# Create a cursor object to execute SQL statements
    cur = conn.cursor()

# Get input ID from user
    id=idt.get()
   

# Execute a SELECT statement to retrieve the name and date of birth based on the input ID
    cur.execute("SELECT email, passd FROM mailiste WHERE id=?", (id,))
    result = cur.fetchone()

# Check if result is not None
    if result is not None:
    # Print the name and date of birth
            email, passd = result
            printqrc(email,passd)
    else:
        print("No record found.")
   
    cur.close()
    conn.close()

     
    
     
     
# creating a label for
# name using widget Label
name_label = tk.Label(root, text = 'ID: ', font=('calibre',10, 'bold'))
  
# creating a entry for input
# name using widget Entry
name_entry = tk.Entry(root,textvariable = idt, font=('calibre',10,'normal'))
  

# creating a button using the widget
# Button that will call the submit function
sub_btn=tk.Button(root,text = 'Print', command = submit)
  
# placing the label and entry in
# the required position using grid
# method
name_label.grid(row=0,column=0)
name_entry.grid(row=0,column=1)

sub_btn.grid(row=2,column=1)
  
# performing an infinite loop
# for the window to display
root.mainloop()