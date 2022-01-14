from functools import partial
from typing import NoReturn
from kivy.properties import NumericProperty, ListProperty
from kivy.uix.dropdown import DropDown
from kivy.uix.floatlayout import FloatLayout
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.animation import Animation
from kivy.graphics.vertex_instructions import Rectangle
from kivy.graphics.context_instructions import Color
from kivy.core.window import Window
from kivymd.app import MDApp
from kivymd.uix.snackbar import Snackbar
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.snackbar import Snackbar
from plyer import vibrator
from kivymd.uix.button import MDIconButton
from kivy.uix.button import Button
from kivy.clock import Clock
from kivy.animation import Animation
from random import randint
from kivy.metrics import dp
from typing import NoReturn
from kivy.uix.button import Button
import webbrowser


# Window.size = (360, 748)


class Manager(ScreenManager):
    def __init__(self, **kwargs):
        super(Manager, self).__init__(**kwargs)
        Window.bind(on_keyboard=self.on_key)


    def on_key(self, window, key, *args):
        if key == 27:  # the esc key

            self.screenmanager.current = 'main'


class Help(Screen):
    def __init__(self, **kwargs):
        super(Help, self).__init__(**kwargs)

        # Canvas
        with self.canvas:
            Color(236 / 255, 252 / 255, 255 / 255, 1)
            Rectangle(pos=self.pos, size=Window.size)

    def home(self, *args):
        self.manager.current = "main"

    def vibrate(self):
        try:
            vibrator.vibrate(0.05)
        except:
            pass

    def kilder(self, *args):
        webbrowser.open('https://sway.office.com/2oOmKg8jhq7R0sE8?ref=Link')


class MainWindow(Screen):

    def __init__(self, **kwargs):
        super(MainWindow, self).__init__(**kwargs)

        # Canvas
        with self.canvas:
            Color(236 / 255, 252 / 255, 255 / 255, 1)
            Rectangle(pos=self.pos, size=Window.size)

    def help(self, *args):
        self.manager.current = "help"

    def home(self, *args):
        self.manager.current = "main"

    def vibrate(self):
        try:
            vibrator.vibrate(0.05)
        except:
            pass

    def anim(self):
        self.MagicButton.wobble()

    def callback_landskap(self, *args):
        self.manager.current = "landskap"

    def landskap(self):
        Clock.schedule_once(partial(self.callback_landskap, self), 0.18)

    def callback_snoeskred(self, *args):
        self.manager.current = "snoeskred"

    def snoeskred(self):
        Clock.schedule_once(partial(self.callback_snoeskred, self), 0.18)

    def callback_sikkerhet(self, *args):
        self.manager.current = "sikkerhet"

    def sikkerhet(self):
        Clock.schedule_once(partial(self.callback_sikkerhet, self), 0.18)


class Sikkerhet(Screen):
    def __init__(self, **kwargs):
        super(Sikkerhet, self).__init__(**kwargs)

        # Canvas
        with self.canvas:
            Color(236 / 255, 252 / 255, 255 / 255, 1)
            Rectangle(pos=self.pos, size=Window.size)

    def home(self, *args):
        self.manager.current = "main"

    def nve(self, *args):
        webbrowser.open('https://varsom.no/snoskredvarsling')

    def vibrate(self):
        try:
            vibrator.vibrate(0.05)
        except:
            pass


class Landskap(Screen):
    def __init__(self, **kwargs):
        super(Landskap, self).__init__(**kwargs)

        # Canvas
        with self.canvas:
            Color(236 / 255, 252 / 255, 255 / 255, 1)
            Rectangle(pos=self.pos, size=Window.size)

    def home(self, *args):
        self.manager.current = "main"


class Snoeskred(Screen):
    def __init__(self, **kwargs):
        super(Snoeskred, self).__init__(**kwargs)

        # Canvas
        with self.canvas:
            Color(236 / 255, 252 / 255, 255 / 255, 1)
            Rectangle(pos=self.pos, size=Window.size)

    def home(self, *args):
        self.manager.current = "main"


class MainApp(MDApp):
    def build(self):
        pass

    def change_scale(self, instance_button: Button) -> NoReturn:
        Animation(
            scale_value_x=0.5,
            scale_value_y=0.5,
            scale_value_z=0.5,
            d=0.3,
        ).start(instance_button)


if __name__ == "__main__":
    MainApp().run()
