# 파이썬을 3.8버전 혹은 3.9버전으로 downgrade 시켜줘야 
# KIVY가 정상적으로 설치 및 실행이 됩니다.

from Tax import Tax
from Insurance import Insurance
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.checkbox import CheckBox
from kivy.uix.button import Button
from kivy.core.text import LabelBase
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button as DropDownButton
from kivy.uix.popup import Popup

from kivy.config import Config
Config.set('modules', 'touchring', '0')
Config.set('input', 'mouse', 'mouse,disable_multitouch')

# 한글 폰트 등록
LabelBase.register(name="NanumGothic", fn_regular="NanumGothic-ExtraBold.ttf")

class InsuranceSettingsPopup(Popup):
    def __init__(self, parent_app, **kwargs):
        super().__init__(**kwargs)
        self.title = "Insurance Settings"
        self.size_hint = (0.5, 0.8)
        self.parent_app = parent_app

        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        #4대보험 가입여부 체크박스
        MajorInsurance_layout = GridLayout(cols=2, spacing=20)
        MajorInsurance_layout.add_widget(Label(text="고용보험", font_size=15, font_name="NanumGothic"))
        self.check_employment = CheckBox()
        MajorInsurance_layout.add_widget(self.check_employment)


        MajorInsurance_layout.add_widget(Label(text="산재보험", font_size=15, font_name="NanumGothic"))
        self.check_industrial = CheckBox()
        MajorInsurance_layout.add_widget(self.check_industrial)

        layout.add_widget(Label(text="4대보험 가입 여부(가입시 체크)", font_size=15, font_name="NanumGothic"))
        layout.add_widget(MajorInsurance_layout)

        #의무보험 가입여부 체크박스
        c_insurance_layout = GridLayout(cols=2, spacing=20)
        c_insurance_layout.add_widget(Label(text="다중이용업소화재보험", font_size=15, font_name="NanumGothic"))
        self.check_multi = CheckBox()
        c_insurance_layout.add_widget(self.check_multi)


        c_insurance_layout.add_widget(Label(text="재난보험", font_size=15, font_name="NanumGothic"))
        self.check_disaster = CheckBox()
        c_insurance_layout.add_widget(self.check_disaster)

        c_insurance_layout.add_widget(Label(text="가스사고보험", font_size=15, font_name="NanumGothic"))
        self.check_gas = CheckBox()
        c_insurance_layout.add_widget(self.check_gas)

        layout.add_widget(Label(text="의무보험 가입 여부(가입시 체크)", font_size=15, halign="left", font_name="NanumGothic"))
        layout.add_widget(c_insurance_layout)

        #확인 버튼 추가
        confirm_button = Button(text="확인", font_size=15, on_press=self.confirm_insurance, font_name="NanumGothic")
        layout.add_widget(confirm_button)

        self.add_widget(layout)
    
    def confirm_insurance(self, instance):
        # 팝업을 닫고 보험 가입 여부를 저장
        self.parent_app.insurance_selections = {
            "employment": self.check_employment.active,
            "industrial": self.check_industrial.active,
            "multi": self.check_multi.active,
            "disaster": self.check_disaster.active,
            "gas": self.check_gas.active,
        }
        self.dismiss()


