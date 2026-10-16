### Set the data for the exercice

my_list = [1, 5, "4", "six", 3.14]

##########################################################""
### Part A.

#name of the error : ValueError

new_list = []

for value in my_list:
    # Check if the current value can be turned into an int
    try:
        inter = int(value)
        # Add the new value to the new list
        new_list.append(inter)

    except ValueError:
        print(f"The current value({value}) can not be converted into an integer")

#print(new_list)


############################################################"
### part B.

def clean_list(used_list):
    int_list = []
    for value in used_list:
    # Check if the current value can be turned into an int
        try:
            inter = int(value)
            # Add the new value to the new list
            int_list.append(inter)

        except ValueError:
            print(f"The current value({value}) can not be converted into an integer")

    return int_list

# replace the new_list from part A to a new new_list (erase it content)
new_list = clean_list(my_list)
print(new_list, "from part B")


################################################################################"
### Part C.
place_cnt = 0
# Create the new list
neighbour = []
for number in new_list:
    # Stop the loop if there is no more second number to add
    if place_cnt < len(my_list)-2:
        # Recover the next value
        place_cnt +=1
        # Calculate the sum
        local_sum = number + new_list[place_cnt]
        neighbour.append(local_sum)

print(neighbour)

