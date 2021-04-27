class Difference:
    def __init__(self, a):
        self.__elements = a

    # Add your code here
    maximumDifference = 0
    def computeDifference(self):
        for i in range(len(a)):
            for j in range(len(a)):
                if abs(a[i] - a[j]) > self.maximumDifference:
                    self.maximumDifference = abs(a[i] - a[j])
        return self.maximumDifference
# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)
