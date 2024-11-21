from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

from src.ElectricitySettingsPopup import ElectricitySettingsPopup
from src.GasSettingsPopup import GasSettingsPopup
from src.WaterSettingsPopup import WaterSettingsPopup


class UtilityButtons(Widget):
    def __init__(self, main_layout, **kwargs):
        super().__init__(**kwargs)
        self.main_layout = main_layout

        # 각 공과금 설정 팝업 객체 할당
        self.electricitySettingsPopup = ElectricitySettingsPopup(self.main_layout)
        self.gasSettingsPopup = GasSettingsPopup(self.main_layout)
        self.waterSettingsPopup = WaterSettingsPopup(self.main_layout)

        # 공과금 설정 버튼들을 담을 BoxLayout (가로로 배치)
        utility_button_layout = BoxLayout(orientation='horizontal', size_hint_y=None, height=40, spacing=10)

        # 전기 설정 버튼
        electricity_button = Button(
            text="전기 요금 설정", font_size=15, on_press=self.open_electricity_popup, font_name="NanumGothic"
        )
        utility_button_layout.add_widget(electricity_button)

        # 가스 설정 버튼
        gas_button = Button(
            text="가스 요금 설정", font_size=15, on_press=self.open_gas_popup, font_name="NanumGothic"
        )
        utility_button_layout.add_widget(gas_button)

        # 수도 설정 버튼
        water_button = Button(
            text="수도 요금 설정", font_size=15, on_press=self.open_water_popup, font_name="NanumGothic"
        )
        utility_button_layout.add_widget(water_button)

        # 공과금 버튼 레이아웃을 main_layout에 추가
        self.main_layout.add_widget(utility_button_layout)

    def open_electricity_popup(self, instance):
        self.electricitySettingsPopup.open()

    def open_gas_popup(self, instance):
        self.gasSettingsPopup.open()

    def open_water_popup(self, instance):
        self.waterSettingsPopup.open()
