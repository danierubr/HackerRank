

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
    def __init__(self, firstName, lastName, idNumber, scores):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber
        self.scores = scores

    #   Function Name: calculate
    #   Return: A character denoting the grade.
    #
    # Write your function here
    def calculate(self):
        soma = sum(self.scores)
        grade = soma / len(self.scores)
        
        if grade >= 90:
            return 'O'
        elif 80 <= grade < 90:
            return 'E'
        elif 70 <= grade < 80:
            return 'A'
        elif 55 <= grade < 70:
            return 'P'
        elif 40 <= grade < 55:
            return 'D'
        else:
            return 'T'
