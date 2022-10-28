from tkinter import *
from tkinter import filedialog
import tkinter.scrolledtext as scrolledtext
import webbrowser

root = Tk()
root.geometry("800x600")
root.resizable(0,0)
root.title("T-replace")
root['bg']='#243665'

output_file = open('output.txt', 'w', encoding='utf-8')
output_file.write('')
output_file.close()

english_minor_alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
english_major_alpha = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
chars = ['!', '@', '#', '$', '%', '^', '&', '*', '/', '\\', '<', '>', '?', '|']

def openFile():
    tf = filedialog.askopenfilename(initialdir="C:/Users/MainFrame/Desktop/", title="باز کردن فایل متنی", filetypes=(("Text Files", "*.txt"),))
    tf = open(tf, encoding='utf-8')
    data = tf.read()
    txtarea.insert(END, data)
    tf.close()


def eng_rem():
    output_file = open('output.txt', 'r', encoding='utf-8')
    data = output_file.read()
    if data:
        output = data
        output_file.close()
        for i in english_minor_alpha:
            try:
                output = output.replace(i, '')
            except:
                pass
        
        for i in english_major_alpha:
            try:
                output = output.replace(i, '')
            except:
                pass

        output_file = open('output.txt', 'w', encoding='utf-8')
        output_file.write(str(output))
        output_file.close()

        resarea.delete(1.0, END)
        resarea.insert(1.0, output)

    elif txtarea.get("1.0","end"):
        output = txtarea.get("1.0","end")
        for i in english_minor_alpha:
            try:
                output = output.replace(i, '')
            except:
                pass
        
        for i in english_major_alpha:
            try:
                output = output.replace(i, '')
            except:
                pass

        output_file = open('output.txt', 'w', encoding='utf-8')
        output_file.write(str(output))
        output_file.close()

        resarea.insert(1.0, output)


def import_urep():
    output_file = open('output.txt', 'r', encoding='utf-8')
    data = output_file.read()
    if data:
        output = data
        output_file.close()
        if rep_old.get():
            if rep_new.get():
                olds = []
                news = []
                for i in rep_old.get().split(' '):
                    olds.append(i)
                for i in rep_new.get().split(' '):
                    news.append(i)
                n = 0
                while n < len(olds):
                    output = output.replace(olds[n], news[n])
                    n += 1

                output_file = open('output.txt', 'w', encoding='utf-8')
                output_file.write(str(output))
                output_file.close()
                resarea.delete(1.0, END)
                resarea.insert(1.0, output)

            else:
                olds = []
                for i in rep_old.get().split(' '):
                    olds.append(i)
                for i in olds:
                    output = output.replace(i, '')
                
                output_file = open('output.txt', 'w', encoding='utf-8')
                output_file.write(str(output))
                output_file.close()
                resarea.delete(1.0, END)
                resarea.insert(1.0, output)

    elif txtarea.get(1.0, END):
        output = txtarea.get(1.0, END)
        if rep_old.get():
            if rep_new.get():
                olds = []
                news = []
                for i in rep_old.get().split(' '):
                    olds.append(i)
                for i in rep_new.get().split(' '):
                    news.append(i)
                
                n = 0
                while n < len(olds):
                    output = output.replace(olds[n], news[n])
                    n += 1

                output_file = open('output.txt', 'w', encoding='utf-8')
                output_file.write(str(output))
                output_file.close()
                resarea.insert(1.0, output)

            else:
                olds = []
                for i in rep_old.get().split(' '):
                    olds.append(i)
                
                for i in olds:
                    output = output.replace(i, '')
                
                output_file = open('output.txt', 'w', encoding='utf-8')
                output_file.write(str(output))
                output_file.close()
                resarea.insert(1.0, output)


