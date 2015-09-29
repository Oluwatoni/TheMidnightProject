import sys
from time import gmtime, strftime 
from PyQt4 import QtGui
from questions import Ui_QuestionWindow

CONST_FILENAME = "patientData.txt"

#UI main window
class Main(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.ui = Ui_QuestionWindow()
        self.ui.setupUi(self)
        self.ui.submitForm.clicked.connect(self.submit)
    
    #submt form button
    def submit(self):
        f = open(CONST_FILENAME, 'w')
        exactTime = strftime("%Y-%m-%d ,%H:%M:%S ,", gmtime())
        #time 
        f.write(exactTime)
        #write patient comments and ratings to file
        f.write(str(self.ui.numberRating.value()) + "," + str(self.ui.numberRating_2.value()) + ",")  
        f.write(str(self.ui.numberRating_3.value()) + "," + str(self.ui.numberRating_4.value()) + ",")
        f.write(str(self.ui.numberRating_5.value()) + "," + str(self.ui.numberRating_6.value()) + ",")
        f.write(str(self.ui.numberRating_7.value()) + "," + str(self.ui.numberRating_8.value()) + ",")
        f.write(str(self.ui.numberRating_9.value()) + "," + str(self.ui.numberRating_10.value()) + ",")
        f.write(str(self.ui.checkBox.isChecked()) + ",")
        f.write(self.ui.comment1.toPlainText() + "   " + self.ui.comment1_2.toPlainText() + "   ")
        f.write(self.ui.comment1_3.toPlainText() + "   " + self.ui.comment1_4.toPlainText() + "   ")
        f.write(self.ui.comment1_5.toPlainText() + "   " + self.ui.comment1_6.toPlainText() + "   ")
        f.write(self.ui.comment1_7.toPlainText() + "   " + self.ui.comment1_8.toPlainText() + "   ")
        f.write(self.ui.comment1_9.toPlainText() + "   " + self.ui.comment1_10.toPlainText() + "\n")
        
        f.close()
        sys.exit(app.exec_())
        
if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())