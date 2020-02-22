#!/usr/bin/env python3

import kivy
kivy.require('1.11.0')

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.widget import Widget


class MainWidget(BoxLayout):
    game_button = None

    def __init__(self):
        BoxLayout.__init__(self, orientation='vertical')

        self.setup_widget()

    def setup_widget(self):
        self.game_button = Button(text="Start game")


class MainWindow(BoxLayout):
    current_widget = None

    current_game_time_label = None

    def __init__(self):
        BoxLayout.__init__(self, orientation='vertical')

        self.time = 100

        self.setup_widget()

    def setup_widget(self):
        self.current_game_time_label = Label(pos=(0, 0), size=(self.width / 2, 30))

        self.set_game_times()
        self.current_widget = MainWidget()

        self.add_widget(self.current_game_time_label)
        self.add_widget(self.current_widget)

        self.current_game_time_label.pos = (0, 0)
        self.current_widget.pos = (0, 30)

    def on_main_widget(self):
        self.current_widget = MainWidget()

        self.current_widget.game_button.bind()

    def on_resize(self):
        self.current_widget.size(self.size)

    def on_timer_timeout(self):
        pass

    def set_game_times(self):
        hours = int(self.time / (60 * 60))
        minutes = int((self.time - hours * (60 * 60)) / 60)
        seconds = int(self.time - (hours * 60 * 60 + minutes * 60))

        if hours < 10:
            hours = "0" + str(hours)

        if minutes < 10:
            minutes = "0" + str(minutes)

        if seconds < 10:
            seconds = "0" + str(seconds)

        self.current_game_time_label.text = "Current game time: " + str(hours) + ":" + str(minutes) + ":" + str(seconds)


class LMGApp(App):
    def build(self):
        window = MainWindow()
        window.size = (600, 400)

        return window


if __name__ == '__main__':
    LMGApp().run()
