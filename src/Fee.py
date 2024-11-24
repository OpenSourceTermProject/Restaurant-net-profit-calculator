from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput

class Fee(Widget):
    def __init__(self, main_layout, **kwargs):
        super(Fee, self).__init__(**kwargs)

        self.main_layout = main_layout
        
        # 주문 수수료 설정 버튼들을 담을 BoxLayout (가로로 배치)
        self.fee_button_layout = BoxLayout(orientation='horizontal', size_hint_y=None, height=40, spacing=10)

        # 팝업 객체 생성
        self.orderIntermediaryPopup = OrderIntermediaryPopup(self)

        # 주문 중개 버튼
        order_intermediary_button = Button(
            text="주문 중개 수수료 설정", font_size=15, on_press=self.open_order_intermediary_popup, font_name="NanumGothic",
            size_hint=(None, None), width=200, height=50
        )
        self.fee_button_layout.add_widget(order_intermediary_button)

        self.main_layout.add_widget(self.fee_button_layout)

    def open_order_intermediary_popup(self, instance):
        self.orderIntermediaryPopup.open()
        
    def get_commission_rates(self, *args) :
        return self.orderIntermediaryPopup.OrderIntermediary_result

class OrderIntermediaryPopup(Popup):
    OrderIntermediary_result = 0
    
    def __init__(self, parent_app, **kwargs):
        super().__init__(**kwargs)
        self.title = "주문 중개 수수료 설정"
        self.size_hint = (0.5, 1.0)
        self.parent_app = parent_app
        self.title_font = "NanumGothic"

        # 메인 레이아웃 설정
        self.layout = BoxLayout(orientation='vertical', padding=20, spacing=20)  # 전체 간격 추가
        self.layout.add_widget(Label(text="주문 중개처", font_size=15, halign="center", font_name="NanumGothic"))
        
        ### 배달의 민족 ###
        p_baemin_layout = GridLayout(cols=2, spacing=10)  # 내부 간격 조정
            
        p_baemin_layout.add_widget(Label(text="배달", font_size=15, font_name="NanumGothic", size_hint_y=None, height=25))
        self.baemin_d = TextInput(multiline=False, input_filter='int', font_size=15, size_hint_y=None, height=25)
        p_baemin_layout.add_widget(self.baemin_d)

        p_baemin_layout.add_widget(Label(text="포장", font_size=15, font_name="NanumGothic", size_hint_y=None, height=25))
        self.baemin_p = TextInput(multiline=False, input_filter='int', font_size=15, size_hint_y=None, height=25)
        p_baemin_layout.add_widget(self.baemin_p)
        
        self.layout.add_widget(Label(text="배달의 민족", font_size=15, halign="center", font_name="NanumGothic"))
        self.layout.add_widget(p_baemin_layout)

        ### 요기요 ###
        p_yogiyo_layout = GridLayout(cols=2, spacing=10)  
        
        p_yogiyo_layout.add_widget(Label(text="요기요 베이직", font_size=15, font_name="NanumGothic", size_hint_y=None, height=25))
        self.yogiyo_basic = TextInput(multiline=False, input_filter='int', font_size=15, size_hint_y=None, height=25)
        p_yogiyo_layout.add_widget(self.yogiyo_basic)

        p_yogiyo_layout.add_widget(Label(text="요기요 라이트", font_size=15, font_name="NanumGothic", size_hint_y=None, height=25))
        self.yogiyo_light = TextInput(multiline=False, input_filter='int', font_size=15, size_hint_y=None, height=25)
        p_yogiyo_layout.add_widget(self.yogiyo_light)

        p_yogiyo_layout.add_widget(Label(text="포장", font_size=15, font_name="NanumGothic", size_hint_y=None, height=25))
        self.yogiyo_p = TextInput(multiline=False, input_filter='int', font_size=15, size_hint_y=None, height=25)
        p_yogiyo_layout.add_widget(self.yogiyo_p)
        
        self.layout.add_widget(Label(text="요기요", font_size=15, halign="center", font_name="NanumGothic"))
        self.layout.add_widget(p_yogiyo_layout)

        ### 쿠팡이츠 ###
        p_coupang_layout = GridLayout(cols=2, spacing=10) 
        
        p_coupang_layout.add_widget(Label(text="배달", font_size=15, font_name="NanumGothic", size_hint_y=None, height=25))
        self.coupang_d = TextInput(multiline=False, input_filter='int', font_size=15, size_hint_y=None, height=25)
        p_coupang_layout.add_widget(self.coupang_d)
        
        p_coupang_layout.add_widget(Label(text="포장", font_size=15, font_name="NanumGothic", size_hint_y=None, height=25))
        self.coupang_p = TextInput(multiline=False, input_filter='int', font_size=15, size_hint_y=None, height=25)
        p_coupang_layout.add_widget(self.coupang_p)
        
        self.layout.add_widget(Label(text="쿠팡이츠", font_size=15, halign="center", font_name="NanumGothic"))
        self.layout.add_widget(p_coupang_layout)
        
        ### 배달 횟수 ###
        p_delivery_layout = GridLayout(cols=2, spacing=10) 
        
        p_delivery_layout.add_widget(Label(text="배달 횟수", font_size=15, font_name="NanumGothic", size_hint_y=None, height=25))
        self.delivery_cnt = TextInput(multiline=False, input_filter='int', font_size=15, size_hint_y=None, height=25)
        p_delivery_layout.add_widget(self.delivery_cnt)

        self.layout.add_widget(Label(text="배달 횟수", font_size=15, halign="center", font_name="NanumGothic"))
        self.layout.add_widget(p_delivery_layout)

        # 확인 버튼
        confirm_button = Button(
            text="확인", font_size=15, 
            on_press=self.confirm_order_intermediary,
            font_name="NanumGothic",
            size_hint=(None, None), 
            width=200, height=50
        )


        self.layout.add_widget(confirm_button)

        self.add_widget(self.layout)

    def calculate_OrderIntermediary(self, *args):
        # 값을 가져와 계산
        baemin_d = int(self.baemin_d.text) if self.baemin_d.text else 0
        baemin_p = int(self.baemin_p.text) if self.baemin_p.text else 0
        yogiyo_basic = int(self.yogiyo_basic.text) if self.yogiyo_basic.text else 0
        yogiyo_light = int(self.yogiyo_light.text) if self.yogiyo_light.text else 0
        yogiyo_p = int(self.yogiyo_p.text) if self.yogiyo_p.text else 0
        coupang_d = int(self.coupang_d.text) if self.coupang_d.text else 0
        delivery_cnt = int(self.delivery_cnt.text) if self.delivery_cnt.text else 0
        
        

        # 계산
        total_cost = (baemin_d * 0.098) + (baemin_p * 0.034) + (yogiyo_basic * 0.125) \
                    + (yogiyo_light * 9.7) + (yogiyo_p * 0.077) + (coupang_d * 0.098) + (delivery_cnt * 2900)

        # 계산 결과 저장
        self.OrderIntermediary_result = total_cost

    def confirm_order_intermediary(self, *args):
        # 주문 중개 수수료 설정 상태 업데이트
        self.calculate_OrderIntermediary()
        print("주문 중개 수수료 설정 업데이트: " + str(self.OrderIntermediary_result))
        self.dismiss()
