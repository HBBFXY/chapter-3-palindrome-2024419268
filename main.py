def is_palindrome():
   num=input("请输入一个五位数: ")
   if len(num)!=5 or not num.isdigit():
      print("输入错误，请确保输入的是一个五位数!")
      return
   if num==num[::-1]:
      print(f"{num}是一个回文数")
   else:
      print(f"{num}不是一个回文数")
if__name__=="__main__":
   is_palindrome()
