# 파이썬을 3.8버전 혹은 3.9버전으로 downgrade 시켜줘야 
# KIVY가 정상적으로 설치 및 실행이 됩니다.

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.checkbox import CheckBox
from kivy.uix.button import Button
from kivy.core.text import LabelBase

from kivy.config import Config
Config.set('modules', 'touchring', '0')
Config.set('input', 'mouse', 'mouse,disable_multitouch')

# 한글 폰트 등록
LabelBase.register(name="NanumGothic", fn_regular="NanumGothic-ExtraBold.ttf")

class RestaurantCalculatorApp(App):
    def build(self):
        main_layout = BoxLayout(orientation='vertical', padding=20, spacing=20)
        
        # 연 매출액 및 식자재비 입력
        input_layout = GridLayout(cols=3, spacing=10)
        input_layout.add_widget(Label(text="연 매출액", font_size=15, font_name="NanumGothic"))
        self.sales_input = TextInput(multiline=False, font_size=15)
        input_layout.add_widget(self.sales_input)
        input_layout.add_widget(Label(text="원", font_size=15, font_name="NanumGothic"))

        input_layout.add_widget(Label(text="식자재비", font_size=15, font_name="NanumGothic"))
        self.material_cost_input = TextInput(multiline=False, font_size=15)
        input_layout.add_widget(self.material_cost_input)
        input_layout.add_widget(Label(text="원", font_size=15, font_name="NanumGothic"))

        main_layout.add_widget(input_layout)

        # 주문 중개처 (체크박스)
        intermediary_layout = GridLayout(cols=3, spacing=20, padding=[0, 20, 0, 0])
        intermediary_layout.add_widget(Label(text="배달의민족", font_size=15, font_name="NanumGothic"))
        intermediary_layout.add_widget(Label(text="요기요", font_size=15, font_name="NanumGothic"))
        intermediary_layout.add_widget(Label(text="쿠팡이츠", font_size=15, font_name="NanumGothic"))

        self.check_baemin = CheckBox()
        self.check_yogiyo = CheckBox()
        self.check_coupangeats = CheckBox()

        intermediary_layout.add_widget(self.check_baemin)
        intermediary_layout.add_widget(self.check_yogiyo)
        intermediary_layout.add_widget(self.check_coupangeats)

        main_layout.add_widget(Label(text="주문 중개처", font_size=15, halign="center", font_name="NanumGothic"))
        main_layout.add_widget(intermediary_layout)

        # 비용 출력 부분
        output_layout = GridLayout(cols=3, spacing=10)
        self.insurance_label = self.create_output_row("보험료", output_layout)
        self.tax_label = self.create_output_row("세금", output_layout)
        self.intermediary_fee_label = self.create_output_row("주문 중개 수수료", output_layout)
        self.payment_processing_fee_label = self.create_output_row("결제 대행 수수료", output_layout)
        self.utilities_label = self.create_output_row("공과금", output_layout)
        self.expected_net_profit_label = self.create_output_row("예상 순이익", output_layout)

        main_layout.add_widget(output_layout)
        
        # 계산 버튼 추가
        calculate_button = Button(text="계산하기", font_size=15, on_press=self.calculate_net_profit, font_name="NanumGothic")
        main_layout.add_widget(calculate_button)

        return main_layout
    
    def create_output_row(self, label_text, layout):
        layout.add_widget(Label(text=label_text, font_size=15, font_name="NanumGothic"))
        output_label = Label(text="0", font_size=15, font_name="NanumGothic")
        layout.add_widget(output_label)
        layout.add_widget(Label(text="원", font_size=15, font_name="NanumGothic"))
        return output_label

    def calculate_net_profit(self, instance):
        # 여기서 입력값을 가져와서 순이익을 계산할 수 있습니다.
        try:
            sales = float(self.sales_input.text)
            material_cost = float(self.material_cost_input.text)
            
            # 각 항목의 비용을 간단히 계산하는 예시 (사용자 정의로 변경 가능)
            insurance = sales * 0.01  # 예: 매출의 1%를 보험료로 가정
            tax = sales * 0.1         # 예: 매출의 10%를 세금으로 가정
            intermediary_fee = 0.05 * sales if self.check_baemin.active else 0
            intermediary_fee += 0.04 * sales if self.check_yogiyo.active else 0
            intermediary_fee += 0.03 * sales if self.check_coupangeats.active else 0
            payment_processing_fee = sales * 0.02  # 예: 매출의 2%를 결제 수수료로 가정
            utilities = sales * 0.005               # 예: 매출의 0.5%를 공과금으로 가정

            # 순이익 계산
            net_profit = sales - (material_cost + insurance + tax + intermediary_fee + payment_processing_fee + utilities)

            # 결과 출력
            self.insurance_label.text = f"{insurance:,.0f}"
            self.tax_label.text = f"{tax:,.0f}"
            self.intermediary_fee_label.text = f"{intermediary_fee:,.0f}"
            self.payment_processing_fee_label.text = f"{payment_processing_fee:,.0f}"
            self.utilities_label.text = f"{utilities:,.0f}"
            self.expected_net_profit_label.text = f"{net_profit:,.0f}"
        except ValueError:
            self.expected_net_profit_label.text = "입력 오류"

if __name__ == "__main__":
    RestaurantCalculatorApp().run()
