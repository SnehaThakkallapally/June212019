class Father(object):
	def show_father(self):
		print("Father")

		
class Mother(object):
	def show_mother(self):
		 print("Mother")

		 
class Daughter(Mother, Father):
	 print("Daughter")
	
obj = Daughter()
obj.show_father()
obj.show_mother()
