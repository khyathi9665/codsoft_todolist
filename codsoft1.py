import tkinter as tk
class ToDo:
    def __init__(self):
        self.main_window=tk.Tk()
        self.main_window.title("To-Do List")
        self.main_window.geometry("400x400")
        self.ti=[]
        self.top_frame=tk.Frame(self.main_window)
        self.top_frame.pack()
        self.lb1=tk.Label(self.top_frame,text="To-Do List",font=("Arial Bold",20))
        self.lb1.pack()
        self.t1_en_widget = tk.Entry(self.top_frame, width=20, validate="key", validatecommand=(self.main_window.register(self.validate_entry), '%P'))
        self.t1_en_widget.pack()
        self.add_b=tk.Button(self.top_frame,text="Add",command=self.add)
        self.add_b.pack()

        
        tk.mainloop() #entering mainloop(infinite loop)
        
    def add(self):
        a=self.t1_en_widget.get()
        checkbutton=tk.Checkbutton(self.top_frame,text=a,command=lambda: self.tog_c(checkbutton))
        checkbutton.pack(anchor="w")
        self.t1_en_widget.delete(0,tk.END)

    def validate_entry(self, new_text):
        if new_text.strip() == "":
            self.add_b.config(state=tk.DISABLED)
        else:
            self.add_b.config(state=tk.NORMAL)
        return True
    
    def tog_c(self,checkbutton):
        i = next((j for j in range(len(self.ti))
        if self.ti[i]["text"] == a["text"]), None)
todo=ToDo()



