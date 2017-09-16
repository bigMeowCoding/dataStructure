import re
n=input("len")
passwords=[]
i=0
result=[]
while i<int(n):
    password=input("password")
    passwords.append(password)
    i+=1
for pwd in passwords:
    if re.match("^\d",pwd):
        result.append(False)
    result.append(True)
    continue
# re.match()
print(passwords)
print(result)
# 小明同学最近开发了一个网站，在用户注册账户的时候，需要设置账户的密码。为了加强账户的安全性，小明对密码强度有一定要求：
# 1、密码只能由大写字母，小写字母，数字构成；
# 2、密码不能以数字开头；
# 3、密码中至少出现大写字母、小写字母和数字这三种字符类型中的两种；
# 4、密码长度至少为8。
# 现在小明收到了n个密码，他想请你写程序判断这些密码中哪些是合法的，哪些是不合法的。