from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

class Gas:
    def __init__(self):
        self.gas = 0.0
        self.gas_layout = None
        self.gas_using_input = None

    def create_input_fields(self):
        self.gas_layout = GridLayout(cols=2, spacing=10)
        
        self.gas_layout.add_widget(Label(text="도시가스 사용량", font_size=15, font_name="NanumGothic", size_hint_y=None, height=25))
        self.gas_using_input = TextInput(multiline=False, input_filter='float', font_size=15)
        self.gas_layout.add_widget(self.gas_using_input)

    def calculate_gas(self):
        # 값을 가져와 계산
        using_gas = float(self.gas_using_input.text) if self.gas_using_input.text else 0
        
        base_cost = (using_gas**2) * 23.105  # 기본 요금 계산
        vat = base_cost * 0.1  # 부가세 10% 계산
        self.gas_cost = base_cost + vat  # 총 비용 계산

        return self.gas_cost