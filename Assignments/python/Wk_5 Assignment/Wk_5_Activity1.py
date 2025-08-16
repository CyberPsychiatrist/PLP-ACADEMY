class Smartphone:
    """A simple smartphone."""

    def __init__(self, model, screen_size, camera, battery):
        self.model = model
        self.screen_size = screen_size
        self.camera = camera
        self.battery = battery
        self.is_on = False  # Is the phone turned on?

    def turn_on(self):
        """Turns the phone on."""
        if not self.is_on:
            self.is_on = True
            print(f"{self.model} is on!")
            print(f"{self.model} is already on.")

        else:
            print(f"{self.model} is already on!")

    def turn_off(self):
        """Turns the phone off."""
        if self.is_on:
            self.is_on = False
            print(f"{self.model} is off.")
        else:
            print(f"{self.model} is already off.")

    def show_info(self):
        print(f"Screen: {self.screen_size} inches")
        print(f"Battery: {self.battery} mAh")
        print(f"Camera: {self.camera}")
        print(f"Status: {'On' if self.is_on else 'Off'}")  # Show phone status

# Create and use the phone
my_phone = Smartphone("AwesomePhone X", 6.5, "48MP", 5000)
my_phone.show_info()
my_phone.turn_on()
my_phone.show_info()
my_phone.turn_off()
my_phone.show_info()