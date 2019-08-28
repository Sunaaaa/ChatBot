from flask import Flask
import random

app = Flask(__name__)

# 가장 근본이 되는 주문서 
@app.route('/')
def home():
    return 'hello'


'''
1. 주문서를 만들기
    - 모든 주문은 url을 통해 받는다.
2. 해당 주문이 들어왔을 때 무엇을 할지 정의
'''

# 이름을 요청하는 주문
@app.route('/name')
def name():
    return '선아 입니다~'

# <name> : 사용자가 입력하는 값을 해당 변수에 담는다.
@app.route('/hello/<name>')
def hello(name):
#    return  'hello '+name
#    return  'hello {}'.format(name)
    return  f'hello {name}'


# 입력된 숫자를 제곱하는 기능
# <num>은 str 이기 때문에 num을 int로 형변환 필요 
# flask함수에서 return은 str 이기 때문에 return 값을 str로 형변환 필요 
@app.route('/square/<num>')
def my_square(num):
    a = (int(num)) * (int(num))
    return f'제곱 :  {a}'

@app.route('/square2/<int:num>')
def my_square2(num):
    return str(num **2)


@app.route('/menu')
def menu():
    foods=['바스버거','대우식당','고갯마루','진가와']
    food = random.choice(foods)
    return food


# 로또 번호 추천
@app.route('/lotto')
def lotto():
    lotto = [random.randint(1,45) for i in range(6)]
    return str(lotto)

@app.route('/lotto2')
def lotto2():
    lotto = random.sample(range(1,46),6)

    # 원본 배열을 바꾼다.
    #lotto.sort()

    # 원본이 바뀌지 않는다.
    # sorted(lotto)

    return str(sorted(lotto))

# 실제 로또 번호와 비교 
# 실제 로또 번호를 자동으로 가져와 매칭한 후 순위를 매긴다.
@app.route('/lotto3')
def lotto3():
    winner = [3,5,12,13,33,39]
    lotto = random.sample(range(1,46),6)

    rank = 0
    # 만약 6개 모두 일치하면 1등
    # 만약 5개가 일치하면 3등
    # 만약 4개가 일치하면 4등
    # 만약 3개가 일치하면 5등

    count = 0

    for val in winner:
        if val in lotto:
            count = count+1

    if count == 6:
        rank = 1
    elif count == 5:
        rank = 3
    elif count == 4:
        rank = 4
    elif count == 3:
        rank = 5
    else :
        rank = 6

    return f'결과 : {str(sorted(lotto)) + str(rank)}'
#    return str(rank)

@app.route('/lotto4')
def lotto4():
    winner = [3,5,12,13,33,39]
    #lotto = random.sample(range(1,46),6)

    lotto = [3,5,12,13,26,88]

    count = len(set(winner)&set(lotto))
    # => {3,5,12}

    rank = '꽝'
    if count == 6:
        rank = '1등'
    elif count == 5:
        rank = '3등'
    elif count == 4:
        rank = '4등'
    elif count == 3:
        rank = '5등'
    else :
        rank = '꽝'

    return f'결과 : {str(sorted(lotto)) + rank}'
