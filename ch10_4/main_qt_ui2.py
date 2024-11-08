from win_ui import Ui_MainWindow
from PySide6.QtWidgets import QApplication, QMainWindow,QTableWidgetItem,QHeaderView
from CustomerDAO import CustomerDAO

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self,dao):
        super(MainWindow, self).__init__()
        self.dao = dao
        self.setupUi(self)
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setHorizontalHeaderLabels(['Id','FirstName',"LastName","Email"])
        
        header = self.tableWidget.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.Stretch)
        
        self.tableWidget.verticalHeader().setVisible(False)
        self.pushButton.clicked.connect(self.load_data)
        # self.load_data()

    
    def load_data(self):
        customers = list(self.dao.find_all())
        self.tableWidget.setRowCount(len(customers))
        
        for line,customer in enumerate(customers):
            self.tableWidget.setItem(line,0,QTableWidgetItem(str(customer.id)))
            self.tableWidget.setItem(line,1,QTableWidgetItem(customer.first_name))
            self.tableWidget.setItem(line,2,QTableWidgetItem(customer.last_name))
            self.tableWidget.setItem(line,3,QTableWidgetItem(customer.email))

def main():
    dao = CustomerDAO(r'..\customers_db.db')
    
    app = QApplication([])
    window = MainWindow(dao)
    window.show()
    app.exec()
if __name__ == '__main__':
    main()
