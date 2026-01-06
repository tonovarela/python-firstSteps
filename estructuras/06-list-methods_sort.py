
letters = [ 'a','b','c','d','e','z',"a"]
numbers=  [1,2,3,4,5,700,6,100,0,-5800,-1]


# new_letter = sorted(letters)
numbers.sort(reverse=True)
# print(letters)
# # print(new_letter)
# print(numbers)

new_letters = letters.copy()
new_letters.sort()
# print(new_letters)


new_letters.reverse()
# print(new_letters)

positive_numbers = [n for n in numbers if n>0 ]

print(sum(positive_numbers)/len(positive_numbers))







