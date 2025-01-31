class StringStorage:
    def __init__(self):
        self.text = str("")

    def getString(self):
        self.text = input("Write your message\n")

    def printString(self):
        print(self.text.upper())

obj1 = StringStorage()
obj1.getString()
obj1.printString()     