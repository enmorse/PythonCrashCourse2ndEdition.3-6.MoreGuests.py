# Make a list that includes at least three people you
# would like to invite to dinner.

# Then use your list to print a message to each person,
# inviting them to dinner.

idol_guest_list = [
    "arnold schwarzenegger",
    "babe ruth",
    "sean connery"
]

invitation = f"Mr. {idol_guest_list[0].title()}, " \
             f"Mr. {idol_guest_list[1].title()}, and " \
             f"Mr. {idol_guest_list[2].title()}, I would like " \
             f"to invite you to dinner because " \
             f"\nyou are idols of mine and I have admired " \
             f"you and looked up to you sense I was a little " \
             f"boy."

print(invitation)

# You just heard that one of your guests can't make the
# dinner, so you need to send out a new set of
# invitations.You will have to think of someone else to
# invite.

# Start with your program from Exercise 3 - 4.
# Add a print() call at the end of your program stating
# the name of the guest who can not make it.

message = f"I am sorry to inform you but " \
          f"{idol_guest_list[1].title()} will not be able to " \
          f"make it for dinner."

print(message)

# Modify your list, replacing the name of the guest who
# can't make it with the name of the new person you
# are inviting.

idol_guest_list[1] = "keanu reeves"

print(idol_guest_list)

# Print a second set of invitation messages,
# one for each person who is still in your list.

invitation1 = f"Mr. {idol_guest_list[0].title()}, I would " \
              f"like to invite you to dinner because " \
              f"\nyou have been an idol of mine and I have " \
              f"admired you and looked up to you sense I " \
              f"was a little boy."
invitation2 = f"Mr. {idol_guest_list[1].title()}, I would " \
              f"like to invite you to dinner because " \
              f"\nyou have been an idol of mine and I have " \
              f"admired you and looked up to you sense I " \
              f"was a little boy."
invitation3 = f"Mr. {idol_guest_list[2].title()}, I would " \
              f"like to invite you to dinner because " \
              f"\nyou have been an idol of mine and I have " \
              f"admired you and looked up to you sense I " \
              f"was a little boy."

print(invitation1)
print(invitation2)
print(invitation3)

# You just found a bigger dinner table, so now more
# space is available. Think of three more guests to
# invite to dinner.

# Start with your program from Exercise 3 - 4 or 3 - 5.
# Add a print() call to the end of your program
# informing people that you found a bigger dinner table.

invitation4 = f"Mr. {idol_guest_list[0].title()}, Mr. " \
              f"{idol_guest_list[1].title()}," \
              f"\nand Mr. {idol_guest_list[2]}, I would like " \
              f"to inform you that I have found" \
              f"\na bigger dinner table and can now seat " \
              f"three more guests for dinner."

print(invitation4)

# Use the insert() function to add one new guest to the
# beginning of your list.

idol_guest_list.insert(0, "Harrison Ford")

print(idol_guest_list)

# Use the insert() function to add one new guest to the
# middle of your list.

idol_guest_list.insert(2, "Sylvester Stallone")

print(idol_guest_list)

# Use append to add one new guest to the end of your
# list.

idol_guest_list.append("Jean-Claude Van Damme")

print(idol_guest_list)

# Print a new set of invitation messages,
# one for each person.

invitation5 = f"Mr. {idol_guest_list[0].title()}, I would " \
              f"like to invite you to dinner because " \
              f"\nyou have been an idol of mine and I have " \
              f"admired you and looked up to you sense I " \
              f"was a little boy."
invitation6 = f"Mr. {idol_guest_list[1].title()}, I would " \
              f"like to invite you to dinner because " \
              f"\nyou have been an idol of mine and I have " \
              f"admired you and looked up to you sense I " \
              f"was a little boy."
invitation7 = f"Mr. {idol_guest_list[2].title()}, I would " \
              f"like to invite you to dinner because " \
              f"\nyou have been an idol of mine and I have " \
              f"admired you and looked up to you sense I " \
              f"was a little boy."
invitation8 = f"Mr. {idol_guest_list[3].title()}, I would " \
              f"like to invite you to dinner because " \
              f"\nyou have been an idol of mine and I have " \
              f"admired you and looked up to you sense I " \
              f"was a little boy."
invitation9 = f"Mr. {idol_guest_list[4].title()}, I would " \
              f"like to invite you to dinner because " \
              f"\nyou have been an idol of mine and I have " \
              f"admired you and looked up to you sense I " \
              f"was a little boy."
invitation10 = f"Mr. {idol_guest_list[5].title()}, I would " \
               f"like to invite you to dinner because " \
              f"\nyou have been an idol of mine and I have " \
               f"admired you and looked up to you sense I " \
               f"was a little boy."

print(invitation5)
print(invitation6)
print(invitation7)
print(invitation8)
print(invitation9)
print(invitation10)
