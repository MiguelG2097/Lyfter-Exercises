class Head:
    def __init__(self):
        pass

class Torso:
    def __init__(self, head, right_arm, left_arm):
        self.head = head
        self.right_arm = right_arm
        self.left_arm = left_arm


class Arm:
    def __init__(self, hand):
        self.hand = hand

class Hand():
    def __init__(self):
        pass

class Leg:
    def __init__(self, feet):
        self.feet = feet


class Feet:
    def __init__(self):
        pass

class Human:
    def __init__(self, torso, right_leg, left_leg):
        self.torso = torso
        self.right_leg = right_leg
        self.left_leg = left_leg



right_hand = Hand()
left_hand = Hand()

right_arm = Arm(right_hand)
left_arm = Arm(left_hand)

head = Head()

torso = Torso(head, right_arm, left_arm)

right_feet = Feet()
left_feet = Feet()

right_leg = Leg(right_feet)
left_leg = Leg(left_feet)

human = Human(torso, right_leg, left_leg)