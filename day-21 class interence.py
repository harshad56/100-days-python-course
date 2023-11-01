class animal:
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("inhale,exhale")


class fish(animal):      # inhertance method is used
    def __init__(self):   # another class is called by this method
        super().__init__()  # uses another class  functions

    def breathe(self):
        super().breathe()  # inhertance method is used
        print("doing this underwater")

    def swim(self):
        print("moving in water.")


nemo = fish()

nemo.swim()
nemo.breathe()
print(nemo.num_eyes)
