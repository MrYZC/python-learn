from openpyxl import Workbook
import os
wb = Workbook()
desk_filename = "成绩.xlsx"
ws1 = wb.active
ws1.title = "成绩"
fr = open('C:/Users/11725/Desktop/score.text','r')
#dic = {}
name = []
score= []
for line in fr:
    v = line.strip().split(':')
    name.append(v[0])
    score.append(v[1])
#A1 = "A1" #'A%s' % (1) 
#B1 = "B1" #'B%s' % (1)
ws1['A1'] = "姓名"
ws1['B1'] = "分数"
# for i in name:
# 	col_A = 'A%s' % (name.index(i)+2)
# 	ws1[col_A] = i
# for m in score:
# 	col_B = 'B%s' % (score.index(m)+2)
# 	ws1[col_B] = m
for (i,m) in zip(name,score):
    col_A = 'A%s' % (name.index(i) + 2)
    col_B = 'B%s' % (name.index(i) + 2)
    ws1[col_A] = i
    ws1[col_B] = m
#     #dic[v[0]] = v[1]
fr.close()
if not os.path.exists('C:/Users/11725/Desktop/'+desk_filename):
	wb.save(filename=desk_filename)

# tuple1= json.load(json1)
# print(tuple1)