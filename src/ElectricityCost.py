from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

class Electricity:
    def __init__(self):
        self.elec_cost = 0.0
        self.elec_layout = None
        self.elec_using_input = None

    def create_input_fields(self):
        self.elec_layout = GridLayout(cols=2, spacing=10)
        
        self.elec_layout.add_widget(Label(text="전력 사용량", font_size=15, font_name="NanumGothic", size_hint_y=None, height=25))
        self.elec_using_input = TextInput(multiline=False, input_filter='float', font_size=15)
        self.elec_layout.add_widget(self.elec_using_input)

    def calculate_electricity(self):
        # 값을 가져와 계산
        using_elec = float(self.elec_using_input.text) if self.elec_using_input.text else 0
        
        self.elec_cost = using_elec * 6160 # 일반용 전력 kw당 6160원 - 24년 10월 24일 적용
        return self.elec_cost