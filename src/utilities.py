from kivy.uix.popup import Popup
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.checkbox import CheckBox
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

# 전기요금 세부 설정 팝업
class ElectricitySettingsPopup(Popup):
    def __init__(self, parent_app, **kwargs):
        super().__init__(**kwargs)
        self.title = "전기요금 세부 설정"
        self.size_hint = (0.5, 0.8)
        self.parent_app = parent_app

        self.layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        # 전기요금 체크박스
        self.electricity_layout = GridLayout(cols=2, spacing=20)
        self.electricity_layout.add_widget(Label(text="전기요금", font_size=15, font_name="NanumGothic"))
        self.check_electricity = CheckBox()
        self.electricity_layout.add_widget(self.check_electricity)

        self.layout.add_widget(Label(text="전기요금 세부 설정", font_size=15, font_name="NanumGothic"))
        self.layout.add_widget(self.electricity_layout)

        # 확인 버튼 추가
        confirm_button = Button(text="확인", font_size=15, on_press=self.confirm_electricity, font_name="NanumGothic")
        self.layout.add_widget(confirm_button)

        self.add_widget(self.layout)

    def confirm_electricity(self, instance):
        # 팝업을 닫고 설정 값을 저장
        self.parent_app.electricity_settings = self.check_electricity.active
        self.dismiss()

# 가스요금 세부 설정 팝업
class GasSettingsPopup(Popup):
    def __init__(self, parent_app, **kwargs):
        super().__init__(**kwargs)
        self.title = "가스요금 세부 설정"
        self.size_hint = (0.5, 0.8)
        self.parent_app = parent_app

        self.layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        # 가스요금 체크박스
        self.gas_layout = GridLayout(cols=2, spacing=20)
        self.gas_layout.add_widget(Label(text="가스요금", font_size=15, font_name="NanumGothic"))
        self.check_gas = CheckBox()
        self.gas_layout.add_widget(self.check_gas)

        self.layout.add_widget(Label(text="가스요금 세부 설정", font_size=15, font_name="NanumGothic"))
        self.layout.add_widget(self.gas_layout)

        # 확인 버튼 추가
        confirm_button = Button(text="확인", font_size=15, on_press=self.confirm_gas, font_name="NanumGothic")
        self.layout.add_widget(confirm_button)

        self.add_widget(self.layout)

    def confirm_gas(self, instance):
        # 팝업을 닫고 설정 값을 저장
        self.parent_app.gas_settings = self.check_gas.active
        self.dismiss()

# 수도요금 세부 설정 팝업
class WaterSettingsPopup(Popup):
    def __init__(self, parent_app, **kwargs):
        super().__init__(**kwargs)
        self.title = "수도요금 세부 설정"
        self.size_hint = (0.5, 0.8)
        self.parent_app = parent_app

        self.layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        # 수도요금 체크박스
        self.water_layout = GridLayout(cols=2, spacing=20)
        self.water_layout.add_widget(Label(text="수도요금", font_size=15, font_name="NanumGothic"))
        self.check_water = CheckBox()
        self.water_layout.add_widget(self.check_water)

        self.layout.add_widget(Label(text="수도요금 세부 설정", font_size=15, font_name="NanumGothic"))
        self.layout.add_widget(self.water_layout)

        # 확인 버튼 추가
        confirm_button = Button(text="확인", font_size=15, on_press=self.confirm_water, font_name="NanumGothic")
        self.layout.add_widget(confirm_button)

        self.add_widget(self.layout)

    def confirm_water(self, instance):
        # 팝업을 닫고 설정 값을 저장
        self.parent_app.water_settings = self.check_water.active
        self.dismiss()
