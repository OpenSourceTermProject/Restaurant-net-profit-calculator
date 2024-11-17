from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.checkbox import CheckBox

# 수수료
class Fee(Widget):
    def __init__(self, main_layout, **kwargs):
        super(Fee, self).__init__(**kwargs)

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