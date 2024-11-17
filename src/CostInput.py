from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

# 연 매출액 및 식자재비 입력
class CostInput(Widget):
    def __init__(self, main_layout, input_layout, **kwargs):
        super(CostInput, self).__init__(**kwargs)

        self.main_layout = main_layout
        self.input_layout = input_layout

        self.input_layout.add_widget(Label(text="연 매출액", font_size=15, font_name="NanumGothic"))
        self.sales_input = TextInput(multiline=False, font_size=15)
        self.input_layout.add_widget(self.sales_input)
        self.input_layout.add_widget(Label(text="원", font_size=15, font_name="NanumGothic"))

        self.input_layout.add_widget(Label(text="식자재비", font_size=15, font_name="NanumGothic"))
        self.material_cost_input = TextInput(multiline=False, font_size=15)
        self.input_layout.add_widget(self.material_cost_input)
        self.input_layout.add_widget(Label(text="원", font_size=15, font_name="NanumGothic"))

        self.main_layout.add_widget(self.input_layout)