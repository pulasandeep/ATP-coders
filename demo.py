#importing openpyxl alias xl to the demo program
import openpyxl as xl
#decleration of excel file if you saved excel file in other location specify path here
wb=xl.load_workbook('Book1.xlsx')
#assign excel file to sheet jeyword
sheet=wb['Book1']
#take input from console
s = input("enter what you want to search:  ")
print(f'{s} >>>')
#split the entered input to word by word
s=s.split()
# iteration starts for searching the keyword
i=int(0)
while i<len(s):
    key = s[i]
    if key == sheet['a1'].value or key == 'oops' or key == 'java':
       cell=sheet['b1']
       print(cell.value)
    if key == 'attributes' or key == 'encapsulation' or key == 'polymorphism' or key == 'inheritance':
        cell=sheet['b2']
        print(cell.value)
    if key == sheet['a3'].value or key == 'program':
        cell=sheet['b3']
        print(cell.value)
    if key == sheet['a4'].value or key == 'identifiers':
        cell=sheet['b4']
        print(cell.value)
    if key == sheet['a5'].value or key == 'keywords':
        cell=sheet['b5']
        print(cell.value)
    if key == sheet['a6'].value or key == 'operators':
        cell=sheet['b6']
        print(cell.value)
    if key == sheet['a7'].value:
        cell=sheet['b7']
        print(cell.value)
    if key == sheet['a8'].value:
        cell=sheet['b8']
        print(cell.value)
    if key == sheet['a9'].value:
        cell=sheet['b9']
        print(cell.value)
    if key == sheet['a10'].value:
        cell=sheet['b10']
        print(cell.value)
    if key == sheet['a11'].value:
        cell=sheet['b11']
        print(cell.value)
    if key == sheet['a12'].value:
        cell=sheet['b12']
        print(cell.value)
    if key == sheet['a13'].value:
        cell=sheet['b13']
        print(cell.value)
    if key == sheet['a14'].value or key == 'conditional':
        cell=sheet['b14']
        print(cell.value)
    if key == sheet['a15'].value:
        cell=sheet['b15']
        print(cell.value)
    if key == sheet['a16'].value:
        cell=sheet['b16']
        print(cell.value)
    if key == sheet['a17'].value:
        cell=sheet['b17']
        print(cell.value)
    if key == sheet['a18'].value:
        cell=sheet['a18']
        print(cell.value)
    if key == sheet['a19'].value:
        cell=sheet['b19']
        print(cell.value)
    if key == sheet['a20'].value or key == 'datatypes':
        cell=sheet['b20']
        print(cell.value)
    if key == sheet['a21'].value:
        cell=sheet['b21']
        print(cell.value)
    if key == sheet['a22'].value or key == 'strings':
        cell=sheet['b22']
        print(cell.value)
    if key == sheet['a23'].value:
        cell=sheet['b23']
        print(cell.value)

    i=i+1

#end of the program
