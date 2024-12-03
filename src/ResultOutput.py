# 클래스 파일 Import
# ---- 보험료 / 세금 ----
from src.Fee import Fee  # Fee 클래스 Import
from src.Insurance import Insurance
from src.Tax import Tax  # Tax 클래스 Import

from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout  # BoxLayout import 추가

class ResultOutput(Widget):
    def __init__(self, main_layout, input_layout, costInput, fee, insurance, utilityButtons, order_intermediary_popup, **kwargs):
        super(ResultOutput, self).__init__(**kwargs)
        self.main_layout = main_layout
        self.input_layout = input_layout
        self.costInput = costInput
        self.fee = fee
        self.insurance = insurance
        self.tax = Tax()
        self.utilityButtons = utilityButtons
        self.order_intermediary_popup = order_intermediary_popup

        self.output_layout = GridLayout(cols=3, spacing=10)
        self.insurance_label = self.create_output_row("보험료", self.output_layout)
        self.tax_label = self.create_output_row("세금", self.output_layout)
        self.intermediary_fee_label = self.create_output_row("주문 중개 수수료", self.output_layout)
        self.utilities_label = self.create_output_row("공과금", self.output_layout)
        self.expected_net_profit_label = self.create_output_row("예상 순이익", self.output_layout)

        self.main_layout.add_widget(self.output_layout)

        calculate_button = Button(
            text="계산",
            font_size=25,
            size_hint=(0.4, None),
            height=90,
            font_name="NanumGothic",
            on_press=self.calculate_net_profit
        )

        calculate_button_layout = BoxLayout(
            orientation='horizontal',
            size_hint=(1, None),
            height=90
        )
        calculate_button_layout.add_widget(calculate_button)
        self.main_layout.add_widget(calculate_button_layout)

    def create_output_row(self, label_text, layout):
        layout.add_widget(Label(text=label_text, font_size=15, font_name="NanumGothic"))
        output_label = Label(text="0", font_size=15, font_name="NanumGothic")
        layout.add_widget(output_label)
        layout.add_widget(Label(text="원", font_size=15, font_name="NanumGothic"))
        return output_label

    def update_utilities_label(self, utilities_cost):
        self.utilities_label.text = f"{utilities_cost:,.0f}"

    def calculate_net_profit(self, instance):
        try:
            sales = float(self.costInput.sales_input.text)
            material_cost = float(self.costInput.material_cost_input.text)
            rates = self.fee.get_commission_rates(sales)

            # UtilityButtons에서 공과금 계산
            utilities = self.utilityButtons.calculate_utilities(None)
            self.update_utilities_label(utilities)
            intermediary_fee = rates

            insurance_states = self.insurance.insurance_selections
            insurance = Insurance.calc_insurance(
                sales,
                material_cost,
                insurance_states.get("employment", False),
                insurance_states.get("industrial", False),
                insurance_states.get("multi", False),
                insurance_states.get("disaster", False),
                insurance_states.get("gas", False),
            )
            
            tax = self.tax.CalcTax(sales, material_cost + insurance + intermediary_fee + utilities)

            net_profit = sales - (material_cost + insurance + tax + intermediary_fee + utilities)

            self.insurance_label.text = f"{insurance:,.0f}"
            self.tax_label.text = f"{tax:,.0f}"
            self.intermediary_fee_label.text = f"{intermediary_fee:,.0f}"
            self.expected_net_profit_label.text = f"{net_profit:,.0f}"
        except ValueError:
            self.expected_net_profit_label.text = "입력 오류"