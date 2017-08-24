class Animal():
    noise = None
    bio_class = "Mammal" or "Bird"
    name = None

    def check_bio_class(self):
        print(self.bio_class)

    def make_noise(self):
        print(self.noise)

    def set_animal_name(self):
        self.name = input("Введите имя:\n")
        return Animal.name


class Cow(Animal):
    bio_class = "Mammal"
    name = "Mumu"
    noise = "Mooo"


class Goose(Animal):
    bio_class = "123"
    noise = "Quack"
    name = Animal.set_animal_name()


cow_1 = Cow()
goose_1 = Goose()

# goose_1.set_animal_name()



