class Evaluation:
    def __init__(self, value):
        self.value = value
        
    def __str__(self):
        return "<Evaluation object of value: {}>".format(self.value)