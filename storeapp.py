
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *
import sqlite3

    
app=QApplication

class Store(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(600,600)
        self.storeTitle=QLabel("Product list",self)
        self.storeTitle.setGeometry(25,25,550,30)
        self.productlist=QTextBrowser(self)
        self.productlist.setGeometry(20,20,550,450)
        self.productlist.setText(self.getProductList())
        self.chooseProduct=QLineEdit("",self)
        self.chooseProduct.setGeometry(25,500,200,30)
        self.order=QPushButton("",self)
        self.order.setGeometry(25,500,200,30)
        self.order.clicked.connect(self.orderProduct)
        
    def orderProduct(self):
        connection=sqlite3.connect("store.db")
        cursor=connection.cursor()
        query=f"insert into Orders(ProductID,CustomerID) values({int(self.chooseProduct.text())},1)"
        cursor.execute(query)
        connection.commit()
        
    def getProductList(self):
        lst=""
        connection=sqlite3.connect("store.db")
        cursor=connection.cursor()
        query=f"select * from product"
        products=cursor.execute(query)
        for product in products:
            lst+=f"{product[0]}.{product[1]} | {product[2]}  AZN \n"
        return lst
        
        
        
class login(Qwidget):
    def __init__(self):
        super().__init__()
        self.currentwindow=None
        self.resize(300,155)
        self.email=QLineEdit("email",self)
        self.email.setGeometry(50,25,200,30)
        self.password=QLineEdit("email",self)
        self.password.setGeometry(50,75,200,30)
        self.loginBtn=QPushButton("login",self)
        self.loginBtn.setGeometry(50,25,200,30)
        self.loginBtn.clicked.connect(self.LoginCustomer)
        
    def LoginCustomer(self):
        email=self.email.text()
        password=self.password.text()
        connection=sqlite3.connect("store.db")
        cursor=connection.cursor()
        query=f""" 
        select count(*),password customer where email="{email}"
        """
        data=cursor.execute(query)
        connection.commit()
        
        for d in data:
            print(d[0],d[1])
            if d[0]==1:
                if d[1]==password:
                    self.currentwindow=Store()
                    self.currentwindow.show()
                else:
                    self.currentwindow=Register()
                    self.currentwindow.show()
                    
                
        
                    
        
        
    
    
    
    
store=Main()
store.show()
app.exec_()

