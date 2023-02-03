import tkinter as tk
# [해석] GUI에 대한 표준 파이썬 매개체 이며 윈도우 창을 생성할 수 있는 tkinter라는 모듈을 tk라는 이름으로 가져옴
disValue = 0
# [해석] 주요 변수 초기화
operator = {'+': 1, '-': 2, '/': 3, '*': 4, 'C': 5, '=': 6}
# [해석] 연산자를 []안의 값인 '키:가치'로 함
stoValue = 0
# [해석] 기록된 값 초기화
opPre = 0
# [해석] 연산자 값 초기화



def number_click(value):
# [해석] 0~9까지의 숫자를 클릭했을 때
    global disValue
    # [해석] 외부선언 함수를 재선언 하여 접근
    disValue = (disValue * 10) + value
    # [해석] 숫자를 클릭할때마다 10의 자리씩 이동
    str_value.set(disValue)
    # [해석] 화면에 숫자를 나타냄



def clear():
# [해석] C를 클릭하여 clear할 때
    global disValue, stoValue, opPre
    # [해석] 외부선언 함수를 재선언 하여 접근
    stoValue = 0
    # [해석] 기록된 값 초기화
    opPre = 0
    # [해석] 연산자 값 초기화
    disValue = 0
    # [해석] 주요 변수 초기화
    str_value.set(str(disValue))
    # [해석] 화면을 지움



def oprator_click(value):
# [해석] + ~ = 연산자를 클릭했을 때
    global disValue, operator, stoValue, opPre
    # [해석] 외부선언 함수를 재선언 하여 접근
    op = operator[value]
    # [해석] value의 값에 따라 숫자로 연산자를 변경

    if op == 5:
        # [해석] C가 클릭될 때
        clear()
        # [해석] 초기화

    elif disValue == 0:#
        # [해석] 현재 화면에 출력된 값이 0일 때
        opPre = 0
        # [해석] 연산자 값 초기화

    elif opPre == 0:
        # [해석] 연산자가 한번도 클릭되지 않았을 때
        opPre = op
        # [해석] 현재 눌린 연산자가 있으면 저장
        stoValue = disValue
        # [해석] 현재까지의 숫자를 저장
        disValue = 0
        # [해석] 연산자 이후의 숫자를 받기 위해 초기화
        str_value.set(str(disValue))
        # [헤석] 0으로 다음 숫자를 받을 준비

    elif op == 6:
        # [해석] = 가 클릭될 때 결과를 계산하고 출력
        if opPre == 1:
            disValue = stoValue + disValue
        # [해석] + 기록된 값과 현재 값을 더하고 출력
        if opPre == 2:
            disValue = stoValue - disValue
        # [해석] - 기록된 값에서 현재 값을 빼고 출력
        if opPre == 3:
            disValue = stoValue / disValue
        # [해석] / 기록된 값을 현재 값으로 나누고 출력
        if opPre == 4:
            disValue = stoValue * disValue
        # [해석] * 기록된 값과 현재 값을 곱한 값을 출력

        str_value.set(str(disValue))
        # [해석] 최종 결과 값을 출력
        disValue = 0
        # [해석] 주요 변수 초기화
        stoValue = 0
        # [해석] 기록된 값 초기화
        opPre = 0
        # [해석] 연산자 값 초기화

    else:
        clear()
    # [해석] 초기화



def button_click(value):
    # [해석] 버튼을 클릭했을 때

    try:
        value = int(value)
        # [해석] 정수로 변환
        #       정수가 아닌 경우 except가 발생하여 아래 except로 이동
        number_click(value)
        # [해석] 정수인 경우 number_click( )를 호출

    except:
        oprator_click(value)
    # [해석] 정수가 아닌 연산자인 경우 여기로 가져옴



win = tk.Tk()
# [해석] tk는 Tk()라는 함수를 가져옴
win.title('계산기')
# [해석] 타이틀 제목을 괄호 안 작음쉼표 사이의 글자로 입력
str_value = tk.StringVar()
# [해석] 결과를 문자로 보여줌
str_value.set(str(disValue))
# [해석] 값 입력시 문자로 변환하여 set 사용시 자동으로 업데이트
dis = tk.Entry(win, textvariable=str_value, justify='right', bg='white', fg='red')
# [해석] tkinter 모듈에 Entry로 텍스트 입출력을 위한 기입창을 생성함
#       justify에 입력된 위치에 배치,
dis.grid(column=0, row=0, columnspan=4, ipadx=80, ipady=30)
# [해석] grid를 통해 텍스트 라벨 버튼을 배치함
#       0번째 행(column), 0번째 열(row), 4행을 묶어서 자리차지
#       x축은 80, 축은 30으로 넓이 설정



calItem = [
           ['1', '2', '3', '4'],
           ['5', '6', '7', '8'],
           ['9', '0', '+', '-'],
           ['/', '*', 'C', '=']
          ]
# [해석] []안의 값을 변수 선언

for i, items in enumerate(calItem):
# [해석] i에는items를 담음
#       enunmerate를 통해 for 문과 결합하여 인덱스 요소를 한번에 가져옴 (리스트 = items)
    for k, item in enumerate(items):
    # [해석] k에 item을 담음
    #       enunmerate를 통해 for 문과 결합하여 인덱스 요소를 한번에 가져옴 (하나의 요소 = item)
        try:
            color = int(item)
            # [해석] 컬러 값이 정수인 경우
            color = 'black'
            # [해석] 검정색
        except:
            color = 'green'
            # [해석] 이외의 겨우엔 초록색
        bt = tk.Button(
                       win, text=item, width=10, height=5, bg=color, fg='white',
                       command=lambda cmd=item: button_click(cmd)
                       )
        # [해석] 윈도우 창을 가져와서 텍스트에 하나의 요소를 담고 폭은 10, 높이는 5, 배경은 컬러 값, 글자는 흰색,
        #       
        bt.grid(column=k, row=(i + 1))
        # [해석] 행은 k, 열은 1부터 시작하는 i로 하는 배열을 생성

#

win.mainloop()
# [해석] 윈도우 내부에서 수행되는 마우스 클릭 등이 발생되게 유지함