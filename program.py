import os
import sqlite3
import qrcode

    

 
import tkinter as tk
  
root=tk.Tk()
 

root.geometry("300x100")
root.title('email to qr')
root.iconbitmap('search.ico')  

idt=tk.StringVar()

 
  

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


    conn = sqlite3.connect("emails.db")


    cur = conn.cursor()


    id=idt.get()
   


    cur.execute("SELECT email, passd FROM mailiste WHERE id=?", (id,))
    result = cur.fetchone()


    if result is not None:
    
            email, passd = result
            printqrc(email,passd)
    else:
        print("No record found.")
   
    cur.close()
    conn.close()

     

name_label = tk.Label(root, text = 'ID: ', font=('calibre',10, 'bold'))
  

name_entry = tk.Entry(root,textvariable = idt, font=('calibre',10,'normal'))
  
sub_btn=tk.Button(root,text = 'Print', command = submit)

name_label.grid(row=0,column=0)
name_entry.grid(row=0,column=1)

sub_btn.grid(row=2,column=1)
  

root.mainloop()
