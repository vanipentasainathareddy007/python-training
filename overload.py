class methodOverLoad:
    def multiply(self,a,b):
        print(a*b)
    def multiply(self,a,b,c):
        print(a*b*c)
m=methodOverLoad()
m.multiply(5,10)