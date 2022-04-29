from tkinter import *

def clear_textbox():
    text_box.delete('1.0', 'end')


root = Tk()
root.title('PythonGuides')
root.geometry('2000x1000')
root.config(bg='#84BF04')

my_entries = []
message ='''
Write you text here '''

text_box = Text(
                root,
                height=2,
                width=80,
                font= ('Arial', 16, 'bold')
)

def something():
    entry_list = ''

    for entries in my_entries:
        entry_list = entry_list + str(entries.get()) + '\n'
        my_label.config(text=entry_list)
    # print(my_entries[1].get())

for x in range(1):
    my_entry = Entry(root)
    my_entry.grid(row=0, column=x, pady=20, padx=50)
    my_entries.append(my_entry)

my_button = Button(root,
                    text="Click Me!",
                    command = something,
                    width = 15,
                    height = 2
                        ).pack(
                                expand=True)

my_button.grid(row=1, column=0, pady=20)
my_label = Label(root, text='')
my_label.grid(row=2, column=0, pady=20)

# text_box.pack(expand=True)
# text_box.insert('end', message)

root.mainloop()
