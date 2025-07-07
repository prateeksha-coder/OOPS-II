class student():
    def __init__(self,n,s):
        self.name=n
        self.surname=s
    def __del__(self):
        print("Desctructor called,Student deleted")
    

ob=student("Prateeksha","Singh")
print(ob.name," ",ob.surname)
del ob
print(ob.name," ",ob.surname)

