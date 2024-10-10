# Suppose you entered a building where there are (100+some_number) doors numbered from 1 to (100+some_number). 
# Here, "some_number" is just one number: there is no multiplication between the letters.
# At first, all of the doors are locked. (100+some_number) students are sent to change the state of the doors (from locked to unlocked or from unlocked to locked).
# The students act one after another, which means that second student starts after the first one, third student starts after the second one, etc.
# The first student unlocks all doors. The second student changes the state of every other door (2, 4, 6, ...).
# The third changes the state of every third door (3, 6, 9, ...). This process goes on until all (100+some_number) students have completed according to the rule.
# The problem is in finding all opened doors after all students pass through the building

# Input format: some_number - number of additional doors

# Output format: return the list of the doors' queue numbers

# First, we need to get the number of additional doors
while True:
    try:
        number_of_doors = 100 + int(input("Add more doors: ")) # add number of doors
        break
    except ValueError:
        print('Invalid number')
    
# Add list of doors which everyone is closed(FALSE)
doors = []
for _ in range(0, number_of_doors):
    doors.append(False)

# Create a function for change state of door
def open_or_close(index, state=False):
    doors[index] = state

#using loops, performed an action in which students open or close doors
for students in range(0, number_of_doors):
    for door_num in range(0, number_of_doors):
        if (door_num + 1) % (students + 1) == 0:
            open_or_close(door_num) if doors[door_num] else open_or_close(door_num, True)             

# Find all opened doors and convert into the list
print([index + 1 for index in range(0, len(doors)) if doors[index]])

















