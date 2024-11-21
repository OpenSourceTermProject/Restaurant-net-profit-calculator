from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.checkbox import CheckBox
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup

class Fee(Widget):
    def __init__(self, main_layout, **kwargs):
        super(Fee, self).__init__(**kwargs)

        self.main_layout = main_layout

        # 결제 대행 체크박스 정의
        self.check_hecto = CheckBox()
        self.check_toss = CheckBox()
        self.check_inicis = CheckBox()
        self.check_KCP = CheckBox()
        self.check_kakao = CheckBox()
        self.check_nice = CheckBox()

        # 주문 중개 체크박스 정의
        self.check_baemin = CheckBox()
        self.check_yogiyo = CheckBox()
        self.check_coupangeats = CheckBox()

        # 결제 대행 버튼
        payment_processing_button = Button(
            text="결제 대행 수수료 설정", font_size=15, on_press=self.open_payment_processing_popup, font_name="NanumGothic",
            size_hint=(None, None), width=200, height=50
        )
        self.main_layout.add_widget(payment_processing_button)

        # 주문 중개 버튼
        order_intermediary_button = Button(
            text="주문 중개 수수료 설정", font_size=15, on_press=self.open_order_intermediary_popup, font_name="NanumGothic",
            size_hint=(None, None), width=200, height=50
        )
        self.main_layout.add_widget(order_intermediary_button)

    def open_payment_processing_popup(self, instance):
        popup = PaymentProcessingPopup(self)
        popup.open()

    def open_order_intermediary_popup(self, instance):
        popup = OrderIntermediaryPopup(self)
        popup.open()

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
            print("헥토파이낸셜 체크박스 상태: 활성화됨")
            payment_processing_fee += rates['hecto'] * sales
        if self.check_toss.active:
            print("토스페이먼츠 체크박스 상태: 활성화됨")
            payment_processing_fee += rates['toss'] * sales
        if self.check_inicis.active:
            print("이니시스 체크박스 상태: 활성화됨")
            payment_processing_fee += rates['inicis'] * sales
        if self.check_KCP.active:
            print("KCP 체크박스 상태: 활성화됨")
            payment_processing_fee += rates['KCP'] * sales
        if self.check_kakao.active:
            print("카카오페이 체크박스 상태: 활성화됨")
            payment_processing_fee += rates['kakao'] * sales
        if self.check_nice.active:
            print("나이스페이 체크박스 상태: 활성화됨")
            payment_processing_fee += rates['nice'] * sales
        return payment_processing_fee


    # 주문 중개 수수료 계산 함수
    def calculate_order_intermediary_fee(self, sales, rates):
        order_intermediary_fee = 0
        if self.check_baemin.active:
            order_intermediary_fee += rates['baemin'] * sales
        if self.check_yogiyo.active:
            order_intermediary_fee += rates['yogiyo'] * sales
        if self.check_coupangeats.active:
            order_intermediary_fee += rates['coupangeats'] * sales
        return order_intermediary_fee


class PaymentProcessingPopup(Popup):
    def __init__(self, parent_app, **kwargs):
        super().__init__(**kwargs)
        self.title = "결제 대행 수수료 설정"
        self.size_hint = (0.5, 0.8)
        self.parent_app = parent_app
        self.title_font = "NanumGothic"

        self.layout = BoxLayout(orientation='vertical', padding=[0, 0, 0, 10], spacing=10)

        # 결제 대행 수수료 설정 체크박스를 항목 이름 오른쪽에 배치
        intermediary_layout = BoxLayout(orientation='vertical', spacing=10)

        # 각 결제 대행사를 수평으로 나열 (항목 이름 오른쪽에 체크박스)
        intermediary_layout.add_widget(self.create_item("헥토파이낸셜"))
        intermediary_layout.add_widget(self.create_item("토스페이먼츠"))
        intermediary_layout.add_widget(self.create_item("이니시스"))
        intermediary_layout.add_widget(self.create_item("KCP"))
        intermediary_layout.add_widget(self.create_item("카카오페이"))
        intermediary_layout.add_widget(self.create_item("나이스페이"))

        # '결제 대행처' 문구와 레이아웃 추가
        self.layout.add_widget(Label(text="결제 대행처", font_size=15, halign="center", font_name="NanumGothic"))
        self.layout.add_widget(intermediary_layout)

        # 확인 버튼
        confirm_button = Button(
            text="확인", font_size=15, on_press=self.confirm_payment_processing, font_name="NanumGothic",
            size_hint=(None, None), width=200, height=50
        )
        self.layout.add_widget(confirm_button)

        self.add_widget(self.layout)

    # 항목을 이름과 체크박스로 구성하는 함수
    def create_item(self, name):
        item_layout = BoxLayout(orientation='horizontal', size_hint_y=None, height=30)
        label = Label(text=name, font_size=15, font_name="NanumGothic", size_hint_x=None, width=200)
        checkbox = CheckBox(size_hint_x=None, width=50)
        item_layout.add_widget(label)
        item_layout.add_widget(checkbox)

        if name == "헥토파이낸셜":
            self.parent_app.check_hecto = checkbox
        elif name == "토스페이먼츠":
            self.parent_app.check_toss = checkbox
        elif name == "이니시스":
            self.parent_app.check_inicis = checkbox
        elif name == "KCP":
            self.parent_app.check_KCP = checkbox
        elif name == "카카오페이":
            self.parent_app.check_kakao = checkbox
        elif name == "나이스페이":
            self.parent_app.check_nice = checkbox

        return item_layout

    def confirm_payment_processing(self, instance):
        # 결제 대행 수수료 설정 상태 업데이트
        print("결제 대행 수수료 설정 업데이트")
        self.dismiss()



class OrderIntermediaryPopup(Popup):
    def __init__(self, parent_app, **kwargs):
        super().__init__(**kwargs)
        self.title = "주문 중개 수수료 설정"
        self.size_hint = (0.5, 0.8)
        self.parent_app = parent_app
        self.title_font = "NanumGothic"

        self.layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        # 주문 중개 수수료 설정 체크박스
        intermediary_layout = GridLayout(cols=3, spacing=20, padding=[0, 20, 0, 0])
        intermediary_layout.add_widget(Label(text="배달의민족", font_size=15, font_name="NanumGothic"))
        intermediary_layout.add_widget(Label(text="요기요", font_size=15, font_name="NanumGothic"))
        intermediary_layout.add_widget(Label(text="쿠팡이츠", font_size=15, font_name="NanumGothic"))

        # 체크박스 초기화
        intermediary_layout.add_widget(self.parent_app.check_baemin)
        intermediary_layout.add_widget(self.parent_app.check_yogiyo)
        intermediary_layout.add_widget(self.parent_app.check_coupangeats)

        self.layout.add_widget(Label(text="주문 중개처", font_size=15, halign="center", font_name="NanumGothic"))
        self.layout.add_widget(intermediary_layout)

        # 확인 버튼
        confirm_button = Button(
            text="확인", font_size=15, on_press=self.confirm_order_intermediary, font_name="NanumGothic",
            size_hint=(None, None), width=200, height=50
        )
        self.layout.add_widget(confirm_button)

        self.add_widget(self.layout)

    def confirm_order_intermediary(self, instance):
        # 주문 중개 수수료 설정 상태 업데이트
        print("주문 중개 수수료 설정 업데이트")
        self.dismiss()
