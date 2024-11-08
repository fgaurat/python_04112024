import sys
from tkinter import *
from tkinter import ttk
from CustomerDAO import CustomerDAO


def main():

    ws = Tk()
    ws.title('PythonGuides')
    ws.geometry('800x600')
    # ws['bg']='#fb0'

    tv = ttk.Treeview(ws,show="headings")
    tv['columns'] = ('Id', 'Name', 'Firstname')

    tv.column('Id', anchor=CENTER, width=80)
    tv.column('Name', anchor=CENTER, width=80)
    tv.column('Firstname', anchor=CENTER, width=80)

    tv.heading('Id', text='Id', anchor=CENTER)
    tv.heading('Name', text='Name', anchor=CENTER)
    tv.heading('Firstname', text='Firstname', anchor=CENTER)

    dao = CustomerDAO(r'..\customers_db.db')
    customers = dao.find_all()
    for customer in customers:
        tv.insert(parent='', index=customer.id, iid=customer.id,  values=(
            customer.id, customer.last_name, customer.first_name))

    tv.pack(fill=BOTH,expand=True)

    ws.mainloop()


if __name__ == '__main__':
    main()
