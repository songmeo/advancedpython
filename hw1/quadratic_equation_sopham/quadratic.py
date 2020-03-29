from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

class MyWindow(QMainWindow):
	def __init__(self):
		super(MyWindow, self).__init__()
		self.setGeometry(200, 200, 300, 300)
		self.setWindowTitle("Quadratic Calculator")
		self.initUI()
		
	def initUI(self):
		self.label = QtWidgets.QLabel(self)
		self.label.setText("label")
		self.label.move(50, 50)
	
		self.b1 = QtWidgets.QPushButton(self)
		self.b1.setText("enter")
		self.b1.clicked.connect(quadratic)
	
	def clicked(self):
		self.label.setText("pressed")
	
def quadratic():
  while True:
    try:
      a, b, c = map(int, input("Please type a, b, c: ").split())
      if a == 0:
        raise Exception("a could not be 0. Please try again.")
        break
    except ValueError:
      print("Illegal input.")
    except Exception:
      print("a could not be zero.")
  d = b**2 - 4*a*c
  if d >= 0:
    x1 = (-b + math.sqrt(d)) / (2*a)
    x2 = (-b - math.sqrt(d)) / (2*a)
  else:
    x1 = (-b + cmath.sqrt(d)) / (2*a)
    x2 = (-b - cmath.sqrt(d)) / (2*a)
  print('x1 = {} x2 = {}'.format(x1, x2))

  
def window():
	app = QApplication(sys.argv)
	win = MyWindow()
	win.show()
	sys.exit(app.exec_())

if __name__ == "__main__":
	window()
