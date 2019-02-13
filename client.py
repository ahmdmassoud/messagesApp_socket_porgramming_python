import socket
from threading import Thread
import tkinter
from tkinter import font


def User_send(event=None):
    msg = my_msg.get()
    my_msg.set("") 
    client_socket.send(bytes(msg, "utf8"))
    print("this message was sent %s!\n" % msg)

def receive():
       while True:
        try:
            msg = client_socket.recv(1024).decode("utf8")
            msg_list.insert(tkinter.END, msg)
            print("New Message recieved, %s!\n" % msg)
        except OSError:  
            break


master = tkinter.Tk()
master.title("socket instant messages by Ahmed Massoud")
font10 = font.Font(size=10)
font15 = font.Font(size=15)
messages_frame = tkinter.Frame(master)
my_msg = tkinter.StringVar()  
my_msg.set("")
scrollbar = tkinter.Scrollbar(messages_frame)  
msg_list = tkinter.Listbox(messages_frame, height=30, width=50, yscrollcommand=scrollbar.set,font=font10)
scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
msg_list.pack(side=tkinter.LEFT, fill=tkinter.BOTH)
msg_list.pack()
messages_frame.pack(expand=True)

entry_field = tkinter.Entry(master, textvariable=my_msg, font=font10)
entry_field.bind("<Return>", User_send)
entry_field.pack()
send_button = tkinter.Button(master, text="Send", command=User_send, font=font10)
send_button.pack()



host = socket.gethostname()
port = 1233
client_socket =  socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
client_socket.connect((host, port))
receive_thread = Thread(target=receive)
receive_thread.start()
tkinter.mainloop()
