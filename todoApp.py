import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import sqlite3

# creating the database or connect to db with the name.
connection = sqlite3.connect('todolist.db')
# create a cursor
c = connection.cursor()

# Create a tabel
c.execute("""CREATE TABLE if not exists todo_list(
    list_item text)
    """)

# Commit the changes
connection.commit()

# Close our connection
connection.close()

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(700, 432)
        MainWindow.setMaximumSize(700, 432)
        MainWindow.setWindowIcon(QtGui.QIcon('todo.png'))
        MainWindow.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.468, y1:0.154, x2:0.521053, y2:1, stop:0 rgba(117, 0, 176, 255), stop:1 rgba(175, 100, 204, 255));\n")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Greetings = QtWidgets.QLabel(self.centralwidget)
        self.Greetings.setGeometry(QtCore.QRect(250, 20, 200, 61))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.Greetings.setFont(font)
        self.Greetings.setStyleSheet("background-color: rgb(117, 0, 176);\n""color: rgb(255,255,255);")
        self.Greetings.setObjectName("Greetings")
        self.input_space = QtWidgets.QLineEdit(self.centralwidget)
        self.input_space.setGeometry(QtCore.QRect(90, 70, 381, 41))
        font = QtGui.QFont()
        font.setFamily("8514oem")
        self.input_space.setFont(font)
        self.input_space.setStyleSheet("selection-background-color: rgb(103, 0, 154);\n""color: rgb(255,255,255);\n"
"border-radius: 5px;")
        self.input_space.setObjectName("input_space")
        self.AddBtn = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.add_item())
        self.AddBtn.setGeometry(QtCore.QRect(490, 77, 121, 31))
        font = QtGui.QFont()
        font.setFamily("8514oem")
        self.AddBtn.setFont(font)
        self.AddBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.AddBtn.setStyleSheet("color: rgb(255,255,255);\n"
"border-radius: 10px;\n")
        self.AddBtn.setObjectName("AddBtn")
        self.my_list = QtWidgets.QListWidget(self.centralwidget)
        self.my_list.setGeometry(QtCore.QRect(90, 130, 381, 221))
        font = QtGui.QFont()
        font.setFamily("Segoe Script")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.my_list.setFont(font)
        self.my_list.setStyleSheet("background-color: rgb(117, 0, 176);\n"
"selection-color: rgb(201, 38, 255);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px;")
        self.my_list.setObjectName("my_list")
        self.Delete_Btn = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.delete_item())
        self.Delete_Btn.setGeometry(QtCore.QRect(490, 140, 121, 31))
        font = QtGui.QFont()
        font.setFamily("8514oem")
        self.Delete_Btn.setFont(font)
        self.Delete_Btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Delete_Btn.setStyleSheet("color: rgb(255,255,255);")
        self.Delete_Btn.setObjectName("Delete_Btn")
        self.Clear_Btn = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.clear_list())
        self.Clear_Btn.setGeometry(QtCore.QRect(490, 210, 121, 31))
        font = QtGui.QFont()
        font.setFamily("8514oem")
        self.Clear_Btn.setFont(font)
        self.Clear_Btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Clear_Btn.setStyleSheet("color: rgb(255,255,255);\n"
"\n"
"")
        self.Clear_Btn.setObjectName("Clear_Btn")
        self.SaveBtn = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.save_list())
        self.SaveBtn.setGeometry(QtCore.QRect(490, 280, 121, 31))
        font = QtGui.QFont()
        font.setFamily("8514oem")
        self.SaveBtn.setFont(font)
        self.SaveBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.SaveBtn.setStyleSheet("color: rgb(255,255,255);")
        self.SaveBtn.setObjectName("SaveBtn")

        self.Outputlbl = QtWidgets.QLabel(self.centralwidget)
        self.Outputlbl.setGeometry(QtCore.QRect(210, 360, 151, 20))
        font1 = QtGui.QFont()
        font1.setFamily("Segoe Script")
        font1.setPointSize(12)
        font1.setBold(True)
        self.Outputlbl.setFont(font)
        self.Outputlbl.setStyleSheet("background-color: rgba(166,81,200,255);\n"
"color: rgb(115, 15, 200);")
        self.Outputlbl.setText("")
        self.Outputlbl.setObjectName("Outputlbl")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 700, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        #self.statusbar = QtWidgets.QStatusBar(MainWindow)
        #self.statusbar.setObjectName("statusbar")
        #MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.grab_all()


        # Grab items from database
    def grab_all(self):
        # Create a database or connect to one
        connection = sqlite3.connect('todolist.db')
        # Create a cursor
        c = connection.cursor()
        c.execute("SELECT * FROM todo_list")
        records = c.fetchall()
        # Commit the changes
        connection.commit()
        # Close our connection
        connection.close()
        # Loop through records and add to screen
        for record in records:
            self.my_list.addItem(str(record[0]))

    # Add item to the list
    def add_item(self):
        task = self.input_space.text()  # takes the items from the input box
        if len(task) != 0:
            self.my_list.addItem(task)  # add item to the list (list view)
        self.input_space.setText("")  # set the input space clear
        self.input_space.setPlaceholderText("Input Tasks")

    # delete an item form the list
    def delete_item(self):
        # Grab the selected row or current row
        clicked = self.my_list.currentRow()
        # Delete selected row
        self.my_list.takeItem(clicked)

    # clear the list
    def clear_list(self):
        self.my_list.clear()

    def save_list(self):
        # Create a database or connect to one
        connection = sqlite3.connect('todolist.db')
        # Create a cursor
        c = connection.cursor()
        # Delete everything in the database table
        c.execute('DELETE FROM todo_list;', )

        # Create Blank List To Hold Todo Items.
        items = []
        # Loop through the listWidget and pull out each
        for index in range(self.my_list.count()):
            items.append(self.my_list.item(index))
        for item in items:
            # print(item.text())
            # Add item to the database
            c.execute("INSERT INTO todo_list VALUES (:item)",
                     {
                          'item': item.text(),
                     })

        # Commit the changes
        connection.commit()
        # Close our connection
        connection.close()
        self.Outputlbl.setText(" List Saved!!")

        """
        # pop up box
        msg = QMessageBox()
        msg.setWindowTitle("Saved")
        msg.setText("Your List has been saved to the database!!")
        msg.setIcon(QMessageBox.Information)
        msg.exec_()
        """

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Todo"))
        self.Greetings.setText(_translate("MainWindow", "Hello!!"))
        self.AddBtn.setText(_translate("MainWindow", "Add Task"))
        self.Delete_Btn.setText(_translate("MainWindow", "Delete Task"))
        self.Clear_Btn.setText(_translate("MainWindow", "Clear List"))
        self.SaveBtn.setText(_translate("MainWindow", "Save"))
        self.input_space.setPlaceholderText(_translate("MainWindow", "Input Tasks"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
