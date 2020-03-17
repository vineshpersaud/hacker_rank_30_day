class Difference:
    def __init__(self, a):
        self.__elements = a

    # Add your code here
    def __init__(self ,elements):
        self.elements = elements
        self.maximumDifference = -1

    def computeDifference(self):
        counter = 0
        for i in self.elements:
            for ele in self.elements[counter+1:]:
                if abs(i - ele) > self.maximumDifference:
                    self.maximumDifference = abs(i - ele)
            counter +=1
