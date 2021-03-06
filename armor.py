import random


class Armor:
    """
    creates a heroes armor
    """

    def __init__(self, name, max_block):
        """
        initilizes instance attributes.
        """
        self.name = name
        self.max_block = max_block

    def block(self):
        """
        Return a random value between 0 and the
        initialized max_block strength.
        """
        random_block_value = random.randint(0, self.max_block)
        return random_block_value


