from string import ascii_lowercase
data = input("Enter data: ")
data = data.split(",")
# Delete point from last element
data[-1] = data[-1][:len(data[-1])-1]
# Each word transform to set and take a union of all sets
general_set = set()
for el in data:
    general_set = general_set.union(set(el))
# Set of vowels
vowels = {'a', "e", "i", "o", "u", "y"}
# Add vowelf to general set to make sure we dont count them
general_set = general_set.union(vowels)
# And take difference between alphabet and general_set
print(set(ascii_lowercase).difference(general_set))