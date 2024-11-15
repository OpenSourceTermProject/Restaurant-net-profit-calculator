# Restaurant-net-profit-calculator

# 1. 파이썬 가상환경 및 주의사항
- kivy_venv 내에 파이썬 가상 환경을 만들어 두었습니다.
- 해당 프로젝트의 모든 기능은 본인의 컴퓨터와 무관하게 가상 환경 위에서 동작합니다.
- 설치된 라이브러리들은 kivy_venv/Lib에 파일이 있습니다.

## IDE 파이썬 인터프리터 설정
- 만약 기존 VSCode나 PyCharm에서 자신의 컴퓨터에 설치된 인터프리터를 사용하고 있다면, kivy_venv 내에 있는 파이썬 인터프리터로 바꾸어 줘야 합니다.
- VSCode의 경우 https://flex-link.co.kr/6 게시물을 참고하시면 됩니다. 이때, 인터프리터를 선택하는 과정에서 "Python 3.12.4 (’kivy_venv’: venv) .\kivy_venv\Scripts\python.ext" 를 선택하시면 됩니다.

## 라이브러리를 새로 설치해야 하는 경우
- 각자 컴퓨터에 있는 터미널에서 pip install을 하게 되면 가상 환경이 아니라 자신의 컴퓨터에만 설치가 되므로 문제가 생깁니다.
- 가상 환경에 라이브러리를 설치하는 과정은 다음과 같습니다.
1. 탐색기에서 main.py 파일이 있는 프로젝트 루트 폴더로 이동
2. 빈 공간에 오른쪽 클릭을 해 '터미널에서 열기' 클릭. 만약 해당 버튼이 없다면 탐색기 주소창에 cmd 입력 후 엔터 (터미널이나 cmd에서 프로젝트 폴더로 이동하기만 하면 됩니다.)
3. kivy_venv\Scripts\activate를 입력
4. 명령 프롬프트 제일 왼쪽에 (kivy_venv) 가 표시되면 해당 프롬프트가 정상적으로 가상 환경에 대한 프롬프트로 변경 완료
5. pip install로 라이브러리 설치

### 만약 UnauthorizedAccess 오류가 뜨는 경우
- 오류 메시지 마지막 줄에 UnauthorizedAccess가 있는 경우, 권한 문제로 인해 실행이 되지 않는 경우입니다.
- 터미널 또는 cmd를 '관리자 권한으로 실행'해 프로젝트 폴더로 이동합니다.
- Set-ExecutionPolicy RemoteSigned 를 입력합니다. (변경 여부를 묻는다면 Y를 입력)

# 2. 구조
- 프로그램을 실행할 때는 main.py를 실행하면 됩니다.

## RestaurantCaculatorApp 클래스
- build 함수의 리턴값이 최종적으로 화면에 표시될 GUI가 됩니다.
- rootWidget에 있는 main_layout을 리턴합니다. (rootWidget은 후술)
- 이 안에 직접 기능 구현하지 말고 각각 클래스 파일에서 구현한 후, rootWidget에 객체 생성해서 하나씩 붙여주세요.

## RootWidget 클래스
- 최종적인 결과물이 될 위젯입니다.
- 각각의 부분들(입력, 보험 설정, 수수료 등)의 객체가 생성되고, 그것들을 한 번에 합치는 역할을 합니다.

## src 폴더 내 클래스들
- 각 기능에 대한 세부적인 구현 내용이 있는 클래스입니다.