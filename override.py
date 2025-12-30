class override:
    def display(self):
        print("method invokes from base")
class override2(override):
    def display(self):
        print("method invoked from derived class")
ob=override2()
ob.display()