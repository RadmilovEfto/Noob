import tkinter as tk

window = tk.Tk()
window.geometry('1024x720')
window.title('Lista Proizvoda')

def show_item_info(event) :
    print('Hello World')

product_list=('Apple', 'Bannana','Cherry','Date','Elderberry')

listbox = tk.Listbox(window, height=50)
listbox.pack(side='left', padx=10)

for item in product_list :
    listbox.insert(tk.END, item)

listbox.bind('<<ListboxSelect>>', show_item_info)

product_info = tk.Text(window, width=50, height=50, font=('Arial', 14))
product_info.pack(side="left")

window.mainloop()
