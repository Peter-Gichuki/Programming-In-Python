#Class to convert Celsius to Fahrenheit and viceversa
class Temperature:
    def __init__(self, celsius, fahrenheit):
        self.celsius=celsius
        self.fahrenheit=fahrenheit

    def convert_fahrenheit(self):
        return (5/9*(self.fahrenheit-32))

    def convert_celsius(self):
        return ((9/5*(self.celsius))+32)

convert= Temperature(37, 100)
print(convert.convert_celsius())
print(convert.convert_fahrenheit())