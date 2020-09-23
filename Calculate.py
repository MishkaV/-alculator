from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from mywindow import Ui_MainWindow

#Переменные
all_numbers = 0

#Создаем приложение
app = QtWidgets.QApplication(sys.argv)

#Создаем форму и выводим
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()


#Печать
#Конкатенация 
def multdig(n):
    num = ui.rezult_show.text()
    new_num = num + n
    ui.rezult_show.setText(new_num)



    
#Присвоим действия кнопкам
#Цифры
def pr0():
    multdig("0")
ui.pushButton_0.clicked.connect( pr0 )

def pr1():
    multdig("1")
ui.pushButton_1.clicked.connect( pr1 )

def pr2():
    multdig("2")
ui.pushButton_2.clicked.connect( pr2 )

def pr3():
    multdig("3")
ui.pushButton_3.clicked.connect( pr3 )

def pr4():
    multdig("4")
ui.pushButton_4.clicked.connect( pr4 )

def pr5():
    multdig("5")
ui.pushButton_5.clicked.connect( pr5 )

def pr6():
    multdig("6")
ui.pushButton_6.clicked.connect( pr6 )

def pr7():
    multdig("7")
ui.pushButton_7.clicked.connect( pr7 )

def pr8():
    multdig("8")
ui.pushButton_8.clicked.connect( pr8 )

def pr9():
    multdig("9")
ui.pushButton_9.clicked.connect( pr9 )

#Буквы
def prA():
    multdig("A")
ui.pushButton_A.clicked.connect( prA )

def prB():
    multdig("B")
ui.pushButton_B.clicked.connect( prB )

def prC():
    multdig("C")
ui.pushButton_C.clicked.connect( prC )

def prD():
    multdig("D")
ui.pushButton_D.clicked.connect( prD )

def prE():
    multdig("E")
ui.pushButton_E.clicked.connect( prE )

def prF():
    multdig("F")
ui.pushButton_F.clicked.connect( prF )

#Символы
def prDiv():
    #Проверка на символ
    check = ui.rezult_show.text()
    if not(check.endswith(" / ") or check.endswith(" * ") or check.endswith(" - ") or check.endswith(" + ")): 
        if not(check.endswith(" /") or check.endswith(" *") or check.endswith(" -") or check.endswith(" +")):
            multdig(" / ")
ui.pushButton_div.clicked.connect( prDiv )

def prMult():
    check = ui.rezult_show.text()
    if not(check.endswith(" / ") or check.endswith(" * ") or check.endswith(" - ") or check.endswith(" + ")):
        if not(check.endswith(" /") or check.endswith(" *") or check.endswith(" -") or check.endswith(" +")):
            multdig(" * ")
ui.pushButton_mult.clicked.connect( prMult )

def prMinus():
    check = ui.rezult_show.text()
    if not(check.endswith(" / ") or check.endswith(" * ") or check.endswith(" - ") or check.endswith(" + ")):
        if not(check.endswith(" /") or check.endswith(" *") or check.endswith(" -") or check.endswith(" +")):
            multdig(" - ")
ui.pushButton_minus.clicked.connect( prMinus )

def prPlus():
    check = ui.rezult_show.text()
    if not(check.endswith(" / ") or check.endswith(" * ") or check.endswith(" - ") or check.endswith(" + ")):
        if not(check.endswith(" /") or check.endswith(" *") or check.endswith(" -") or check.endswith(" +")):
            multdig(" + ")
ui.pushButton_plus.clicked.connect( prPlus )

    


def prBracketLeft():
    multdig(" ( ")
ui.pushButton_BracketRight.clicked.connect( prBracketLeft )

def prBracketRight():
    multdig(" ) ")
ui.pushButton_BracketLeft.clicked.connect( prBracketRight )



#Логика
def brackets():
    #Проверим скобки
    st = ui.rezult_show.text()
    flag = True
    brclose = 0 #кол-во открытых
    bropen = 0 #кол-во закрытых
    i = 0
    while (flag == True) and (i <= len(st)):
        if st[i] == '(' :
            bropen += 1
        if st[i] == ')' :
            brclose += 1
        if brclose > bropen:
            flag = False
        if (st[i] == '(') and (st[i+3] == ')'):
            flag = False
        i += 1
        
    if (flag == True) and (bropen == brclose):
        return True
    else:
        return False


def prEqual():
    #Проверка скобок
    if brackets() == False:
       ui.rezult_show.setText("Ошибка ввода!")


    
    
       
ui.pushButton_equal.clicked.connect( prEqual )    




#Удаление
#Один символ
def delete():
    num = ui.rezult_show.text()
    new_num = num[:-1]
    ui.rezult_show.setText(new_num)
ui.pushButton_del.clicked.connect( delete )

#Удалить всё
def clear():
    ui.rezult_show.clear()
    all_numbers = 0
ui.pushButton_clear.clicked.connect( clear )


 

    
#Закрываем
sys.exit(app.exec_())
