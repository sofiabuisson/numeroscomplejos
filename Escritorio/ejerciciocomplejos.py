import unittest

class Complejo(object):
    def __init__(self, real, imag=0):
        self.real = real
        self.imag = imag
       
    def sumar(self, otro):
        result = Complejo(self.real + otro.real,
                          self.imag + otro.imag)
        return result
       
    def restar(self, otro):
        result = Complejo(self.real - otro.real,
                          self.imag - otro.imag)
        return result
       
    def multiplicar(self, otro):
        result = Complejo((self.real*otro.real - self.imag*otro.imag),
                          (self.real*otro.imag + self.imag*otro.real))
        return result
       
    def dividir(self, otro):
        a = (self.real*otro.real + self.imag*otro.imag)
        b = (self.imag*otro.real - self.real*otro.imag)
        denom = ((otro.real**2)+(otro.imag**2))
        result = Complejo((a/denom),
               (b/denom))
        return result
   
    def igual(self, otro):
        return self.real == otro.real and self.imag == otro.imag
       
class TestComplejo(unittest.TestCase):
   
    def test_sumar(self):
       
        c1 = Complejo(7,8)
        c2 = Complejo(5,1)
       
        suma = c1.sumar(c2)
       
        self.assertEqual(suma.real, 3)
        self.assertEqual(suma.imag, 0)
   
    def test_restar(self):
       
        c1 = Complejo(9,3)
        c2 = Complejo(4,4)
       
        restar = c1.restar(c2)
       
        self.assertEqual(restar.real, -4)
        self.assertEqual(restar.imag, -9)
       
    def test_multiplicar(self):
        c1 = Complejo(4,6)
        c2 = Complejo(5,9)
       
        multiplica = c1.multiplicar(c2)
       
        self.assertEqual(multiplica.real, -1)
        self.assertEqual(multiplica.imag, 12)
   
    def test_dividir(self):
        c1 = Complejo(4,5)
        c2 = Complejo(0,-4)
       
        divide = c1.dividir(c2)
       
        self.assertEqual(divide.real, float(-1/4))
        self.assertEqual(divide.imag, float(5/6))
   
if __name__ == "__main__":
    unittest.main()
