# KIVY 모듈 다운로드시 파이썬을 3.8버전 혹은 3.9버전으로 downgrade 시켜줘야 
# 정상적으로 설치 및 실행이 됩니다.

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

class SimpleApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        
        # Label 생성
        self.label = Label(text="Hello, Kivy!")
        layout.add_widget(self.label)
        
        # Button 생성
        button = Button(text="Click Me")
        button.bind(on_press=self.on_button_click)
        layout.add_widget(button)
        
        return layout

    def on_button_click(self, instance):
        # 버튼 클릭 시 텍스트 변경
        self.label.text = "Button clicked!"

# 앱 실행
if __name__ == '__main__':
    SimpleApp().run()