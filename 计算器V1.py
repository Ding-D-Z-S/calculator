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

print("选择运算：")
print("1、加法")
print("2、减法")
print("3、乘法")
print("4、除法")

# 获取用户输入
choice = input("输入您的选择（1/2/3/4）:")

num1 = float(input("输入第一个数字："))
num2 = float(input("输入第二个数字："))

if choice == '1':
    print(num1, "+", num2, "=", add(num1, num2))

elif choice == '2':
    print(num1, "-", num2, "=", subtract(num1, num2))

elif choice == '3':
    print(num1, "*", num2, "=", multiply(num1, num2))

elif choice == '4':
    print(num1, "/", num2, "=", divide(num1, num2))

else:
    print("无效的输入")
