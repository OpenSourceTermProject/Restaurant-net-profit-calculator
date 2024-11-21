# 클래스 파일 Import
# ---- 보험료 / 세금 ----
from src.Insurance import Insurance
# ---- 보험료 / 세금 ----

from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button

# 결과 출력
class ResultOutput(Widget):
    def __init__(self, main_layout, input_layout, costInput, fee, insurance, **kwargs):  # 보험 객체 추가
        super(ResultOutput, self).__init__(**kwargs)
        self.main_layout = main_layout
        self.input_layout = input_layout
        self.costInput = costInput
        self.fee = fee
        self.insurance = insurance  # 보험 객체 저장
        
        # 비용 출력 부분
        self.output_layout = GridLayout(cols=3, spacing=10)
        self.insurance_label = self.create_output_row("보험료", self.output_layout)
        self.tax_label = self.create_output_row("세금", self.output_layout)
        self.intermediary_fee_label = self.create_output_row("주문 중개 수수료", self.output_layout)
        self.payment_processing_fee_label = self.create_output_row("결제 대행 수수료", self.output_layout)
        self.utilities_label = self.create_output_row("공과금", self.output_layout)
        self.expected_net_profit_label = self.create_output_row("예상 순이익", self.output_layout)

        self.main_layout.add_widget(self.output_layout)

        # 계산 버튼 추가
        calculate_button = Button(text="계산하기", font_size=15, on_press=self.calculate_net_profit,
                                  font_name="NanumGothic")
        self.main_layout.add_widget(calculate_button)

    def create_output_row(self, label_text, layout):
        layout.add_widget(Label(text=label_text, font_size=15, font_name="NanumGothic"))
        output_label = Label(text="0", font_size=15, font_name="NanumGothic")
        layout.add_widget(output_label)
        layout.add_widget(Label(text="원", font_size=15, font_name="NanumGothic"))
        return output_label

    def calculate_net_profit(self, instance):
        # 여기서 입력값을 가져와서 순이익을 계산할 수 있습니다.
        try:
            sales = float(self.costInput.sales_input.text)
            material_cost = float(self.costInput.material_cost_input.text)
            rates = self.fee.get_commission_rates(sales)

            # 결제 수수료 계산
            payment_processing_fee = self.fee.calculate_payment_processing_fee(sales, rates)

            # 공과금 계산
            utilities = sales * 0.005  # 예: 매출의 0.5%를 공과금으로 가정
            # 각 항목의 비용을 간단히 계산하는 예시 (사용자 정의로 변경 가능)
            intermediary_fee = 0.05 * sales if self.fee.check_baemin.active else 0
            intermediary_fee += 0.04 * sales if self.fee.check_yogiyo.active else 0
            intermediary_fee += 0.03 * sales if self.fee.check_coupangeats.active else 0
            utilities = sales * 0.005  # 예: 매출의 0.5%를 공과금으로 가정
            insurance_states = self.insurance.insurance_selections  # 상태 가져오기
            insurance = Insurance.calc_insurance(
                sales,
                material_cost,
                insurance_states.get("employment", False),
                insurance_states.get("industrial", False),
                insurance_states.get("multi", False),
                insurance_states.get("disaster", False),
                insurance_states.get("gas", False),
            ) ############# 두번째 값 다 완성후 수정필요 필요경비 싹다 넣어야함 식자재+a
            
            tax = sales * 0.1  # 예: Tax(sales, 모든경비(보험도포함))

            # 순이익 계산
            net_profit = sales - (
                    material_cost + insurance + tax + intermediary_fee + payment_processing_fee + utilities)

            # 결과 출력
            self.insurance_label.text = f"{insurance:,.0f}"
            self.tax_label.text = f"{tax:,.0f}"
            self.intermediary_fee_label.text = f"{intermediary_fee:,.0f}"
            self.payment_processing_fee_label.text = f"{payment_processing_fee:,.0f}"
            self.utilities_label.text = f"{utilities:,.0f}"
            self.expected_net_profit_label.text = f"{net_profit:,.0f}"
        except ValueError:
            self.expected_net_profit_label.text = "입력 오류"