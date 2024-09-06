# q3.py

#
# Full Name: Hanzala Yousuf Mahmood     
#  SFU ID #: 301623949
# SFU Email: hym7@sfu.ca
#

# ... put your answer to question 3 here ...

message = input("Please write you message in here ")
character = input("What charcater do you want to use? ")

box_length = len(message) + 4

# you would think +2 would work but you need to use +4 

print(box_length * character)
print(f"{character} {message} {character}")
print(box_length * character)
