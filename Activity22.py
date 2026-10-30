class Robot:
    """A blueprint representing a Robot."""

    def __init__(self, name, model, color, battery=100):
    
        self.name = name
        self.model = model
        self.color = color
        self.battery = battery

    def introduce_self(self):
        """Method for the robot to introduce itself."""
        print(
            f"Hey! I am {self.name}, a {self.color} {self.model} model."
        )
        print(f"My current battery level is {self.battery}%.")

    
my_robot = Robot(name="Elie", model="AW-67", color="blue", battery=98)
my_robot.introduce_self()