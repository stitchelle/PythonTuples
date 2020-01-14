# 1. Create a tuple named zoo that contains 10 of your favorite animals.
# 2. Find one of your animals using the tuple.index(value) syntax on the tuple.

# Example
# flowers = ("daisy", "rose")
# flower.index("rose") # Output is 1

zoo = ("lion", "tiger", "bear", "monkey", "giraffe", "penquin", "panda", "red panda", "flamingo", "koala")

print("panda", zoo.index("panda"))

# 3. Determine if an animal is in your tuple by using value in tuple syntax.

# animal_to_find = "kangaroo"
# if animal_to_find in zoo:
     # Print that the animal was found

animal_to_find = "panda"
if animal_to_find in zoo:
    print("animal was found")

# 4. You can reverse engineer (unpack) a tuple into another tuple with the following syntax.

# children = ("Sally", "Hansel", "Gretel", "Svetlana")
# (first_child, second_child, third_child, fourth_child) = children
# print(first_child) # Output is "Sally"
# print(second_child) # Output is "Hansel"
# print(third_child) # Output is "Gretel"
# print(fourth_child) # Output is "Svetlana"

# Create a variable for the animals in your zoo tuple, and print them to the console.

animal = ("lion", "tiger", "bear", "monkey", "giraffe", "penquin", "panda", "red panda", "flamingo", "koala")
(first_animal, second_animal, third_animal, fourth_animal, fifth_animal, sixth_animal, seventh_animal, eighth_animal, ninth_animal, tenth_animal) = animal
print(first_animal)
print(second_animal)
print(third_animal)
print(fourth_animal)
print(fifth_animal)
print(sixth_animal)
print(seventh_animal)
print(eighth_animal)
print(ninth_animal)
print(tenth_animal)

# 5. Convert your tuple into a list.
zoo_list = list(zoo)
# 6. Use extend() to add three more animals to your zoo.
# another list of animals
animal1 = ['wolf', 'dingo', 'fox']

zoo_list.extend(animal1)

# Extended List
print('Animal List: ', zoo_list)

# 7. Convert the list back into a tuple.
zoo_tuple = tuple(zoo_list)
print('Animal Tuple:', zoo_tuple)