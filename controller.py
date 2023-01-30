
from tkinter import*
import model

def found_contact():
    model.found_contact()
    Label(window, text=f"{model.found_contacts}").grid(row=9, column=0, stick='w')
def add_data():
    global number
    number=contact_number.get() 
    global title
    title=contact_title.get()
    model.add_contact()
    Label(window, text=f"Контакт {title}:{number} добавлен").grid(row=8, column=0, stick='w')
def export_csv():
    model.export_csv()
    Label(window, text=f"Контакты экспортированы в CSV").grid(row=8, column=0, stick='w')
def export_txt():
    model.export_txt()
    Label(window, text=f"Контакты экспортированы в TXT").grid(row=8, column=0, stick='w')
def start():
    global window
    global contact_number
    global contact_title
    window = Tk()
    window.grid()
    window.title("Phone list")
    window['bg']='white'
    window.geometry('400x400+200+300')
    window.resizable(False, True)
    button_add_contact=Button(window, width=30, height=5, text='Добавить номер', command=add_data)
    button_add_contact.grid(row=0, column=0)
    button_find_contact=Button(window, width=30, height=5, text='Найти номер', command=found_contact)
    button_find_contact.grid(row=1, column=0)
    button_export_csv=Button(window, width=30, height=5, text='Экспортировать CSV', command=export_csv)
    button_export_csv.grid(row=0, column=1)
    button_export_txt=Button(window, width=30, height=5, text='Экспортировать TXT', command=export_txt)
    button_export_txt.grid(row=1, column=1)
    Label(window, text="Имя контакта").grid(row=5, column=0, stick='w')
    contact_title=Entry(window)
    contact_title.grid(row=5, column=1, stick='w')
    Label(window, text="Номер телефона").grid(row=4, column=0, stick='w')
    contact_number=Entry(window)
    contact_number.grid(row=4, column=1, stick='w')
    window.mainloop()

