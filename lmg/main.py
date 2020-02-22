#!/usr/bin/env python3

import kivy
kivy.require('1.11.0')

from kivy.app import App
from kivy.uix.widget import Widget


class MainWindow(Widget):
    def __init__(self):
        Widget.__init__(self)


class LMGApp(App):
    def build(self):
        return MainWindow()


if __name__ == '__main__':
    LMGApp().run()
