from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.label import Label  # Label 모듈 추가

import sys
import os

# 현재 파일이 위치한 디렉터리를 sys.path에 추가합니다.
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

        # 각 요금 클래스의 인스턴스 생성
        self.water_instance = Water()
        self.gas_instance = Gas()
        self.electricity_instance = Electricity()

        # 공과금 버튼 추가
        utility_button = Button(text="공과금 설정",
                                on_release=self.show_utility_popup, 
                                font_name="NanumGothic",
                                size_hint=(None, None), 
                                width=200, height=50)
        self.add_widget(utility_button)

    def show_utility_popup(self, instance):
        # Water, Gas, Electricity 입력 필드를 포함한 레이아웃 생성
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

        popup = Popup(title='공과금 설정', content=utility_layout, size_hint=(None, None), size=(400, 600))
        popup.open()