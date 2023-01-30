import shutil
import controller


def add_contact():
    number=controller.number
    title=controller.title
    contacts_txt=open('contact_list.txt', 'a', encoding='cp1251')
    contacts_txt.write(f'{number}:{title}\n')
    contacts_txt.close
def found_contact():
    global found_contacts
    title_import=str(controller.title)
    file=open("contact_list.txt", 'r', encoding='cp1251')
    contact_list=list(file.readlines())
    found_contacts=[]
    for i in contact_list:
        if title_import in i:
            found_contacts.append(i.split('\n'))
    file.close
found_contact
def export_txt(): 
    file1=open('contact_list.txt', 'a', encoding='cp1251')
    file2=open('Список контактов.txt', 'w')
    shutil.copyfile("contact_list.txt", "Список контактов.txt")
    file1.close
    file2.close
    return "экспортировано"
def export_csv(): 
    file_txt=open('contact_list.txt', 'a', encoding='cp1251')
    file_csv=open('Список контактов.csv', 'w')
    shutil.copyfile("contact_list.txt", "Список контактов.csv")
    file_txt.close
    file_csv.close
    return "экспортировано"