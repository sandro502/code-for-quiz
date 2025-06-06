from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer, QTime
class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        Form.setWindowTitle("ჩემი კლავიატურა")
        #რეალური დრო
        self.Label = QtWidgets.QLabel(Form)
        self.Label.setGeometry(QtCore.QRect(300, 10, 90, 20))
        self.timer = QTimer(Form)
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000) #1 წამში ერთხელ განახლება


        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(20, 140, 21, 31))
        self.pushButton.setObjectName("pushButton")

        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(30, 40, 331, 71))
        self.lineEdit.setObjectName("lineEdit")

        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(50, 140, 21, 31))
        self.pushButton_2.setObjectName("pushButton_2")

        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(110, 140, 21, 31))
        self.pushButton_3.setObjectName("pushButton_3")

        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(140, 140, 21, 31))
        self.pushButton_4.setObjectName("pushButton_4")

        self.pushButton_5 = QtWidgets.QPushButton(Form)
        self.pushButton_5.setGeometry(QtCore.QRect(200, 140, 21, 31))
        self.pushButton_5.setObjectName("pushButton_5")

        self.pushButton_6 = QtWidgets.QPushButton(Form)
        self.pushButton_6.setGeometry(QtCore.QRect(170, 140, 21, 31))
        self.pushButton_6.setObjectName("pushButton_6")

        self.pushButton_7 = QtWidgets.QPushButton(Form)
        self.pushButton_7.setGeometry(QtCore.QRect(90, 220, 21, 31))
        self.pushButton_7.setObjectName("pushButton_7")

        self.pushButton_8 = QtWidgets.QPushButton(Form)
        self.pushButton_8.setGeometry(QtCore.QRect(60, 220, 21, 31))
        self.pushButton_8.setObjectName("pushButton_8")

        self.pushButton_9 = QtWidgets.QPushButton(Form)
        self.pushButton_9.setGeometry(QtCore.QRect(280, 180, 21, 31))
        self.pushButton_9.setObjectName("pushButton_9")

        self.pushButton_10 = QtWidgets.QPushButton(Form)
        self.pushButton_10.setGeometry(QtCore.QRect(220, 180, 21, 31))
        self.pushButton_10.setObjectName("pushButton_10")

        self.pushButton_11 = QtWidgets.QPushButton(Form)
        self.pushButton_11.setGeometry(QtCore.QRect(250, 180, 21, 31))
        self.pushButton_11.setObjectName("pushButton_11")

        self.pushButton_12 = QtWidgets.QPushButton(Form)
        self.pushButton_12.setGeometry(QtCore.QRect(70, 180, 21, 31))
        self.pushButton_12.setObjectName("pushButton_12")

        self.pushButton_13 = QtWidgets.QPushButton(Form)
        self.pushButton_13.setGeometry(QtCore.QRect(40, 180, 21, 31))
        self.pushButton_13.setObjectName("pushButton_13")

        self.pushButton_14 = QtWidgets.QPushButton(Form)
        self.pushButton_14.setGeometry(QtCore.QRect(290, 140, 20, 31))
        self.pushButton_14.setObjectName("pushButton_14")

        self.pushButton_15 = QtWidgets.QPushButton(Form)
        self.pushButton_15.setGeometry(QtCore.QRect(100, 180, 21, 31))
        self.pushButton_15.setObjectName("pushButton_15")

        self.pushButton_16 = QtWidgets.QPushButton(Form)
        self.pushButton_16.setGeometry(QtCore.QRect(130, 180, 21, 31))
        self.pushButton_16.setObjectName("pushButton_16")

        self.pushButton_17 = QtWidgets.QPushButton(Form)
        self.pushButton_17.setGeometry(QtCore.QRect(160, 180, 21, 31))
        self.pushButton_17.setObjectName("pushButton_17")

        self.pushButton_18 = QtWidgets.QPushButton(Form)
        self.pushButton_18.setGeometry(QtCore.QRect(190, 180, 21, 31))
        self.pushButton_18.setObjectName("pushButton_18")

        self.pushButton_19 = QtWidgets.QPushButton(Form)
        self.pushButton_19.setGeometry(QtCore.QRect(260, 140, 21, 31))
        self.pushButton_19.setObjectName("pushButton_19")

        self.pushButton_20 = QtWidgets.QPushButton(Form)
        self.pushButton_20.setGeometry(QtCore.QRect(230, 140, 21, 31))
        self.pushButton_20.setObjectName("pushButton_20")

        self.pushButton_21 = QtWidgets.QPushButton(Form)
        self.pushButton_21.setGeometry(QtCore.QRect(80, 140, 21, 31))
        self.pushButton_21.setObjectName("pushButton_21")

        self.pushButton_22 = QtWidgets.QPushButton(Form)
        self.pushButton_22.setGeometry(QtCore.QRect(120, 220, 21, 31))
        self.pushButton_22.setObjectName("pushButton_22")

        self.pushButton_23 = QtWidgets.QPushButton(Form)
        self.pushButton_23.setGeometry(QtCore.QRect(150, 220, 21, 31))
        self.pushButton_23.setObjectName("pushButton_23")

        self.pushButton_24 = QtWidgets.QPushButton(Form)
        self.pushButton_24.setGeometry(QtCore.QRect(180, 220, 21, 31))
        self.pushButton_24.setObjectName("pushButton_24")

        self.pushButton_25 = QtWidgets.QPushButton(Form)
        self.pushButton_25.setGeometry(QtCore.QRect(210, 220, 21, 31))
        self.pushButton_25.setObjectName("pushButton_25")

        self.pushButton_26 = QtWidgets.QPushButton(Form)
        self.pushButton_26.setGeometry(QtCore.QRect(240, 220, 21, 31))
        self.pushButton_26.setObjectName("pushButton_26")

        self.pushButton_27 = QtWidgets.QPushButton(Form)
        self.pushButton_27.setGeometry(QtCore.QRect(80, 260, 151, 31))
        self.pushButton_27.setObjectName("pushButton_27")

        self.pushButton_28 = QtWidgets.QPushButton(Form)
        self.pushButton_28.setGeometry(QtCore.QRect(270, 260, 51, 31))
        self.pushButton_28.setObjectName("pushButton_28")


        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        # ასოების დაკავშირება აღწერილ ფუნქციებთან.(ტექსტის დამატების და გასუფთავების)

        self.pushButton.clicked.connect(lambda: self.insert_letter("Q"))    #clicked.connect(...) ითხოვს ფუნქციას,
        self.pushButton_2.clicked.connect(lambda: self.insert_letter("W"))  #რომელიც არ იღებს არგუმენტს,
        self.pushButton_3.clicked.connect(lambda: self.insert_letter("R"))  #მაგრამ მინდა გამოვიძახო
        self.pushButton_4.clicked.connect(lambda: self.insert_letter("T"))  #insert_letter("Q"), სადაც "Q" არგუმენტია.
        self.pushButton_5.clicked.connect(lambda: self.insert_letter("U"))  #ამიტო ვიყენებ ლამბდას.
        self.pushButton_6.clicked.connect(lambda: self.insert_letter("Y"))
        self.pushButton_7.clicked.connect(lambda: self.insert_letter("X"))  #clicked.connect_ით კოდი რეაგირებს ასოზე დაჭერისას
        self.pushButton_8.clicked.connect(lambda: self.insert_letter("Z"))
        self.pushButton_9.clicked.connect(lambda: self.insert_letter("L"))
        self.pushButton_10.clicked.connect(lambda: self.insert_letter("J"))  #lambda: self.insert_letter("Q") — ესაა ფუნქცია,
        self.pushButton_11.clicked.connect(lambda: self.insert_letter("K"))  #რომელიც  გამოიძახებს self.insert_letter("Q")
        self.pushButton_12.clicked.connect(lambda: self.insert_letter("S"))  #მაშინ, როცა ღილაკზე დააჭერენ.
        self.pushButton_13.clicked.connect(lambda: self.insert_letter("A"))
        self.pushButton_14.clicked.connect(lambda: self.insert_letter("P"))
        self.pushButton_15.clicked.connect(lambda: self.insert_letter("D"))
        self.pushButton_16.clicked.connect(lambda: self.insert_letter("F"))
        self.pushButton_17.clicked.connect(lambda: self.insert_letter("G"))
        self.pushButton_18.clicked.connect(lambda: self.insert_letter("H"))
        self.pushButton_19.clicked.connect(lambda: self.insert_letter("O"))
        self.pushButton_20.clicked.connect(lambda: self.insert_letter("I"))
        self.pushButton_21.clicked.connect(lambda: self.insert_letter("E"))
        self.pushButton_22.clicked.connect(lambda: self.insert_letter("C"))
        self.pushButton_23.clicked.connect(lambda: self.insert_letter("V"))
        self.pushButton_24.clicked.connect(lambda: self.insert_letter("B"))
        self.pushButton_25.clicked.connect(lambda: self.insert_letter("N"))
        self.pushButton_26.clicked.connect(lambda: self.insert_letter("M"))

        self.pushButton_27.clicked.connect(lambda: self.insert_letter(" "))  # space bar
        self.pushButton_28.clicked.connect(self.clear_text)  # clear

    # ასოს დამატების ფუნქცია
    def insert_letter(self, letter):
        current_text = self.lineEdit.text()
        self.lineEdit.setText(current_text + letter)

    # ტექსტის გასუფთავების ფუნქცია
    def clear_text(self):
        self.lineEdit.clear()
    #დროის ფუნქცია
    def update_time(self):
        self.Label.setText(QTime.currentTime().toString("hh:mm:ss"))

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        self.pushButton.setText(_translate("Form", "Q"))
        self.pushButton_2.setText(_translate("Form", "W"))
        self.pushButton_3.setText(_translate("Form", "R"))
        self.pushButton_4.setText(_translate("Form", "T"))
        self.pushButton_5.setText(_translate("Form", "U"))
        self.pushButton_6.setText(_translate("Form", "Y"))
        self.pushButton_7.setText(_translate("Form", "X"))
        self.pushButton_8.setText(_translate("Form", "Z"))
        self.pushButton_9.setText(_translate("Form", "L"))
        self.pushButton_10.setText(_translate("Form", "J"))
        self.pushButton_11.setText(_translate("Form", "K"))
        self.pushButton_12.setText(_translate("Form", "S"))
        self.pushButton_13.setText(_translate("Form", "A"))
        self.pushButton_14.setText(_translate("Form", "P"))
        self.pushButton_15.setText(_translate("Form", "D"))
        self.pushButton_16.setText(_translate("Form", "F"))
        self.pushButton_17.setText(_translate("Form", "G"))
        self.pushButton_18.setText(_translate("Form", "H"))
        self.pushButton_19.setText(_translate("Form", "O"))
        self.pushButton_20.setText(_translate("Form", "I"))
        self.pushButton_21.setText(_translate("Form", "E"))
        self.pushButton_22.setText(_translate("Form", "C"))
        self.pushButton_23.setText(_translate("Form", "V"))
        self.pushButton_24.setText(_translate("Form", "B"))
        self.pushButton_25.setText(_translate("Form", "N"))
        self.pushButton_26.setText(_translate("Form", "M"))
        self.pushButton_27.setText(_translate("Form", "space bar"))
        self.pushButton_28.setText(_translate("Form", "clear"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
