import math

'''
A gigantic pie is split amongst 100 guests

1st guest gets 1% of the pie
2nd guest gets 2% of the remaining pie
3rd guest gets 3% of the remaining pie, ...
last guest gets 100% of the rest

Who has the largest piece of pie?
'''

guests = []
remaining_pie = 100
#for each guest
for i in range(1, 101):
    guest_portion = (i/100)*remaining_pie
    guests.append(guest_portion)
    #update remaining_pie
    remaining_pie = remaining_pie - guest_portion

print("Guest portions: ", guests)

largest_portion = 0
for i in range(0, len(guests)):
    if (guests[i] > largest_portion):
        largest_portion = guests[i]
        guest_id = i+1

print("Largest portion of {}% goes to guest {}".format(largest_portion, guest_id))
