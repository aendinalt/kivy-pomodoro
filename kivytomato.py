__author__ = 'Aen Dinalt'

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.config import Config
from kivy.uix.floatlayout import FloatLayout





class LargeIconWidget(Widget):
    def __init__(self, **kwargs):
        super(LargeIconWidget, self).__init__(**kwargs)


class StartButton(Widget):
    def __init__(self, **kwargs):
        super(StartButton, self).__init__(**kwargs)


class StopButton(Widget):
    def __init__(self, **kwargs):
        super(StopButton, self).__init__(**kwargs)


class ClearButton(Widget):
    def __init__(self, **kwargs):
        super(ClearButton, self).__init__(**kwargs)


class CherryGood(Widget):
    def __init__(self, **kwargs):
        super(CherryGood, self).__init__(**kwargs)


class TomatoLayout(FloatLayout):
    pass



class TomatoApp(App):
    def build(self):
        Config.set('graphics', 'width', '400')
        Config.set('graphics', 'height', '400')
        return TomatoLayout()

if __name__ == '__main__':
    TomatoApp().run()
