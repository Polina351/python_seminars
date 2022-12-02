import tkinter as tk

def new_contact():
    frst_name = first_name.get()
    lst_name = last_name.get()
    tlphone = telephone.get()
    with open('telephone_numbers.txt', 'a', encoding='utf-8') as data:
        data.write(f'{frst_name} {lst_name}: {tlphone}\n')
    first_name.delete(0, tk.END)
    last_name.delete(0, tk.END)
    telephone.delete(0, tk.END)

def print_contacts():
    try:
        with open('telephone_numbers.txt', 'r', encoding='utf-8') as data:
            for contact in data.readlines():
                contacts.insert(tk.END, contact)
    except FileNotFoundError:
        print('Файл не найден')

def clear_list():
    contacts.delete(0, 50)

def cerch():
    un_row = under_row.get()
    with open('telephone_numbers.txt', 'r', encoding='utf-8') as data:
            for contact in data.readlines():
                if un_row in contact:
                    contacts.insert(tk.END, contact)
    under_row.delete(0, tk.END)


root = tk.Tk()
root.title('Телефонный справочник')
root.geometry('700x500')

tk.Label(root, text='Имя').grid(row=0, column=0)
first_name = tk.Entry(root)
first_name.grid(row=0, column=1)

tk.Label(root, text='Фамилия').grid(row=1, column=0)
last_name = tk.Entry(root)
last_name.grid(row=1, column=1)

tk.Label(root, text='Поиск').grid(row=0, column=2)
under_row = tk.Entry(root)
under_row.grid(row=1, column=2)

tk.Label(root, text='Номер телефона').grid(row=2, column=0)
telephone = tk.Entry(root)
telephone.grid(row=2, column=1)

contacts = tk.Listbox(root, height=15, width=50)
contacts.grid(row=4, column=2)

tk.Button(root, text='Создать контакт', command=new_contact).grid(row=3, column=1)
tk.Button(root, text='Показать все контакты', command=print_contacts).grid(row=3, column=2)
tk.Button(root, text='Очистить', command=clear_list, justify=tk.RIGHT).grid(row=3, column=3)
tk.Button(root, text='Найти', command=cerch).grid(row=1, column=3)

root.mainloop()