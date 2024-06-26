from PyQt6.QtWidgets import *
from gui2 import *
from formulas import *
from Project2 import *
from csv import *

class Logic(QMainWindow, Ui_Dialog):
    def __init__(self):
        '''
        Tells the window what to do on startup and lays out the function of the buttons.
        '''
        super().__init__()
        self.setupUi(self)
        self.hidemode()
        
        self.ClearBtn.clicked.connect(self.Result.clear)
        self.ModeBtn.clicked.connect(self.mode)
        self.DelBtn.clicked.connect(self.delete)
        self.PlusMinusBtn.clicked.connect(self.plusminus)
        
        self.Btn1.clicked.connect(self.one)
        self.Btn2.clicked.connect(self.two)
        self.Btn3.clicked.connect(self.three)
        self.Btn4.clicked.connect(self.four)
        self.Btn5.clicked.connect(self.five)
        self.Btn6.clicked.connect(self.six)
        self.Btn7.clicked.connect(self.seven)
        self.Btn8.clicked.connect(self.eight)
        self.Btn9.clicked.connect(self.nine)
        self.Btn0.clicked.connect(self.zero)
        self.LeftParBtn.clicked.connect(self.leftpar)
        self.RightParBtn.clicked.connect(self.rightpar)
        self.DecimalBtn.clicked.connect(self.decimal)
        
        self.AddBtn.clicked.connect(self.add)
        self.SubtractBtn.clicked.connect(self.subtract)
        self.MultiplyBtn.clicked.connect(self.multiply)
        self.DivideBtn.clicked.connect(self.divide)
        self.EqualsBtn.clicked.connect(self.equals)
        
        self.ShapeSubmit.clicked.connect(self.shape)
        self.BaseSubmit.clicked.connect(self.area_circle_square)
        self.HeightSubmit.clicked.connect(self.area_rectangle_triangle)
    
    def checkforerror(self):
        '''
        If an error value is currently shown and the user types, it will be cleared.
        '''
        formula = self.Result.toPlainText()
        if formula == 'Error' or formula == 'Values must be positive':
            self.Result.clear()
            
    def one(self):
        '''
        If one of the following buttons are pressed, the correct key is typed in the calculator.
        If an error is currently shown, it will be cleared and typed over.
        '''
        self.checkforerror()
        self.Result.insertPlainText('1')
    def two(self):
        self.checkforerror()
        self.Result.insertPlainText('2')
    def three(self):
        self.checkforerror()
        self.Result.insertPlainText('3')
    def four(self):
        self.checkforerror()
        self.Result.insertPlainText('4')
    def five(self):
        self.checkforerror()
        self.Result.insertPlainText('5')
    def six(self):
        self.checkforerror()
        self.Result.insertPlainText('6')
    def seven(self):
        self.checkforerror()
        self.Result.insertPlainText('7')
    def eight(self):
        self.checkforerror()
        self.Result.insertPlainText('8')
    def nine(self):
        self.checkforerror()
        self.Result.insertPlainText('9')
    def zero(self):
        self.checkforerror()
        self.Result.insertPlainText('0')
    def leftpar(self):
        self.checkforerror()
        self.Result.insertPlainText('(')
    def rightpar(self):
        self.checkforerror()
        self.Result.insertPlainText(')')
    def decimal(self):
        self.checkforerror()
        self.Result.insertPlainText('.')
    def add(self):
        self.checkforerror()
        self.Result.insertPlainText(' + ')
    def subtract(self):
        self.checkforerror()
        self.Result.insertPlainText(' - ')
    def multiply(self):
        self.checkforerror()
        self.Result.insertPlainText(' * ')
    def divide(self):
        self.checkforerror()
        self.Result.insertPlainText(' / ')
        
    def equals(self):
        '''
        The text in the calculator is converted to a formula and evaluated up to 10 decimal places.
        Whole number answers will be converted to ints.
        The answer is appended back up into the calculator as a string.
        If the result is an error, an error message is shown.
        '''
        try:
            formula = self.Result.toPlainText()
            result = round(eval(formula), 10)
            if result % 1 == 0:
                result = int(result)
            self.Result.clear()
            self.Result.append(str(result))
        except:
            self.Result.clear()
            self.Result.append("Error")
    
    def delete(self):
        '''
        The last character of the formula is deleted.
        If an error message is displayed, it is fully deleted.
        If there is nothing to delete, nothing happens.
        '''
        self.checkforerror()
        formula = self.Result.toPlainText()
        if formula == '':
            pass
        elif formula[-1] == ' ':
            formula = formula[:-3]
            self.Result.clear()
            self.Result.append(formula)
        else:
            formula = formula[:-1]
            self.Result.clear()
            self.Result.append(formula)
    
    def plusminus(self):
        '''
        The sign of the last value in the formula is changed.
        If there are no values, nothing happens.
        The list is split and the final values is changed, then the message is reappended.
        '''
        self.checkforerror()
        values = self.Result.toPlainText()
        if values == '':
            pass
        elif values == 'Error' or values == 'Values must be positive':
            pass
        else:
            splitvalues = values.split()
            if splitvalues[-1][0] != '-':
                splitvalues[-1] = f'-{splitvalues[-1]}'
            else:
                splitvalues[-1] = splitvalues[-1][1:]
            result = ' '.join(splitvalues)
            self.Result.clear()
            self.Result.append(result)
    
    def mode(self):
        '''
        If the area functions are open, they close. If they are closed, the shape options open.
        '''
        if self.ShapeSubmit.isVisible():
            self.hidemode() 
        else:
            self.CircleBtn.show()
            self.SquareBtn.show()
            self.RectangleBtn.show()
            self.TriangleBtn.show()
            self.ShapeSubmit.show()
    def hidemode(self):
        '''
        All buttons relating to area are hidden.
        '''
        self.CircleBtn.hide()
        self.SquareBtn.hide()
        self.RectangleBtn.hide()
        self.TriangleBtn.hide()
        self.ShapeSubmit.hide()
        self.BaseLabel.hide()
        self.BaseInput.hide()
        self.BaseSubmit.hide()
        self.HeightLabel.hide()
        self.HeightInput.hide()
        self.HeightSubmit.hide()
        
    def shape(self):
        '''
        Once a shape is selected, the needed criteria are revealed.
        '''
        if self.CircleBtn.isChecked() or self.SquareBtn.isChecked():
            self.BaseLabel.show()
            self.BaseInput.show()
            self.BaseSubmit.show()
            self.HeightLabel.hide()
            self.HeightInput.hide()
            self.HeightSubmit.hide()
        elif self.RectangleBtn.isChecked() or self.TriangleBtn.isChecked():
            self.BaseLabel.show()
            self.BaseInput.show()
            self.BaseSubmit.hide()
            self.HeightLabel.show()
            self.HeightInput.show()
            self.HeightSubmit.show()
        
    def area_circle_square(self):
        '''
        The area of the selected shape is calculated.
        Since only the base input is open, only a square or circle can be calculated.
        If an impossible equation is given, an error will display on the calculator.
        '''
        if self.CircleBtn.isChecked():
            try:
                base = float(self.BaseInput.text())
                area = 3.1415 * (base * base)
                if base <= 0:
                    self.Result.clear()
                    self.Result.append('Values must be positive')
                else:
                    self.Result.clear()
                    self.Result.append(f'{area:.2f}')
            except:
                self.Result.clear()
                self.Result.append('Values must be positive')
        elif self.SquareBtn.isChecked():
            try:
                base = float(self.BaseInput.text())
                area = base * base
                if base <= 0:
                    self.Result.clear()
                    self.Result.append('Values must be positive')
                else:
                    self.Result.clear()
                    self.Result.append(f'{area:.2f}')
            except:
                self.Result.clear()
                self.Result.append('Values must be positive')
                
    def area_rectangle_triangle(self):
        '''
        The area of the selected shape is calculated.
        Since the base and height inputs are open, rectangles and triangles can be calculated.
        If an impossible equation is given, an error will display on the calculator.
        '''
        if self.RectangleBtn.isChecked():
            try:
                base = float(self.BaseInput.text())
                height = float(self.HeightInput.text())
                area = base * height
                if base <= 0 or height <= 0:
                    self.Result.clear()
                    self.Result.append('Values must be positive')
                else:
                    self.Result.clear()
                    self.Result.append(f'{area:.2f}')
            except:
                self.Result.clear()
                self.Result.append('Values must be positive')
        elif self.TriangleBtn.isChecked():
            try:
                base = float(self.BaseInput.text())
                height = float(self.HeightInput.text())
                area = base * height / 2
                if base <= 0 or height <= 0:
                    self.Result.clear()
                    self.Result.append('Values must be positive')
                else:
                    self.Result.clear()
                    self.Result.append(f'{area:.2f}')
            except:
                self.Result.clear()
                self.Result.append('Values must be positive')