class RestaurantCalculatorApp(App):
    def build(self):
        self.insurance_selections = {}  # 보험 가입 여부 저장할 딕셔너리

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

        # 결제 대행
        intermediary_layout = GridLayout(cols=6, spacing=20, padding=[0, 20, 0, 0])
        intermediary_layout.add_widget(Label(text="헥토파이낸셜", font_size=15, font_name="NanumGothic"))
        intermediary_layout.add_widget(Label(text="토스페이먼츠", font_size=15, font_name="NanumGothic"))
        intermediary_layout.add_widget(Label(text="이니시스", font_size=15, font_name="NanumGothic"))
        intermediary_layout.add_widget(Label(text="KCP", font_size=15, font_name="NanumGothic"))
        intermediary_layout.add_widget(Label(text="카카오페이", font_size=15, font_name="NanumGothic"))
        intermediary_layout.add_widget(Label(text="나이스페이", font_size=15, font_name="NanumGothic"))

        self.check_hecto = CheckBox()
        self.check_toss = CheckBox()
        self.check_inicis = CheckBox()
        self.check_KCP = CheckBox()
        self.check_kakao = CheckBox()
        self.check_nice = CheckBox()

        intermediary_layout.add_widget(self.check_hecto)
        intermediary_layout.add_widget(self.check_toss)
        intermediary_layout.add_widget(self.check_inicis)
        intermediary_layout.add_widget(self.check_KCP)
        intermediary_layout.add_widget(self.check_kakao)
        intermediary_layout.add_widget(self.check_nice)

        main_layout.add_widget(Label(text="결제 대행처", font_size=15, halign="center", font_name="NanumGothic"))
        main_layout.add_widget(intermediary_layout)

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

        # 보험료 세부 설정 버튼 추가
        insurance_settings_button = Button(text="보험료 세부 설정", font_size=15, on_press=self.open_insurance_settings, font_name="NanumGothic")
        main_layout.add_widget(insurance_settings_button)
        
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
    
    # 매출 구간에 따른 수수료율을 반환하는 함수
    def get_commission_rates(self, sales):
        if sales <= 300000000:
            return {
                'hecto': 0.016, 'toss': 0.019, 'inicis': 0.019, 
                'KCP': 0.0192, 'kakao': 0.017, 'nice': 0.023
            }
        elif sales <= 500000000:
            return {
                'hecto': 0.022, 'toss': 0.024, 'inicis': 0.025, 
                'KCP': 0.0252, 'kakao': 0.023, 'nice': 0.028
            }
        elif sales <= 1000000000:
            return {
                'hecto': 0.024, 'toss': 0.025, 'inicis': 0.0256, 
                'KCP': 0.0267, 'kakao': 0.0245, 'nice': 0.029
            }
        elif sales <= 3000000000:
            return {
                'hecto': 0.026, 'toss': 0.027, 'inicis': 0.029, 
                'KCP': 0.0292, 'kakao': 0.027, 'nice': 0.031
            }
        else:
            return {
                'hecto': 0.029, 'toss': 0.032, 'inicis': 0.032, 
                'KCP': 0.035, 'kakao': 0.032, 'nice': 0.032
            }
    
    # 결제 대행사 수수료 계산 함수
    def calculate_payment_processing_fee(self, sales, rates):
        payment_processing_fee = 0
        if self.check_hecto.active:
            payment_processing_fee += rates['hecto'] * sales
        if self.check_toss.active:
            payment_processing_fee += rates['toss'] * sales
        if self.check_inicis.active:
            payment_processing_fee += rates['inicis'] * sales
        if self.check_KCP.active:
            payment_processing_fee += rates['KCP'] * sales
        if self.check_kakao.active:
            payment_processing_fee += rates['kakao'] * sales
        if self.check_nice.active:
            payment_processing_fee += rates['nice'] * sales
        return payment_processing_fee

    def open_insurance_settings(self, instance):
        popup = InsuranceSettingsPopup(self)
        popup.open()

    def calculate_net_profit(self, instance):
        # 여기서 입력값을 가져와서 순이익을 계산할 수 있습니다.
        try:
            sales = float(self.sales_input.text)
            material_cost = float(self.material_cost_input.text)
            rates = self.get_commission_rates(sales)

            # 결제 수수료 계산
            payment_processing_fee = self.calculate_payment_processing_fee(sales, rates)
            
            # 공과금 계산
            utilities = sales * 0.005  # 예: 매출의 0.5%를 공과금으로 가정
            # 각 항목의 비용을 간단히 계산하는 예시 (사용자 정의로 변경 가능)
            intermediary_fee = 0.05 * sales if self.check_baemin.active else 0
            intermediary_fee += 0.04 * sales if self.check_yogiyo.active else 0
            intermediary_fee += 0.03 * sales if self.check_coupangeats.active else 0
            utilities = sales * 0.005               # 예: 매출의 0.5%를 공과금으로 가정
            insurance = Insurance(sales, material_cost, 
                                  self.insurance_selections.get("employment", False), 
                                  self.insurance_selections.get("industrial", False), 
                                  self.insurance_selections.get("multi", False), 
                                  self.insurance_selections.get("disaster", False), 
                                  self.insurance_selections.get("gas", False))      ############# 두번째 값 다 완성후 수정필요 필요경비 싹다 넣어야함 식자재+a
            tax = sales * 0.1         #예: Tax(sales, 모든경비(보험도포함))

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