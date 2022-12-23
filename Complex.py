class Complex:

    def __init__(self, Re=None, Im=None):
        """ Initialize self """
        self.Re = Re
        self.Im = Im

    def __add__(self, other):
        """ Return sum. """
        return Complex(self.Re + other.Re, self.Im + other.Im)

    def __sub__(self, other):
        """ Return subtraction. """
        return Complex(self.Re - other.Re, self.Im - other.Im)

    def __mul__(self, other):
        """ Return str(multiply). """
        return Complex(self.Re * other.Re - self.Im * other.Im,
                       self.Im * other.Re + self.Re * other.Im)
    def __str__(self):
        """ Return str(self). """
        if self.Re == 0:
            return str(self.Im) + 'i'
        if self.Im == 0:
            return str(self.Re)
        if self.Im == 1:
            return str(self.Re) + '+' + 'i'
        if self.Im == -1:
            return str(self.Re) + '-' + 'i'
        if self.Im > 0:
            return str(self.Re) + '+' + str(self.Im) + 'i'
        if self.Im < 0:
            return str(self.Re) + str(self.Im) + 'i'



