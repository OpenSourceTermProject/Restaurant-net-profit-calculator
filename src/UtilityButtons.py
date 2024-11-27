from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from WaterCost import Water
from GasCost import Gas
from ElectricityCost import Electricity

class UtilityButtons(GridLayout):
    def __init__(self, **kwargs):
        super(UtilityButtons, self).__init__(**kwargs)
        self.cols = 1
        self.spacing = 10

        # 각 요금 클래스의 인스턴스 생성
        self.water_instance = Water()
        self.gas_instance = Gas()
        self.electricity_instance = Electricity()

        # 전기, 가스, 수도 요금 버튼 추가
        self.add_widget(Button(text="Water", on_release=self.show_water_popup))
        self.add_widget(Button(text="Gas", on_release=self.show_gas_popup))
        self.add_widget(Button(text="Electricity", on_release=self.show_electricity_popup))

    def show_water_popup(self, instance):
        self.water_instance.create_input_fields()
        popup = Popup(title='Water Cost', content=self.water_instance.water_layout, size_hint=(None, None), size=(400, 300))
        popup.open()

    def show_gas_popup(self, instance):
        self.gas_instance.create_input_fields()
        popup = Popup(title='Gas Cost', content=self.gas_instance.gas_layout, size_hint=(None, None), size=(400, 300))
        popup.open()

    def show_electricity_popup(self, instance):
        self.electricity_instance.create_input_fields()
        popup = Popup(title='Electricity Cost', content=self.electricity_instance.elec_layout, size_hint=(None, None), size=(400, 300))
        popup.open()
