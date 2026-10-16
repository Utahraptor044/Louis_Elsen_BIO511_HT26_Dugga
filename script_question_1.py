########################################################"
# 
### Part A.

#Create a variable that save my name
my_name = "Louis"


### Part B.

# Calculate the length of my name
len_my_name = len(my_name)

#print the result
print(len_my_name)

### Part C.

# letter i is chosen
cnt_i = 0
for letter in my_name:
    if letter == 'i':
        cnt_i += 1

print(f"There is {cnt_i} time the letter \"i\" in my name") 