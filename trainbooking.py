class Train:
    l=[1,2,3,4,5]
    def __init__(self,s):
        self.s=s
    def book(self):
        if self.l:
            print("These seats are available : \n",self.l)
            i=int(input("Which one you wanna book : "))
            if i in self.l:
                print("Sir,your seat is booked successfully!")
                self.l.remove(i)
            else:
                print("Sorry Sir, This Seat is not available!")
        else:
            print("No seats are available!")

hesh=Train(2)
hesh.book()
