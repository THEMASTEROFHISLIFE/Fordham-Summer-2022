#Nicholas Clarke
#July 30, 2022
#HW_7, Pet Class Ch.10 Programming Exercise

#class named Pet, which should have the following:
##  _ _name(for the name of a pet)
##  _ _animal_type(for the type of animal that a pet is. Example values are 'Dog', 'Cat', and 'Bird')
##  _ _age (for the pet's age)

### Pet class should have an _ _innit_ _ method for these attributes.

### Have the following methods:

# o set_name  [check]

    ##this assigns a value to the _ _name field

# o set_animal_type

    ##this assigns a value to the _ _animal_type field

# o set_age

    ##this assigns a value to the _ _age field

# o get_name

    ##this assigns a value to the _ _name field

# o get_animal_type

    ##this assigns a value to the _ _animal_type field

# o get_age

    ##this assigns a value to the _ _age field





# !!! Once written, write a program that creates an object of the class and prompts the user to enter the name, type and age of his/her pet
# %%% STORE DATA as OBJECT'S ATTRIBUTE
# @@@ Use the object's accessor methods to retrieve the pet's name, type, age. Display data on screen



def main():

        p_name = input('pet name: ')
        p_type = input('pet type: ')
        p_age  = int(input(' age:   '))

        object_pet = (p_name, p_type, p_age)

        print(object_pet)

main()

    




#PET CLASS
class PET:
    def __innit__(self, name, animal_type, age):
        self.__name = name
        self.__animal_type = animal_type
        self.__age = age


##    def set__name(self, name):
##        self.__name = name
##
##    def set__animal__type (self, animal_type):
##        self.__animal__type = animal_type
##
##    def set__age (self, age):
##        self.__age = age
        #get
##    def get__name(self):
##        return self.__name
##    def get_animal_type(self):
##        return self._animal_type
##    def get__age(self):
##        return self.__age

        
#pet program
