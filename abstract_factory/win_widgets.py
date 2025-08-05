from abstract_factory.interfaces import Button, Checkbox, GUIFactory


class WinButton(Button):
    def paint(self):
        print("Rendering a Win-style button")

class WinCheckbox(Checkbox):
    def paint(self):
        print("Rendering a Win-style checkbox")

class WinFactory(GUIFactory):
    def create_button(self) -> Button:
        return WinButton()

    def create_checkbox(self) -> Checkbox:
        return WinCheckbox()