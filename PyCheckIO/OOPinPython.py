def debug(string: str):
    if False:
        print(string)


class Rectangle():
    def __init__(self, length: int=5, width: int=5):
        self.length = length
        self.width  = width

    @property
    def perimeter(self):
        return self.width*2 + self.length*2
    
    @property
    def area(self):
        return self.width * self.length

    def display(self):
        print(f"The Length of the rectangle is:     {self.length}")
        print(f"The Width of the rectangle is:      {self.width}")
        print(f"The Perimeter of the rectangle is:  {self.perimeter}")
        print(f"The Area of the rectangle is:       {self.area}")

class Parallelepipede(Rectangle):
    def __init__(self, length: int=10, width: int=10, height: int=5):
        super().__init__(length, width)
        self.height     = height
    
    @property
    def Volume(self):
        return self.area * self.height
    
test = Parallelepipede()
assert test.Volume == 500

class Person():
    def __init__(self, name: str, age: str):
        self.name   = name
        self.age    = age
    
    def display(self):
        print(f"My Name is {self.name}")
        print(f"I am {self.age} years old")

class Student(Person):
    def __init__(self, name: str, age: int, section: str):
        super().__init__(name, age)
        self.section = section

    def displayStudent(self):
        super().display()
        print(f"I am studying {self.section}")

student1 = Student("Isaac", "18", "CompSci")
student1.displayStudent()
#Can't assert this, it doesn't return anything.

class BankAcount():
    def __init__(self, accountNumber: int, name: str, balance: int):
        self.accountNumber  = accountNumber
        self.name           = name
        self.balance        = balance
    
    def deposit(self, value: int):
        if value > 0:
            self.balance += value
        else:
            print("Error, Value must be Greater Than Zero")

    def withdrawl(self, value: int):
        if 0 > value:
            print("Error, Cannot withdraw negative money!")
        elif value > self.balance:
            print("Error, Cannot withdraw more money than present in account")
        else:
            self.balance -= value

    def bankFees(self):
        self.balance -= self.balance/20 #Subtracts 5% of the balance.
    
    def display(self):
        print(f"Account number is:  {self.accountNumber}")
        print(f"Account Name is:    {self.name}")
        print(f"Current Balance is: {self.balance}")

bank = BankAcount(1837, "Isaac", 0)
bank.deposit(50000)
bank.deposit(-1000)
bank.withdrawl(100000000)
bank.withdrawl(-10)
bank.bankFees()
bank.display()
bank.withdrawl(47500)
bank.withdrawl(20)
bank.display()
#Can't exactly assert these either? they either don;t return anything, or directly print it tp console themselves.

class Computation():
    def __init__(self):
        pass
    
    def factorial(self, targ: int):
        outval = 1
        for i in range(1, targ + 1):
            outval = outval*i
        if targ >= 0:
            return outval
        else:
            return "Undefined"
    
    def sum(self, targ: int):
        outval = 0
        for i in range(0, targ+1):
            outval += i
        return outval
    
    def testPrim(self, targ):
        #Well, this is gonna be "Fun"
        debug(targ)

        if targ % 2 == 0:
            if targ == 2:
                debug("2 is prime")
                return True
            else:
                debug("Number even")
                return False
        else:
            outval = [targ%i for i in range(2, targ)]
            debug(outval)
            if 0 in outval:
                debug("0 in outval")
                return False
            else:
                debug("0 not in outval")
                return True
    
    def testPrims(self, arg1, arg2):
        outval = []
        for i in range(arg1, arg2 +1):
            if self.testPrim(i):
                outval.append(i)
        return outval 
    
    def tableMult(self, targ, out = True):
        outval = []
        for i in range(1, targ+1):
            outval.append(f"{targ} x {i} = {i*targ}")
        if out:
            print(outval)
        return outval
    
    def allTablesMult(self, out = True):
        outval = []
        for j in range(1, 9+1):
            midval = []
            for i in range(1, 9+1):
                midval.append(f"{j} x {i} = {j*i}")
            outval.append(midval)
        if out:
            print(outval)
        return outval

    #Easy to make "Static", just don't get how that'd impact the functionality and not willing to test.
    def listDiv(self, targ: int):
        ldiv = [i for i in range(1, targ+1) if targ % i == 0]
        return ldiv
    
    def listDivPrime(self, targ: int):
        ldiv = self.listDiv(targ)
        outval = [i for i in ldiv if self.testPrim(i)]
        return outval

    
