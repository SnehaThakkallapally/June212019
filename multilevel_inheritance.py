class Grand_Father:
    def first_gen(self):
        print("This is GrandFather")

class Father(Grand_Father):
     
    def second_gen(self):
         print("This is Father")

class Son(Father):
    def third_gen(self):
         print("This is son")
 
    
  
obj = Son()  
obj.first_gen()
obj.second_gen()
obj.third_gen()