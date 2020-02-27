
class MinusException(Exception):
    def __str__(self):
        return "you cant withdraw more that you have"
