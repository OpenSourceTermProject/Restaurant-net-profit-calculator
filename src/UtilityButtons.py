from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.label import Label

import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from WaterCost import Water
from GasCost import Gas
from ElectricityCost import Electricity

class UtilityButtons(GridLayout):
    def __init__(self, main_layout, **kwargs):
        super(UtilityButtons, self).__init__(**kwargs)
        self.cols = 1
        self.spacing = 10
        self.main_layout = main_layout

        self.water_instance = Water()
        self.gas_instance = Gas()
        self.electricity_instance = Electricity()

        self.popup = None  # 클래스 변수로 popup 초기화

        utility_button = Button(text="공과금 설정",
                                on_release=self.show_utility_popup, 
                                font_name="NanumGothic",
                                size_hint=(None, None), 
                                width=200, height=50)
        self.add_widget(utility_button)

    def show_utility_popup(self, instance):
        self.water_instance.create_input_fields()
        self.gas_instance.create_input_fields()
        self.electricity_instance.create_input_fields()

        utility_layout = GridLayout(cols=1, spacing=10)
        utility_layout.add_widget(Label(text="상수도 및 하수도", font_size=15, font_name="NanumGothic"))
        utility_layout.add_widget(self.water_instance.water_layout)
        utility_layout.add_widget(Label(text="도시가스", font_size=15, font_name="NanumGothic"))
        utility_layout.add_widget(self.gas_instance.gas_layout)
        utility_layout.add_widget(Label(text="전력", font_size=15, font_name="NanumGothic"))
        utility_layout.add_widget(self.electricity_instance.elec_layout)

        calculate_button = Button(text="계산하기",
                                  on_release=self.calculate_utilities,
                                  font_name="NanumGothic",
                                  size_hint=(None, None),
                                  width=200, height=50)
        utility_layout.add_widget(calculate_button)

        self.popup = Popup(title='공과금 설정', content=utility_layout, size_hint=(None, None), size=(400, 600), title_font="NanumGothic")
        self.popup.open()

    def calculate_utilities(self, instance):
        total_water_cost = self.water_instance.calculate_water()
        total_gas_cost = self.gas_instance.calculate_gas()
        total_electricity_cost = self.electricity_instance.calculate_electricity()

        total_cost = total_water_cost + total_gas_cost + total_electricity_cost

        # 팝업 닫기
        self.popup.dismiss()

        # 계산된 결과 반환
        return total_cost
