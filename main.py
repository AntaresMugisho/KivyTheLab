from kivy.app import App
from kivy.graphics import Line, Color, Rectangle, Ellipse
from kivy.metrics import dp
from kivy.properties import StringProperty, BooleanProperty, Clock
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.widget import Widget


class CanvasExample7(BoxLayout):
    pass

class CanvasExample5(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.ball_size = dp(50)
        self.vx = dp(3)
        self.vy = dp(4)

        with self.canvas:
            self.ball = Ellipse(pos=(100, 100), size=(self.ball_size, self.ball_size))

        Clock.schedule_interval(self.update, 1/60)

    def on_size(self, *args):
        #print("on size : " + str(self.width) + ", " + str(self.height))
        self.ball.pos = (self.center_x - self.ball_size/2, self.center_y - self.ball_size/2 )

    def update(self, dt):
        x, y = self.ball.pos
        x += self.vx
        y += self.vy

        if x + self.ball_size > self.width:
            x = self.width - self.ball_size
            self.vx = -self.vx
        if x < 0:
            self.vx = -self.vx

        if y + self.ball_size > self.height:
            y = self.height - self.ball_size
            self.vy = -self.vy
        if y < 0:
            self.vy = -self.vy

        self.ball.pos = (x, y)



class CanvasExample4(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with self.canvas:
            Line(points=(0, 0, 100, 100))
            Line(circle=(200, 200, 40), width=2)
            Color(rgb=(0, 1, 0))
            Line(rectangle=(200, 400, 150, 100))
            self.rect = Rectangle(pos=(300, 50), size=(dp(150), dp(75)))

    def on_btn_a_click(self):
        x, y = self.rect.pos
        w, h = self.rect.size
        inc = dp(10)

        diff = self.width - (x+w)
        if diff < inc:
            inc = diff

        x += inc
        self.rect.pos = (x, y)


class CanvasExample3(Widget):
    pass

class CanvasExample2(Widget):
    pass

class CanvasExample1(Widget):
    pass

class WidgetsExample(GridLayout):
    my_text = StringProperty("1")
    count_enabled = BooleanProperty(False)
    count = 1
    slider_value_txt = StringProperty("1")
    text_input_str = StringProperty("foo")

    def on_btn_click(self):
        if self.count_enabled:
            self.count += 1
            self.my_text = str(self.count)

    def on_toggle_state(self, widget):
        print(widget.state)
        if widget.state == "normal":
            widget.text = "OFF"
            self.count_enabled = False

        else:
            widget.text = "ON"
            self.count_enabled = True

    def on_switch_active(self, widget):
        print("Switch: " + str(widget.active))

    #def on_slider_value(self, widget):
    #   self.slider_value_txt = str(int(widget.value))

    def on_text_validate(self, widget):
        self.text_input_str = widget.text



class StackLayoutExample(StackLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        for i in range(0, 200):
            # size = dp(100) + i*10
            size = dp(100)
            b = Button(text=str(i+1), size_hint=(None, None), size=(size, size))
            self.add_widget(b)

#class GridLayoutExample(GridLayout):
#    pass

class AnchorLayoutExample(AnchorLayout):
    pass

class BoxLayoutExample(BoxLayout):
    pass
    #def __init__(self, **kwargs):
    #    super().__init__(**kwargs)

    #    self.orientation = "vertical"

    #    b1 = Button(text="A")
    #    b2 = Button(text="B")

    #    self.add_widget(b1)
    #    self.add_widget(b2)


class MainWidget(Widget):
    pass

class TheLabApp(App):
    pass

TheLabApp().run()