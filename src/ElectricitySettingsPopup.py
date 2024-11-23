from kivy.uix.popup import Popup
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout


class ElectricitySettingsPopup(Popup):
    def __init__(self, main_layout, **kwargs):
        super().__init__(**kwargs)
        self.title = "ElectricitySetting"
        self.size_hint = (0.5, 0.9)
        self.main_layout = main_layout
        self.electric_settings_result = 0

        self.layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        # 전기요금 금액 입력
        self.electricity_layout = GridLayout(cols=2, spacing=10)
        
        # 첫 번째 항목 - 영업비용
        self.electricity_layout.add_widget(Label(text="영업비용", font_size=15, font_name="NanumGothic", size_hint_y=None, height=25))
        self.electricity_cost_input1 = TextInput(multiline=False, input_filter='float', font_size=15)
        self.electricity_layout.add_widget(self.electricity_cost_input1)

        # 두 번째 항목 - 적정법인세비용
        self.electricity_layout.add_widget(Label(text="적정법인세비용", font_size=15, font_name="NanumGothic", size_hint_y=None, height=25))
        self.electricity_cost_input2 = TextInput(multiline=False, input_filter='float', font_size=15)
        self.electricity_layout.add_widget(self.electricity_cost_input2)

        # 세 번째 항목 - 순설비가액
        self.electricity_layout.add_widget(Label(text="순설비가액", font_size=15, font_name="NanumGothic", size_hint_y=None, height=25))
        self.electricity_cost_input3 = TextInput(multiline=False, input_filter='float', font_size=15)
        self.electricity_layout.add_widget(self.electricity_cost_input3)

        # 네 번째 항목 - 건설중인자산
        self.electricity_layout.add_widget(Label(text="건설중인자산", font_size=15, font_name="NanumGothic", size_hint_y=None, height=25))
        self.electricity_cost_input4 = TextInput(multiline=False, input_filter='float', font_size=15)
        self.electricity_layout.add_widget(self.electricity_cost_input4)

        # 다섯 번째 항목 - 운전자금
        self.electricity_layout.add_widget(Label(text="운전자금", font_size=15, font_name="NanumGothic", size_hint_y=None, height=25))
        self.electricity_cost_input5 = TextInput(multiline=False, input_filter='float', font_size=15)
        self.electricity_layout.add_widget(self.electricity_cost_input5)

        # 여섯 번째 항목 - 자기 자본 보수율
        self.electricity_layout.add_widget(Label(text="자기 자본 보수율", font_size=15, font_name="NanumGothic", size_hint_y=None, height=25))
        self.electricity_cost_input6 = TextInput(multiline=False, input_filter='float', font_size=15)
        self.electricity_layout.add_widget(self.electricity_cost_input6)

        # 일곱 번째 항목 - 타인 자본 보수율
        self.electricity_layout.add_widget(Label(text="타인 자본 보수율", font_size=15, font_name="NanumGothic", size_hint_y=None, height=25))
        self.electricity_cost_input7 = TextInput(multiline=False, input_filter='float', font_size=15)
        self.electricity_layout.add_widget(self.electricity_cost_input7)

        self.layout.add_widget(Label(text="전기요금 세부 설정", font_size=15, font_name="NanumGothic"))
        self.layout.add_widget(self.electricity_layout)

        # 확인 버튼 추가
        confirm_button = Button(text="확인", font_size=15, on_press=self.confirm_electircity, font_name="NanumGothic")
        self.layout.add_widget(confirm_button)

        self.add_widget(self.layout)

    
    def confirm_electircity(self, instance):
        # 값을 가져와 계산
        cost1 = float(self.electricity_cost_input1.text) if self.electricity_cost_input1.text else 0
        cost2 = float(self.electricity_cost_input2.text) if self.electricity_cost_input2.text else 0
        cost3 = float(self.electricity_cost_input3.text) if self.electricity_cost_input3.text else 0
        cost4 = float(self.electricity_cost_input4.text) if self.electricity_cost_input4.text else 0
        cost5 = float(self.electricity_cost_input5.text) if self.electricity_cost_input5.text else 0
        cost6 = float(self.electricity_cost_input6.text) if self.electricity_cost_input6.text else 0
        cost7 = float(self.electricity_cost_input7.text) if self.electricity_cost_input7.text else 0

        # 계산 (영업비용 + 적정 법인세 비용) + ((순설비가액 + 건설 중인 자산 + 운전 자금) x (자기 자본 보수율 + 타인 자본 보수율))
        total_cost = (cost1 + cost2) + (cost3 + cost4 + cost5) * (cost6 + cost7)

        # 계산 결과 저장
        self.electric_settings_result = total_cost

        # 팝업 닫기
        self.dismiss()
