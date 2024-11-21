# main.py는 프로그램 전반적으로 사용되는 것들만 정의합니다.
# 세부적인 기능은 src 폴더 내에 새로운 클래스 파일에 구현 해주세요.


# 클래스 파일 Import
# ---- 보험료 / 세금 ----
from src.Insurance import Insurance
from src.Insurance import InsuranceSettingsPopup
from src.Tax import Tax

# ---- 공과금 / 수수료 ----
from src.Fee import Fee
from src.ElectricitySettingsPopup import ElectricitySettingsPopup
from src.GasSettingsPopup import GasSettingsPopup
from src.WaterSettingsPopup import WaterSettingsPopup

# ---- 비용 입력 ----
from src.CostInput import CostInput

# ---- 결과 출력 ----
from src.ResultOutput import ResultOutput

# Kivy 라이브러리 Import
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.core.text import LabelBase
from kivy.uix.button import Button

from kivy.config import Config
Config.set('modules', 'touchring', '0')
Config.set('input', 'mouse', 'mouse,disable_multitouch')

# 한글 폰트 등록
LabelBase.register(name="NanumGothic", fn_regular="NanumGothic-ExtraBold.ttf")

class RootWidget(Widget):
    def __init__(self, **kwargs):
        # 주요 레이아웃
        self.main_layout = BoxLayout(orientation='vertical', padding=20, spacing=20)
        self.input_layout = GridLayout(cols=3, spacing=10)

        # 위젯 객체 생성
        self.costInput = CostInput(self.main_layout, self.input_layout) # 입력
        self.insurance = Insurance(self.main_layout)  # 보험 객체 생성
        self.fee = Fee(self.main_layout)  # 수수료
        self.resultOutput = ResultOutput(self.main_layout, self.input_layout, self.costInput, self.fee, self.insurance)  # 보험 객체 전달

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


# 이 안에 직접 기능 구현하지 말고 각각 클래스 파일에서 구현한 후, rootWidget에 객체 생성해서 하나씩 붙여주세요.
class RestaurantCalculatorApp(App):
    # 최종 위젯
    rootWidget = RootWidget()

    def build(self):
        # 최종 위젯
        self.rootWidget = RootWidget()

        return self.rootWidget.main_layout # 루트 위젯의 메인 레이아웃 출력

if __name__ == "__main__":
    RestaurantCalculatorApp().run()