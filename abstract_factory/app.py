from interfaces import GUIFactory

def paint(factory: GUIFactory):
    factory.create_button().paint()
    factory.create_checkbox().paint()