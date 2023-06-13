import operator

class Animal:
    def __init__(self, name, age, specie, sex):
        self.name = name
        self.age = age
        self.specie = specie
        self.sex = sex

    def __str__(self):
        return "{0}, {1}, {2}, {3}".format(self.name, str(self.age), self.specie, self.sex)  #printar ut info om djuren

    def __lt__(self, other): #funktion för att sortera efter yngst ålder först och för att få äldst först så används reverse i den andra filen
        return self.age < other.age


animal_dict = {}


def read_file(): #läser in text filen med information på djuren
    my_file = open("djur_i_park.txt", "r")
    for line in my_file:
        text_info = line.split(", ") #separerar djuren och replace tar bort onödiga mellanrum i textfilen
        name = text_info[0]
        age = text_info[1]
        specie = text_info[2]
        sex = text_info[3]
        animal_dict[name] = Animal(name, int(age), specie, sex)
    return

def get_int_input(prompt_string): #felhantering för int värden
    done = False
    while not done:
        try:
            user_input = int(input(prompt_string))
        except ValueError:
            print('Ange ett korrekt alternativ... Försök igen!')
        else:
            return (user_input)


def menu(): #printar ut menyn med val
    print("\n" + "Välkommen till djurparken!" +
          2 *"\n" + "Alternativ: " +
          "\n" + "1. Sök efter ett djur" +
          "\n" + "2. Visa alla djur som finns i parken" +
          "\n" + "3. Sälj ett djur" +
          "\n" + "4. Lägg till ett djur i parken" +
          "\n" + '5. Sortera Djuren' +
          "\n" + "6. Avsluta")
    return


def menu_choice(): #används för att göra val i execute funktionen
    choice = get_int_input("Ange ditt val 1-6: ")
    return (choice)


def execute(choice): #kör koden för alternativen från menyn, utifrån input från användaren
        if choice == 1:
            search_Animal()
        elif choice == 2:
            animals_in_park()
        elif choice == 3:
            sell_animal()
        elif choice == 4:
            add_animal()
        elif choice == 5:
            sort_animals()


def search_Animal(): #funktion för att söka efter djur baserat på önskad parameter
    search_choice = get_int_input("Vilken parameter vill du söka efter?\n1. Namn\n2. Ålder\n3. Djurart\n4. Kön\nAnge alternativ: ")
    if search_choice == 1:
        key = input("Namn: ").capitalize() #capitalize gör första bokstaven till en stor bokstav
        if key in animal_dict:
            print(animal_dict[key])
        else:
            print(key + " finns inte i parken...")
    elif search_choice == 2: #sorterar efter ålder och printar ut alla djur som är den åldern som användare skriver in i age_input
        age_input = get_int_input("Ålder: ")
        for animal in (sorted(animal_dict.values(), key=operator.attrgetter('age'))):
            if age_input == animal.age:
                print(animal.name + ", " + str(age_input) + " år")
    elif search_choice == 3:
        specie_input = input("Djurart: ").capitalize() #samma som i ovanstående fast för specie(dvs djurart)
        for animal in (sorted(animal_dict.values(), key=operator.attrgetter('specie'))):
                if specie_input == animal.specie:
                    print(animal.name + " är en " + specie_input)
    elif search_choice == 4:
        sex_input = input("Ange kön på djuren: ").capitalize() #samma princip igen, fast printar ut alla djur som är av samma kön i parken
        for animal in (sorted(animal_dict.values(), key=operator.attrgetter('specie'))):
            if sex_input == animal.sex:
                print(animal.name + " är en " + sex_input)
            else:
                return(execute(1))


def animals_in_park():
    for key in animal_dict:
        print(animal_dict[key])


def sell_animal(): #tar bort/säljer djur, använder pop för att ta bort djuret ur parken.
    name = input("Namn på djuret som ska säljas: ").capitalize()
    if name in animal_dict:
        animal_dict.pop(name) #tar bort djuret ur parken
        print(name + " såldes!")
        return animal_dict
    else:
        print("Djuret finns inte i parken...")


def add_animal():
    key = input("Namn:").capitalize()
    if key not in animal_dict:
        age = get_int_input("Ålder: ")
        specie = input("Djur: ").capitalize()
        sex = input("Kön: ").capitalize()
        animal_dict[key] = Animal(key, age, specie, sex + "\n")
        print(str(animal_dict[key]) + " lades till i parken!")
    elif key in animal_dict: #om ett djur med namnet finns i parken printas printen nedan ut
        print("Ett djur med namnet finns redan i parken...")


def sort_animals(): #funktion för att sortera djuren efter önskad parameter
    sort_input = get_int_input("1. Sortera efter bokstavsordning\n2. Sortering efter yngst\n3. Äldst i parken \n4. Sortering efter djurart \nAnge 1-4 för vilken sortering som önskas: ") #tar in input för typ av sortering
    if sort_input == 1:
        print("\nBokstavsordning:")
        for animal in (sorted(animal_dict.values(), key=operator.attrgetter('name'))):
            print(animal.name)
    elif sort_input == 2:
        sort_youngest = sorted(animal_dict, key=animal_dict.__getitem__) #använder inbygda __lt__ funktionen i Animal för att sortera efter yngst
        print("Yngst först: " + str(sort_youngest))
    elif sort_input == 3:
        sort_oldest = sorted(animal_dict, key=animal_dict.__getitem__, reverse= True) #samma som i ovan, fast äldst först, genom reverse kommando
        print("Äldst först: " + str(sort_oldest))
    elif sort_input == 4:
        for animal in (sorted(animal_dict.values(), key=operator.attrgetter('specie'))):
            print(animal.name + ", " + animal.specie)
    else:
        execute(5)


def main(): #while-loop som körs till choice 6 är givet
    read_file()
    while True:
        menu()
        choice = menu_choice()
        if choice != 6:
            execute(choice)
        else:
            with open("/Users/admin/Desktop/Simon_Toblad_P-Upg/djur_i_park.txt", "w+") as my_file: #skriver förändringarna i parkens djur till textfilen
                for key in animal_dict:
                    my_file.write(str(animal_dict[key]))
            print("Avslutar programmet...")
            break


if __name__ == "__main__":
    main()
