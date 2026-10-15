from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

class Root(BoxLayout):
    def __init__(self, **kw):
        super().__init__(orientation="vertical", padding=40, spacing=20, **kw)
        self.n = 0
        self.lbl = Label(text="Нажатий: 0", font_size="32sp")
        btn = Button(text="Нажми", size_hint_y=0.3)
        btn.bind(on_press=self.tap)
        self.add_widget(self.lbl)
        self.add_widget(btn)

    def tap(self, *_):
        self.n += 1
        self.lbl.text = f"Нажатий: {self.n}"

class MyApp(App):
    def build(self):
        return Root()

MyApp().run()
