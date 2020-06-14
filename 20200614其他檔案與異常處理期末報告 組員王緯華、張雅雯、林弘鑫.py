#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#撰寫一個程式，以不定數迴圈輸入學生姓名，微積分與會計成績。當輸入學生姓名為none時，則結束輸入動作。並將上述輸入的資料寫入名為students.dat的檔案中。
outfile = open('students.dat','w') #'students.dat' 為檔名  W 指說是寫輸入進去
#write data to the file
while True:
  name = input()
  calculus = input()
  accounting = input()
  if name == 'none':
    break
  else:
    outfile.write(name)
    outfile.write(' ')
    outfile.write(calculus)
    outfile.write(' ')
    outfile.write(accounting)
    outfile.write(' ')
    outfile.write('\n')
outfile.close() #close 關閉檔案


# In[ ]:


#撰寫一程式，將綜合範例11所建立的students.dat檔案加以讀取之
infile = open('students.dat','r')

info = infile.readline() #r 為讀一行一行的方式
while info != '': #當info 不等於 空字串
  print(info) ) #執行這個
  info = infile.readline() #區間

infile.close()


# In[ ]:


#撰寫一程式，將宗和範力11所建立的students.dat檔案加以讀取之，並計算每位學生的平均分數。假設微積分的比重是60%，而會計的比重是40%。
infile = open('students.dat','r')

info = infile.readline()
while info != '':
  lst = info.split(' ')
  calculus = eval(lst[1])   #eval 叫 lst得物件,回傳他的值
  accounting = eval(lst[2])  #計算平均
  average = calculus * 0.6 + accounting * 0.4
  print('|%10s: %.2f|'%(lst[0], average)) #%s 為類似format的概念 將%帶換成後面的值   0.2為小數點後兩位
  info = infile.readline()#區間

infile.close()


# In[ ]:


###綜合範例１４：試撰寫一程式，將綜合範例１１所建立的 students.dat 檔案加以讀取之，看哪位學生的微積分最高

infile = open("students.dat", "r")

max = -1
info = infile.readline()
while info != "":
    lst = info.split(" ")
    calculus = eval(lst[1])
    if calculus > max:
        max = calculus
        name = lst[0]
    info = infile.readline()

print("#1 calculus score is {}： {}.".format(name, max))
infile.close()


# In[ ]:


###綜合範例１５：試撰寫一程式，將綜合範例１１所建立的 students.dat 檔案加以讀取之，看哪位學生的會計最低

infile = open("students.dat","r")

min = 101
info = infile.readline()
while info != "":
    lst = info.split(" ")
    accounting  =eval(lst[2])
    if accounting < min:
        min = accounting
        name = lst[0]
    info = infile.readline()

print("The lowest accounting score is\n          {}：    {}.".format(name, max))
infile.close()


# In[ ]:


#1.試撰寫一程式，要求使用者輸入五個好友的姓名、電話，以及出生年、月、日。並將它寫入名為friends.dat的檔案。
outfile=open('friends.dat','w')
for i in range(1,6):
  data=input()
  outfile.write(data)
  outfile.write('\n')

outfile.close()


# In[ ]:


# 2.試著撰寫一程式，以不定數迴圈輸入學生的姓名、python的分數，
#當姓名為none時，則結束輸入的動作，並將寫入各為scores.dat的檔案(至少輸入三位學生)
outfile=open('scores.dat','w')#以寫入模式開啟檔案
while True:#迴圈
  name=input() #輸入姓名
  score=input() #輸入成績
  if name=='none':#如果名字為none 就結束
    break
  else: #其他
    outfile.write(name) #內容都輸入進去
    outfile.write(' ')
    outfile.write(score)
    outfile.write('\n')#換行

outfile.close()  #關閉檔案


# In[ ]:


#3.試撰寫一程式，將習題1的friends.dat檔案開啟，檔案內容後加以印出
infile=open('friends.dat','r') #開啟檔案
for i in range(1,6): #迴圈
  info=infile.readline() #readline 該方法每次讀出一行內容
  print(info)
infile.close() #關閉檔案


# In[ ]:


#4.試撰寫一程式，將習題2的scores.dat檔案開啟，並讀出檔案內容加以印出
infile=open('scores.dat','r')
info=infile.readline()
while info !='': #當info不等於空集合，就可以執行
  print(info)
  info=infile.readline()

infile.close() #關閉檔案


# In[ ]:


#計算平均成績
infile=open('scores.dat','r')
count = 0 #總人數
tot = 0 #總分
info= infile.readline()
while info !='':
  lst = info.split(' ')#計算切片
  tot += eval(lst[1]) #eval() 函数用来執行一個字符串表達式，并返回表達式的值。
  count += 1
  info= infile.readline()

average = tot / count
print('average score : %.2f'%(average)) #小數點去到第二位
infile.close()


# In[1]:


#影片連結 請老師複製貼上連結即可觀看影片
#https://youtu.be/jiBbaYWBurg


# In[ ]:




