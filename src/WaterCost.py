from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

class Water:
    def __init__(self):
        self.water_cost = 0.0
        self.water_layout = None
        self.p_water_using_input = None
        self.n_water_using_input = None

    def create_input_fields(self):
        self.water_layout = GridLayout(cols=2, spacing=10)
        
        self.water_layout.add_widget(Label(text="상수도 사용량", font_size=15, font_name="NanumGothic", size_hint_y=None, height=25))
        self.p_water_using_input = TextInput(multiline=False, input_filter='float', font_size=15)
        self.water_layout.add_widget(self.p_water_using_input)
        
        self.water_layout.add_widget(Label(text="하수도 배출량", font_size=15, font_name="NanumGothic", size_hint_y=None, height=25))
        self.n_water_using_input = TextInput(multiline=False, input_filter='float', font_size=15)
        self.water_layout.add_widget(self.n_water_using_input)

    def calculate_water(self):
        using_p_water = float(self.p_water_using_input.text) if self.p_water_using_input.text else 0
        using_n_water = float(self.n_water_using_input.text) if self.n_water_using_input.text else 0
        
        p_water_cost = using_p_water * 160
        
        if 1 < using_n_water <= 50:
            n_water_cost = using_n_water * 560
        elif 50 < using_n_water <= 100:
            n_water_cost = (using_n_water-50) * 730 + 28000 # 50 x 560
        elif using_n_water > 100:
            n_water_cost = (using_n_water-100) * 1070 + 64500   # 50 x 560 + 50 x 730
        else:
            n_water_cost = 0  
                                   
        self.water_cost = 229070 + p_water_cost + n_water_cost  # 일반용 계량기 구경: 200mm
        return self.water_cost
