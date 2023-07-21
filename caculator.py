import tkinter as tk

# 定义字体大小
font_size = 20

# 定义计算函数，用于计算表达式的值
def calculate():
    try:
        # 尝试评估表达式
        result = eval(entry.get())
        # 将结果显示在输入框中
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except:
        # 如果表达式无效，显示错误信息
        entry.delete(0, tk.END)
        entry.insert(tk.END, "输入无效")

# 定义输入函数，用于处理按钮输入
def input_char(char):
    if char == 'C':
        # 如果输入的是"C"，清空输入框
        entry.delete(0, tk.END)
    else:
        # 否则，将字符插入到输入框
        entry.insert(tk.END, char)

# 创建窗口
window = tk.Tk()
window.title("简单计算器")

# 设置窗口大小
window.geometry('300x400')

# 将窗口居中显示
window_width = window.winfo_reqwidth()
window_height = window.winfo_reqheight()
position_right = int(window.winfo_screenwidth()/2 - window_width/2)
position_down = int(window.winfo_screenheight()/2 - window_height/2)
window.geometry("+{}+{}".format(position_right, position_down))

# 创建输入框
entry = tk.Entry(window, font=("Helvetica", font_size))
entry.grid(row=0, column=0, columnspan=4, sticky="nsew")

# 定义按钮字符，把 'C' 和运算符放在一起
button_chars = [
    '7', '8', '9', 'C',
    '4', '5', '6', '+',
    '1', '2', '3', '-',
    '0', '.', '*', '/',
]

# 创建按钮
buttons = [
    tk.Button(window, text=char, font=("Helvetica", font_size), command=lambda char=char: input_char(char))
    for char in button_chars
]

# 将按钮添加到窗口
for i, button in enumerate(buttons):
    button.grid(row=i//4+1, column=i%4, sticky="nsew")

# 创建"等于"按钮，用于计算结果
equal_button = tk.Button(window, text='=', font=("Helvetica", font_size), command=calculate)
equal_button.grid(row=5, column=0, columnspan=4, sticky="nsew")

# 配置行和列的权重，确保按钮可以随窗口大小改变
for i in range(6):
    window.grid_rowconfigure(i, weight=1)
for i in range(4):
    window.grid_columnconfigure(i, weight=1)

# 启动主循环
window.mainloop()
