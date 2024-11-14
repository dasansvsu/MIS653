# %%
print("hello world")

# %%
def square_number(number):
    return number ** 2

num = 4
result = square_number(num)
print(f"The square of {num} is {result}")

# %%
class Car:
    def __init__(self, make, model, year, mileage):
        self.make = make
        self.model = model
        self.year = year
        self.mileage = mileage

    def display_info(self):
        print(f"{self.year} {self.make} {self.model}")
        print(f"Mileage: {self.mileage} miles")

    def drive(self, miles):
        self.mileage += miles
        print(f"Driving {miles} miles. New mileage: {self.mileage} miles")

# %%
my_car = Car("Toyota", "Corolla", 2020, 15000.5)
my_car.display_info()
my_car.drive(200)
my_car.display_info()

# %%
class Book:
    def __init__(self, title, author, year, price):
        self.title = title
        self.author = author
        self.year = year
        self.price = price

    def display_info(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Year: {self.year}")
        print(f"Price: ${self.price:.2f}")

    def apply_discount(self, percentage):
        discount = self.price * percentage
        self.price -= discount
        print(f"Discount applied. New price: ${self.price:.2f}")

# %%
my_book = Book("To Kill a Mockingbird", "Harper Lee", 1960, 18.99)
my_book.display_info()
my_book.apply_discount(0.1)
my_book.display_info()


