from abstract_factory.interfaces import Button, Checkbox, GUIFactory


class MacButton(Button):
    def paint(self):
        print("Rendering a Mac-style button")

class MacCheckbox(Checkbox):
    def paint(self):
        print("Rendering a Mac-style checkbox")

class MacFactory(GUIFactory):
    def create_button(self) -> Button:
        return MacButton()

    def create_checkbox(self) -> Checkbox:
        return MacCheckbox()