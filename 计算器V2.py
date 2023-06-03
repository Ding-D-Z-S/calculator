import tkinter as tk

def add(x, y):
    """加法运算"""
    return x + y

def subtract(x, y):
    """减法运算"""
    return x - y

def multiply(x, y):
    """乘法运算"""
    return x * y

def divide(x, y):
    """除法运算"""
    return x / y

def convert_decimal():
    """将十进制数转换为其他进制"""
    decimal_num = int(num_entry.get())
    conversion_type = choice_var.get()

    if conversion_type == 1:
        converted_num = oct(decimal_num)[2:]  # 十进制转八进制
        conversion_label.configure(text="十进制数 {} 的八进制为：{}".format(decimal_num, converted_num))
    elif conversion_type == 2:
        converted_num = hex(decimal_num)[2:]  # 十进制转十六进制
        conversion_label.configure(text="十进制数 {} 的十六进制为：{}".format(decimal_num, converted_num))
    elif conversion_type == 3:
        converted_num = bin(decimal_num)[2:]  # 十进制转二进制
        conversion_label.configure(text="十进制数 {} 的二进制为：{}".format(decimal_num, converted_num))
    else:
        conversion_label.configure(text="无效的转换类型")

def calculate():
    """执行选择的运算并显示结果"""
    operation_choice = operation_choice_var.get()
    if operation_choice == 1:
        result = add(float(num1_entry.get()), float(num2_entry.get()))
        result_label.configure(text="结果：" + str(result))
    elif operation_choice == 2:
        result = subtract(float(num1_entry.get()), float(num2_entry.get()))
        result_label.configure(text="结果：" + str(result))
    elif operation_choice == 3:
        result = multiply(float(num1_entry.get()), float(num2_entry.get()))
        result_label.configure(text="结果：" + str(result))
    elif operation_choice == 4:
        result = divide(float(num1_entry.get()), float(num2_entry.get()))
        result_label.configure(text="结果：" + str(result))
    else:
        result_label.configure(text="无效的操作选择")

# 创建主窗口
window = tk.Tk()
window.title("计算器")
window.geometry("600x350")

# 创建选择标签和单选按钮（操作选择）
operation_choice_label = tk.Label(window, text="选择运算：")
operation_choice_label.grid(row=0, column=0, sticky="w")

operation_choice_var = tk.IntVar()

addition_radio = tk.Radiobutton(window, text="加法", variable=operation_choice_var, value=1)
addition_radio.grid(row=1, column=0, sticky="w")

subtraction_radio = tk.Radiobutton(window, text="减法", variable=operation_choice_var, value=2)
subtraction_radio.grid(row=2, column=0, sticky="w")

multiplication_radio = tk.Radiobutton(window, text="乘法", variable=operation_choice_var, value=3)
multiplication_radio.grid(row=3, column=0, sticky="w")

division_radio = tk.Radiobutton(window, text="除法", variable=operation_choice_var, value=4)
division_radio.grid(row=4, column=0, sticky="w")

# 创建输入标签和输入框
num1_label = tk.Label(window, text="输入第一个数字：")
num1_label.grid(row=0, column=1, sticky="e")

num1_entry = tk.Entry(window)
num1_entry.grid(row=1, column=1, sticky="e")

num2_label = tk.Label(window, text="输入第二个数字：")
num2_label.grid(row=2, column=1, sticky="e")

num2_entry = tk.Entry(window)
num2_entry.grid(row=3, column=1, sticky="e")

# 创建计算按钮
calculate_button = tk.Button(window, text="计算", command=calculate)
calculate_button.grid(row=4, column=1, sticky="e")

# 创建结果标签
result_label = tk.Label(window, text="结果：")
result_label.grid(row=5, column=0, sticky="w")

# 创建十进制转换标签和单选按钮（转换选择）
conversion_choice_label = tk.Label(window, text="选择转换类型：")
conversion_choice_label.grid(row=6, column=0, sticky="w")

choice_var = tk.IntVar()

decimal_to_octal_radio = tk.Radiobutton(window, text="十进制转八进制", variable=choice_var, value=1)
decimal_to_octal_radio.grid(row=7, column=0, sticky="w")

decimal_to_hex_radio = tk.Radiobutton(window, text="十进制转十六进制", variable=choice_var, value=2)
decimal_to_hex_radio.grid(row=8, column=0, sticky="w")

decimal_to_binary_radio = tk.Radiobutton(window, text="十进制转二进制", variable=choice_var, value=3)
decimal_to_binary_radio.grid(row=9, column=0, sticky="w")

# 创建十进制转换输入标签和输入框
num_label = tk.Label(window, text="输入十进制数：")
num_label.grid(row=6, column=1, sticky="e")

num_entry = tk.Entry(window)
num_entry.grid(row=7, column=1, sticky="e")

# 创建十进制转换按钮
convert_button = tk.Button(window, text="转换", command=convert_decimal)
convert_button.grid(row=8, column=1, sticky="e")

# 创建转换结果标签
conversion_label = tk.Label(window, text="")
conversion_label.grid(row=9, column=1, sticky="w")

# 创建窗口大小输出标签
window_size_label = tk.Label(window, text="窗口大小：")
window_size_label.grid(row=10, column=0, sticky="w")

def update_window_size(event):
    width = window.winfo_width()
    height = window.winfo_height()
    window_size_label.configure(text="窗口大小：{} x {}".format(width, height))

# 监听窗口大小变化事件
window.bind("<Configure>", update_window_size)

# 启动GUI事件循环
window.mainloop()
