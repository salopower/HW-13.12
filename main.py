class Human:
    def __init__(self, name: str, surname: str, age: int, phone: str, address: str):
        self.name = name
        self.surname = surname
        self.age = age
        self.phone = phone
        self.address = address
        self.human_info = {"name": name, "surname": surname, "age": age, "phone": phone, "address": address}

    def print_info(self):
        print(self.human_info)

    def call(self, phone_number: str):
        print(f"{self.phone} is calling {phone_number}")


tom = Human("Tom", "Smith", 18, "+380987654321", "123")
tom.print_info()
tom.call("+3809123456789")

jack = Human("Jack", "Smith", 18, "+380684564567", "Peremogi")
jack.print_info()
jack.call("+380987654321")

jerry = Human("Jerry", "Smith", 18, "+380671515511","Yankees")
jerry.print_info()
jerry.call("+380987654321")