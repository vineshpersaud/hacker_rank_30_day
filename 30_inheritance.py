class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)

class Student(Person):
    #   Class Constructor
    #
    #   Parameters:
    #   firstName - A string denoting the Person's first name.
    #   lastName - A string denoting the Person's last name.
    #   id - An integer denoting the Person's ID number.
    #   scores - An array of integers denoting the Person's test scores.
    #
    # Write your constructor here
    def __init__(self, firstName, lastName, idNumber,scores):
        super().__init__(firstName, lastName, idNumber)
        self.scores = scores


    #   Function Name: calculate
    #   Return: A character denoting the grade.
    #
    # Write your function here
    def calculate(self):
        ave = sum(self.scores) / len(self.scores)
        if ave >= 90 :
            return 'O'
        elif ave >= 80:
            return 'E'
        elif ave >= 70:
            return 'A'
        elif ave >= 55:
            return 'P'
        elif ave >= 40 :
            return 'D'
        else:
            return 'T'



line = input().split()