def num_rem():
    output_file = open('output.txt', 'r', encoding='utf-8')
    data = output_file.read()
    if data:
        output = data
        output_file.close()
        for i in numbers:
            try:
                output = output.replace(i, '')
            except:
                pass
        
        output_file = open('output.txt', 'w', encoding='utf-8')
        output_file.write(str(output))
        output_file.close()

        resarea.delete(1.0, END)
        resarea.insert(1.0, output)

    elif txtarea.get(1.0, END):
        output = txtarea.get(1.0, END)
        for i in numbers:
            try:
                output = output.replace(i, '')
            except:
                pass
        
        output_file = open('output.txt', 'w', encoding='utf-8')
        output_file.write(str(output))
        output_file.close()

        resarea.insert(1.0, output)


def char_rem():
    output_file = open('output.txt', 'r', encoding='utf-8')
    data = output_file.read()
    if data:
        output = data
        output_file.close()
        for i in chars:
            try:
                output = output.replace(i, '')
            except:
                pass
        
        output_file = open('output.txt', 'w', encoding='utf-8')
        output_file.write(str(output))
        output_file.close()

        resarea.delete(1.0, END)
        resarea.insert(1.0, output)

    elif txtarea.get(1.0, END):
        output = txtarea.get(1.0, END)
        for i in chars:
            try:
                output = output.replace(i, '')
            except:
                pass
        
        output_file = open('output.txt', 'w', encoding='utf-8')
        output_file.write(str(output))
        output_file.close()

        resarea.insert(1.0, output)


def export():
    tf = filedialog.asksaveasfilename(initialdir="C:/Users/MainFrame/Desktop/", title="ذخیره خروجی", filetypes=(("Text files", "*.txt"), ))
    file_name = tf + '.txt'
    res_file = open(file_name, 'w', encoding="utf-8")
    res_file.write(resarea.get("1.0","end"))
    res_file.close()


def reset_fields():
    resarea.delete("1.0","end")
    txtarea.delete("1.0","end")
    output_file = open('output.txt', 'w', encoding='utf-8')
    output_file.write('')
    output_file.close()


def callback(url):
   webbrowser.open_new_tab(url)


resarea = scrolledtext.ScrolledText(root, font=("Vazir", 10))
resarea.place(x=10, y=10, width=380, height=390)

txtarea = scrolledtext.ScrolledText(root, font=("Vazir", 10))
txtarea.place(x=410, y=10, width=380, height=390)

Button(root, text="دریافت خروجی", font=("Vazir", 10), command=export).place(x=110, y=420, width=180, height=30)
Button(root, text="ریست", font=("Vazir", 10), command=reset_fields).place(x=375, y=405, width=50, height=30)
Button(root, text="وارد کردن فایل", font=("Vazir", 10), command=openFile).place(x=510, y=420, width=180, height=30)


Button(root, text="حذف کلمات انگلیسی", font=("Vazir", 10), command=eng_rem).place(x=110, y=460, width=180, height=30)
Button(root, text="حذف کاراکتر ها", font=("Vazir", 10), command=char_rem).place(x=310, y=460, width=180, height=30)
Button(root, text="حذف اعداد", font=("Vazir", 10), command=num_rem).place(x=510, y=460, width=180, height=30)


rep_new = Entry(root, font=("Vazir", 10))
rep_new.place(x=110, y=500, width=180, height=30)
Label(root, text="به (با فاصله جدا شود)", font=("Vazir", 8), fg="#fff", bg='#243665').place(x=110, y=540, width=180, height=20)

Button(root, text="تبدیل", font=("Vazir", 10), command=import_urep).place(x=310, y=500, width=180, height=30)

rep_old = Entry(root, font=("Vazir", 10))
rep_old.place(x=510, y=500, width=180, height=30)
Label(root, text="از (با فاصله جدا شود)", font=("Vazir", 8), fg="#fff", bg='#243665').place(x=510, y=540, width=180, height=20)

link = Label(root, text="Alien Max", font=("Vazir", 8), bg='#243665', cursor="hand2")
link.place(x=370, y=575)
link.bind("<Button-1>", lambda e: callback("https://github.com/alien-max"))

root.mainloop()