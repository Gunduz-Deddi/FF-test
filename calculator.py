
from PySide6.QtWidgets import *
clicknumber=0
def btnclick():
    global clicknumber
    clicknumber+=1
    print(btn.clicked)
app=QApplication()
xPos=0
yPos=0
real=QMainWindow()
real.resize(600,600)
# ekranda gostermek ucun vtn "real" yeni pencereye uzerine elave edilmelidir
#btn.resize(100,100)
#btn.move(120,150)
btn=QPushButton("Real M",real)
btn.setGeometry(xPos,0,100,50)
btn.clicked.connect(btnclick)
xPos+=75
#btn01=QPushButton("2",real)
#btn01.setGeometry(xPos,0,100,50)
#xPos+=75
#btn02=QPushButton("3",real)
#btn02.setGeometry(xPos,0,100,50)
#xPos+=75
#btn03=QPushButton("4",real)
#btn03.setGeometry(xPos,0,100,50)
# tekrar olaraq buttonlari for dovr ile artiriq
for reqem in range(3):
    btn=QPushButton(str(reqem),real)
    btn.setGeometry(xPos,0,100,50)
    btn.clicked.connect(btnclick)
    xPos+=75
    btn.setStyleSheet("background:white; color:black; border:1px solid blue")
xPos=0
yPos+=75
for reqem in range(3,7):
    btn2=QPushButton(str(reqem),real)
    btn2.setGeometry(xPos,yPos,100,50)
    btn2.clicked.connect(btnclick)
    xPos+=75
    btn2.setStyleSheet("background:white; color:black; border:1px solid blue")
xPos=0
yPos+=75
for reqem in range(7,11):
    btn2=QPushButton(str(reqem),real)
    btn2.setGeometry(xPos,yPos,100,50)
    btn2.clicked.connect(btnclick)
    xPos+=75
    btn2.setStyleSheet("background:white; color:black; border:1px solid blue")
btn3=QPushButton("+",real)
btn3.setGeometry(350,0,100,50)
btn3.clicked.connect(btnclick)
xPos+=75
btn4=QPushButton("-",real)
btn4.setGeometry(xPos,75,100,50)
btn4.clicked.connect(btnclick)
xPos+=75
btn5=QPushButton("*",real)
btn5.setGeometry(xPos,75,100,50)
btn5.clicked.connect(btnclick)
xPos+=75



real.show()

app.exec_()
