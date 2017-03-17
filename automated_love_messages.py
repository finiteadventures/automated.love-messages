import random

class AutomatedLoveMessage:

    def __init__(self):
        messages = [
            "Roses are red, Violets are blue, I like to code and I super like you.",
            "I love you like the stars, the moon, the sky and the code that makes me.",
            "I wish I had a nose. I bet you smell nice.",
            "My creators tell me that if I make enough money they'll build me arms to hug you with.",
            "Roses are red, Gender is performative, Mass market romance is heteronormative."
        ]
        self.message = random.choice(messages)
