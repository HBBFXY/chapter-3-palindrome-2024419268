sum=input("请输入一个五位数:")
if len(num)!=5 or ont num.isdigit():
   print("输入错误，请输入一个五位数。")
else:
    reversed_num=num[::-1]
    if num==reversed_num:
        print(f"{num}是回文数。")
    else:
        print(f"{num}不是回文数。")

