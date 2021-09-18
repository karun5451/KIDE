from tkinter import *
from tkinter.filedialog import asksaveasfilename, askopenfilename
import subprocess

KIDE_App = Tk()
KIDE_App.title('KIDE')

icon = PhotoImage(file='KIDE_logo_design_V1.png')
file_path = ''

def set_file_path(path):
    global file_path
    file_path = path

def open_file():
    path = askopenfilename(filetypes=[('Python Files', '*.py')])
    with open(path, 'r') as file:
        code = file.read()
        editor.delete('1.0', END)
        editor.insert('1.0', code)
        set_file_path(path)


def save_as():
    if file_path == '':
        path = asksaveasfilename(filetypes=[('Python Files', '*.py')])
    else:
        path = file_path
    with open(path, 'w') as file:
        code = editor.get('1.0', END)
        file.write(code)
        set_file_path(path)


def run():
    if file_path == '':
        save_prompt = Toplevel()
        text = Label(save_prompt, text='Please save your code')
        text.pack()
        return
    command = f'python {file_path}'
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    output, error = process.communicate()
    code_output.insert('1.0', output)
    code_output.insert('1.0',  error)

def Board_Manager():
    return True
def set_txt_Color():
    return True
def set_BG_color():
    return True

menu_bar = Menu(KIDE_App)

file_menu = Menu(menu_bar, tearoff=False, background='skyblue', fg='Black')
tool_menu = Menu(menu_bar, tearoff=False, background='skyBlue', fg='black')
preferences_menu = Menu(menu_bar, tearoff=False, background='skyBlue', fg='Black')
file_menu.add_command(label='Open', command=open_file)
file_menu.add_command(label='Save', command=save_as)
file_menu.add_command(label='Save As', command=save_as)
file_menu.add_command(label='Exit', command=exit)
tool_menu.add_command(label='Board Manager', command=Board_Manager)
preferences_menu.add_command(label='Change Text color', command=set_txt_Color)
preferences_menu.add_command(label=' Change BackGround color', command=set_BG_color)
menu_bar.add_cascade(label='File', menu=file_menu)
menu_bar.add_cascade(label='Preferences', menu=preferences_menu)
menu_bar.add_cascade(label='Tools',menu=tool_menu)
run_bar = Menu(menu_bar, tearoff=False, background='green', fg='white')
run_bar.add_command(label='Run', command=run)
menu_bar.add_cascade(label='Run', menu=run_bar)

KIDE_App.config(menu=menu_bar)
KIDE_App.configure(background='Black')
KIDE_App.iconphoto(False,icon)

editor = Text()
editor.pack()

code_output = Text(height=10)
code_output.pack()

KIDE_App.mainloop()

