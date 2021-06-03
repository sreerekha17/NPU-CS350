# Problem #3:
# In the simulation of a card game playing, Card class needs to be created first. And the constructor of it takes three arguments:
# the name of the card, a string
# the attack stat of the card, an integer
# the defense stat of the card, an integer

# Each Card instance should keep track of these values using instance attributes called name, attack, and defense.
# And the power method in Card should be implemented, which takes in another card as an input and calculates the current card's power. The following notice shows how power is calculated.

# class Card:
#     cardtype = 'Staff'

#     def __init__(self, name, attack, defense):
#                                 """
#         Create a Card object with a name, attack and defense.
        
#         staff_member = Card('staff', 400, 300)
#         staff_member.name
#         'staff'
        
#        staff_member.attack
#         400
        
#         staff_member.defense
#         300
        
#         other_staff = Card('other', 300, 500)
#         other_staff.attack
#         300
#         other_staff.defense
#         500
#         """
#         """ Write your program here"""



#     def power(self, opponent_card):
#         """
#         Calculate power as:
#         (player card's attack) - (opponent card's defense)/2

#         staff_member = Card('staff', 400, 300)
#         other_staff = Card('other', 300, 500)
#         staff_member.power(other_staff)
#         150.0			# 400 – 500/2 = 150.0

#         other_staff.power(staff_member)
#         150.0			# 300 – 300/2 = 150.0
        
#         third_card = Card('third', 200, 400)
#         staff_member.power(third_card)
#         200.0			# 400– 400/2 = 200.0
#         third_card.power(staff_member)
#         50.0			# 200– 300/2 = 50.0
#         """
#         """ Write your program here"""

# Notice:
# Each played card's power value is calculated as follows:
# (player card's attack) - (opponent card's defense) / 2
# For example, let's say Player 1 plays a card with 2000 attack/1000 defense and Player 2 plays a card with 1500 attack/3000 defense. Their cards' powers are calculated as:
# P1: 2000 - 3000/2 = 2000 - 1500 = 500
# P2: 1500 - 1000/2 = 1500 - 500 = 1000
# So Player 2 would win this round.


class Card():
    cardType = 'Staff'
    def __init__(self, name, attack, defense): #name of card(str), attack stat(int), defense stat(int)
        self.name = name
        self.attack = attack
        self.defense = defense

    def power(self, opponent_card):
       return self.attack - (opponent_card.defense/2)


staff_member = Card('staff', 400, 300)
print(staff_member.name)                    # staff
print(staff_member.attack)                  # 400
print(staff_member.defense)                 # 300

other_staff = Card('other', 300, 500)
print(other_staff.attack)                   # 300
print(other_staff.defense)                  # 500

print(staff_member.power(other_staff))      # 150.0
print(other_staff.power(staff_member))      # 150.0


third_card = Card('third', 200, 400)
print(staff_member.power(third_card))        # 200.0
print(third_card.power(staff_member))        # 50