comp1 = Computation()
assert comp1.factorial(6)   == 720
assert comp1.factorial(0)   == 1
assert comp1.factorial(-5)  == "Undefined"

assert comp1.sum(100)       == 5050

assert comp1.testPrim(8)        == False
assert comp1.testPrim(2)
assert comp1.testPrim(5)
assert comp1.testPrim(55)       == False
assert comp1.testPrims(1, 10)   == [1, 2, 3, 5, 7]

#Print is toggleable, defaults to True.
assert comp1.tableMult(5)                   == ['5 x 1 = 5', '5 x 2 = 10', '5 x 3 = 15', '5 x 4 = 20', '5 x 5 = 25']
assert comp1.allTablesMult(out = False)     == [['1 x 1 = 1', '1 x 2 = 2', '1 x 3 = 3', '1 x 4 = 4', '1 x 5 = 5', '1 x 6 = 6', '1 x 7 = 7', '1 x 8 = 8', '1 x 9 = 9'],
 ['2 x 1 = 2', '2 x 2 = 4', '2 x 3 = 6', '2 x 4 = 8', '2 x 5 = 10', '2 x 6 = 12', '2 x 7 = 14', '2 x 8 = 16', '2 x 9 = 18'],
 ['3 x 1 = 3', '3 x 2 = 6', '3 x 3 = 9', '3 x 4 = 12', '3 x 5 = 15', '3 x 6 = 18', '3 x 7 = 21', '3 x 8 = 24', '3 x 9 = 27'],
 ['4 x 1 = 4', '4 x 2 = 8', '4 x 3 = 12', '4 x 4 = 16', '4 x 5 = 20', '4 x 6 = 24', '4 x 7 = 28', '4 x 8 = 32', '4 x 9 = 36'],
 ['5 x 1 = 5', '5 x 2 = 10', '5 x 3 = 15', '5 x 4 = 20', '5 x 5 = 25', '5 x 6 = 30', '5 x 7 = 35', '5 x 8 = 40', '5 x 9 = 45'],
 ['6 x 1 = 6', '6 x 2 = 12', '6 x 3 = 18', '6 x 4 = 24', '6 x 5 = 30', '6 x 6 = 36', '6 x 7 = 42', '6 x 8 = 48', '6 x 9 = 54'],
 ['7 x 1 = 7', '7 x 2 = 14', '7 x 3 = 21', '7 x 4 = 28', '7 x 5 = 35', '7 x 6 = 42', '7 x 7 = 49', '7 x 8 = 56', '7 x 9 = 63'],
 ['8 x 1 = 8', '8 x 2 = 16', '8 x 3 = 24', '8 x 4 = 32', '8 x 5 = 40', '8 x 6 = 48', '8 x 7 = 56', '8 x 8 = 64', '8 x 9 = 72'],
 ['9 x 1 = 9', '9 x 2 = 18', '9 x 3 = 27', '9 x 4 = 36', '9 x 5 = 45', '9 x 6 = 54', '9 x 7 = 63', '9 x 8 = 72', '9 x 9 = 81']]
#Works, but neither of these format their outputs nicely. However, that's not really in the spec.

assert comp1.listDiv(100)       == [1, 2, 4, 5, 10, 20, 25, 50, 100]
assert comp1.listDivPrime(100)  == [1, 2, 5]
