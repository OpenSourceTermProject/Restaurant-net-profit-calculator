from kivy.uix.popup import Popup
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

class WaterSettingsPopup(Popup):
    def __init__(self, main_layout, **kwargs):
        super().__init__(**kwargs)
        self.title = "WaterSetting"
        self.size_hint = (0.5, 0.8)
        self.main_layout = main_layout
        
        self.layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        # 수도요금 숫자 입력
        self.water_layout = GridLayout(cols=2, spacing=10)

        # 첫 번째 항목 - 상수도요금
        self.water_layout.add_widget(Label(text="상수도 사용량", font_size=15, font_name="NanumGothic", size_hint_y=None, height=25))
        self.usage_input = TextInput(multiline=False, input_filter='float', font_size=15)  # 숫자 입력 필터
        self.water_layout.add_widget(self.usage_input)

        # 두 번째 항목 - 하수도요금
        self.water_layout.add_widget(Label(text="하수도 사용량", font_size=15, font_name="NanumGothic", size_hint_y=None, height=25))
        self.correction_factor_input = TextInput(multiline=False, input_filter='float', font_size=15)  # 숫자 입력 필터
        self.water_layout.add_widget(self.correction_factor_input)

        # 세 번째 항목 - 구경
        self.water_layout.add_widget(Label(text="구경 (mm)", font_size=15, font_name="NanumGothic", size_hint_y=None, height=25))
        self.diameter_input = TextInput(multiline=False, input_filter='float', font_size=15)  # 숫자 입력 필터
        self.water_layout.add_widget(self.diameter_input)

        self.layout.add_widget(Label(text="수도요금 세부 설정", font_size=15, font_name="NanumGothic"))
        self.layout.add_widget(self.water_layout)

        # 확인 버튼 추가
        confirm_button = Button(text="확인", font_size=15, on_press=self.confirm_water, font_name="NanumGothic")
        self.layout.add_widget(confirm_button)

        self.add_widget(self.layout)
    
    def confirm_water(self, instance):
        # 상수도, 하수도 사용량, 구경을 가져옴

        water_usage = float(self.usage_input.text) if self.usage_input.text else 0
        sewer_usage = float(self.correction_factor_input.text) if self.correction_factor_input.text else 0
        diameter = float(self.diameter_input.text) if self.diameter_input.text else 0

        # 요금 계산
        total_cost = self.calculate_total_water_sewer_bill(water_usage, sewer_usage, diameter)

        # 결과를 main_layout에 저장
        self.main_layout.water_settings_result = total_cost

        # 팝업 닫기
        self.dismiss()

    
    def calculate_total_water_sewer_bill(self, water_usage, sewer_usage, diameter):
        """상수도 요금과 하수도 요금을 계산 후 합산하는 함수"""
        
        # 상수도 요금 계산
        if water_usage <= 50:
            water_bill = 620
        elif water_usage <= 100:
            water_bill = 1040
        else:
            water_bill = 1040  # 101 이상은 동일

        # 물 이용 부담금 (미터제곱당 160원)
        water_usage_fee = water_usage * 160

        # 하수도 요금 계산
        if sewer_usage <= 50:
            sewer_bill = 560
        elif sewer_usage <= 100:
            sewer_bill = 730
        else:
            sewer_bill = 1070  # 101 이상은 동일

        # 구경에 따른 요금 조정 
        if diameter == 15:
            diameter_fee = 860
        elif diameter == 20:
            diameter_fee = 2420
        elif diameter == 25:
            diameter_fee = 3890 
        elif diameter == 32:
            diameter_fee = 7540
        elif diameter == 40:
            diameter_fee = 11670
        elif diameter == 50:
            diameter_fee = 18520
        elif diameter == 80:
            diameter_fee = 43410
        elif diameter == 100:
            diameter_fee = 74020
        elif diameter == 150:
            diameter_fee = 161270
        elif diameter == 200:
            diameter_fee = 229070
        elif diameter == 250:
            diameter_fee = 308970
        elif diameter == 300:
            diameter_fee = 372610 
        elif diameter == 400:
            diameter_fee = 510450 
        else:
            diameter_fee = 0

        # 상수도 요금 + 물 이용 부담금 + 하수도 요금 + 구경에 따른 요금
        total_bill = water_bill + water_usage_fee + sewer_bill + diameter_fee
        return total_bill
    