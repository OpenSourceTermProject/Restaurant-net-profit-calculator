from kivy.uix.popup import Popup
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

class GasSettingsPopup(Popup):
    def __init__(self, main_layout, **kwargs):
        super().__init__(**kwargs)
        self.title = "GasSetting"
        self.size_hint = (0.5, 0.8)
        self.main_layout = main_layout
        self.gas_settings_result = 0 # 계산 결과
        
        self.layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        # 가스요금 숫자 입력
        self.gas_layout = GridLayout(cols=2, spacing=20)

        # 첫 번째 항목 - 사용량
        self.gas_layout.add_widget(Label(text="사용량", font_size=15, font_name="NanumGothic", size_hint_y=None, height=25))
        self.usage_input = TextInput(multiline=False, input_filter='float', font_size=15)  # 숫자 입력 필터
        self.gas_layout.add_widget(self.usage_input)

        # 두 번째 항목 - 보정계수
        self.gas_layout.add_widget(Label(text="보정계수", font_size=15, font_name="NanumGothic", size_hint_y=None, height=25))
        self.correction_factor_input = TextInput(multiline=False, input_filter='float', font_size=15)  # 숫자 입력 필터
        self.gas_layout.add_widget(self.correction_factor_input)

        # 세 번째 항목 - 평균열량
        self.gas_layout.add_widget(Label(text="평균열량", font_size=15, font_name="NanumGothic", size_hint_y=None, height=25))
        self.average_energy_input = TextInput(multiline=False, input_filter='float', font_size=15)  # 숫자 입력 필터
        self.gas_layout.add_widget(self.average_energy_input)

        # 네 번째 항목 - 계기손료
        self.gas_layout.add_widget(Label(text="계기손료", font_size=15, font_name="NanumGothic", size_hint_y=None, height=25))
        self.instrument_cost_input = TextInput(multiline=False, input_filter='float', font_size=15)  # 숫자 입력 필터
        self.gas_layout.add_widget(self.instrument_cost_input)

        self.layout.add_widget(Label(text="가스요금 세부 설정", font_size=15, font_name="NanumGothic"))
        self.layout.add_widget(self.gas_layout)

        # 확인 버튼 추가
        confirm_button = Button(text="확인", font_size=15, on_press=self.confirm_gas, font_name="NanumGothic")
        self.layout.add_widget(confirm_button)

        self.add_widget(self.layout)
    
    def confirm_gas(self, instance):
        # 값을 가져와 계산
        usage = float(self.usage_input.text) if self.usage_input.text else 0
        correction_factor = float(self.correction_factor_input.text) if self.correction_factor_input.text else 0
        average_energy = float(self.average_energy_input.text) if self.average_energy_input.text else 0
        instrument_cost = float(self.instrument_cost_input.text) if self.instrument_cost_input.text else 0

        # 계산 (사용량 x 보정계수) x 평균열량 x 요금단가 + 계기손료 + 부가세 (10%)
        total_cost = ((usage * correction_factor) * average_energy * 23.105 + instrument_cost) * 1.1

        # 계산 결과 저장
        self.gas_settings_result = total_cost

        # 팝업 닫기
        self.dismiss()
