from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.checkbox import CheckBox
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup


# 보험
class Insurance(Widget):
    def __init__(self, main_layout, **kwargs):
        super(Insurance, self).__init__(**kwargs)
        self.main_layout = main_layout

        # 기본 보험 설정값
        self.insurance_selections = {
            "employment": False,
            "industrial": False,
            "multi": False,
            "disaster": False,
            "gas": False,
        }

        # 보험료 세부 설정 버튼 추가
        insurance_settings_button = Button(
            text="보험료 세부 설정", font_size=15, on_press=self.open_insurance_settings, font_name="NanumGothic"
        )
        self.main_layout.add_widget(insurance_settings_button)
        
    def open_insurance_settings(self, instance):
        popup = InsuranceSettingsPopup(self)
        popup.open()

    # 보험료 계산 함수
    def calc_insurance(year_total_income, necessary_expenses, employment_insurance, industrial_accident_insurance,
                  multi_insurance, disaster_insurance, gas_insurance):
        # 입력값 총매출액(부가세포함) 필요경비(보험제외 재료비, 공과금,배달 수수료 등) 고용보험(True,false) 산재보험(True,false) 의무보험3개(True,false) True,False는 체크표시

        m_insurance = 0
        c_insurance = 0

        ####################### 4대보험 ########################
        business_income = year_total_income - (year_total_income * 0.1) - necessary_expenses  # 사업소득 총매출 - 부가세 - 필요경비

        # 국민연금 사업소득 9%
        pension = business_income * 0.09

        # 건강보험 https://www.nhis.or.kr/nhis/minwon/retrieveLocalCalcView.do?toDt=
        health_insurance = business_income * 0.0709  # + {재산(전월세 등 포함)보험료 부과점수 × 부과점수 당 금액(208.4원)} ######################################################################

        # 고용보험 선택(true,false) 사업소득 2.25%
        if employment_insurance:
            e_insurance = business_income * 0.0225
        else:
            e_insurance = 0

        # 산재보험 선택(true,false) 사업 소득 0.96%
        if industrial_accident_insurance:
            industrial_insurance = business_income * 0.0096
        else:
            industrial_insurance = 0

        m_insurance = pension + e_insurance + industrial_insurance + health_insurance

        ####################### 의무보험 ########################
        if multi_insurance:
            c_insurance += 50000
        if disaster_insurance:
            c_insurance += 20000
        if gas_insurance:
            c_insurance += 20000

        return m_insurance + c_insurance


class InsuranceSettingsPopup(Popup):
    def __init__(self, parent_app, **kwargs):
        super().__init__(**kwargs)
        self.title = "Insurance Settings"
        self.size_hint = (0.5, 0.8)
        self.parent_app = parent_app

        self.layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        # 4대보험 가입여부 체크박스
        self.MajorInsurance_layout = GridLayout(cols=2, spacing=20)
        self.MajorInsurance_layout.add_widget(Label(text="고용보험", font_size=15, 
                                                    font_name="NanumGothic"))
        self.check_employment = CheckBox()
        self.MajorInsurance_layout.add_widget(self.check_employment)

        self.MajorInsurance_layout.add_widget(Label(text="산재보험", font_size=15, 
                                                    font_name="NanumGothic"))
        self.check_industrial = CheckBox()
        self.MajorInsurance_layout.add_widget(self.check_industrial)

        self.layout.add_widget(Label(text="4대보험 가입 여부(가입시 체크)", font_size=15, 
                                     font_name="NanumGothic"))
        self.layout.add_widget(self.MajorInsurance_layout)

        # 의무보험 가입여부 체크박스
        c_insurance_layout = GridLayout(cols=2, spacing=20)
        c_insurance_layout.add_widget(Label(text="다중이용업소화재보험", font_size=15, 
                                            font_name="NanumGothic"))
        self.check_multi = CheckBox()
        c_insurance_layout.add_widget(self.check_multi)

        c_insurance_layout.add_widget(Label(text="재난보험", font_size=15, 
                                            font_name="NanumGothic"))
        self.check_disaster = CheckBox()
        c_insurance_layout.add_widget(self.check_disaster)

        c_insurance_layout.add_widget(Label(text="가스사고보험", font_size=15, 
                                            font_name="NanumGothic"))
        self.check_gas = CheckBox()
        c_insurance_layout.add_widget(self.check_gas)

        self.layout.add_widget(Label(text="의무보험 가입 여부(가입시 체크)", font_size=15, 
                                     halign="left", font_name="NanumGothic"))
        self.layout.add_widget(c_insurance_layout)

        # 확인 버튼 추가
        confirm_button = Button(text="확인", font_size=15, on_press=self.confirm_insurance, 
                                font_name="NanumGothic")
        self.layout.add_widget(confirm_button)

        self.add_widget(self.layout)

    def confirm_insurance(self, instance):

        self.parent_app.insurance_selections = {
            "employment": self.check_employment.active,
            "industrial": self.check_industrial.active,
            "multi": self.check_multi.active,
            "disaster": self.check_disaster.active,
            "gas": self.check_gas.active,
        }
        print("업데이트된 상태:", self.parent_app.insurance_selections)
        self.dismiss()
