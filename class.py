# number_int = 123
# number_str = "456"

# print(type(number_int))  
# print(type(number_str))  

# number_str = int(number_str)
# print(type(number_str))

# number_sum = number_int + number_str
# print(number_sum)
# print(type(number_sum))




# a = 1001
# b = 1000 + 1

# print("a == b",a == b)
# print("a is b =", a is b)

# print(id(a));
# print(id(b));





a = ["Python", "Django"]
b = ["Python", "Django"]
c = a

print(a is c)
print(id(a));
print(id(c));
print(a is b);
print(id(a));
print(id(b));
# returns True because c is the same object as a
# print(a is b)
# returns False because a is not the same object as b, even if they have the same content
# print(a == b)
# to demonstrate the difference between "is" and "==": this comparison returns True because a is equal to y




a = 10
b = 30
print("a is not b = ",a is not b)
print(id(a));
print(id(b));