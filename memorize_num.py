from time import time
from random import randint

print("桁数を入力してください")
digit_num = int(input())

num = []
for i in range(1, digit_num+1):
    num.append(str(randint(0, 9)))
    if i%5==0 and i%20!=0 and i<digit_num:
        num.append(" ")
    if i%20==0 and i<digit_num:
        num.append("\n")

with open("correct.txt", "w+") as f:
    correct = "".join(num)
    f.write(correct)

for i in range(len(num)):
    if num[i]=="\n":
        num[i] = " "
correct = "".join(num)

TIME = time()

print("半角スペース区切りで5桁ずつ出力してください")
ans = ""
while ans!=correct:
    ans = input()
    
print("%.2f 秒" % (time()-TIME))
