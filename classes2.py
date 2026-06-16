class dog:
    a = 10
    def sound(self,name,breed):
        self.name = name
        self.breed = breed
        print(self.name,self.breed)

x = dog()
print(x.a)
x.sound('tommy','pitbul')