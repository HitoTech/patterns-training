from command.light_command import LightOnCommand, LightOffCommand
from remote import RemoteControl
from devices import Light

# Initialization
light = Light()
remote = RemoteControl()

# Turns the light on
on_command = LightOnCommand(light)
remote.set_command(on_command)
remote.press_button()

# Turns the light off
off_command = LightOffCommand(light)
remote.set_command(off_command)
remote.press_button()