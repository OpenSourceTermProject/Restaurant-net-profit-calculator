from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout

# 연 매출액 및 식자재비 입력
class CostInput(Widget):
    def __init__(self, main_layout, input_layout, **kwargs):
        super(CostInput, self).__init__(**kwargs)

        self.main_layout = main_layout
        self.input_layout = input_layout  # input_layout 매개변수 유지

        # 레이아웃 설정
        self.input_layout.cols = 3
        self.input_layout.spacing = 15  # 간격 줄이기
        self.input_layout.padding = [10, 10, 10, 10]

        # 연 매출 입력 필드
        self.input_layout.add_widget(Label(
            text="연 매출액", font_size=18, font_name="NanumGothic", size_hint_x=0.4  # 글씨 크기 약간 축소
        ))
        self.sales_input = TextInput(
            multiline=False, font_size=18, size_hint_x=0.5  # 입력 필드 글씨 크기도 조정
        )
        self.input_layout.add_widget(self.sales_input)
        self.input_layout.add_widget(Label(
            text="원", font_size=18, font_name="NanumGothic", size_hint_x=0.1  # 단위도 크기 조정
        ))

        # 식자재비 입력 필드
        self.input_layout.add_widget(Label(
            text="식자재비", font_size=18, font_name="NanumGothic", size_hint_x=0.4
        ))
        self.material_cost_input = TextInput(
            multiline=False, font_size=18, size_hint_x=0.5
        )
        self.input_layout.add_widget(self.material_cost_input)
        self.input_layout.add_widget(Label(
            text="원", font_size=18, font_name="NanumGothic", size_hint_x=0.1
        ))

        # Main Layout에 입력 레이아웃 추가
        self.main_layout.add_widget(self.input_layout)
