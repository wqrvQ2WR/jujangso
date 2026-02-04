set_id = input("아이디 설정: ")
set_pw = input("비밀번호 설정: ")

while True:
    id = input("아이디 입력: ")
    pw = input("비밀번호 입력: ")
    if id == set_id and pw == set_pw:
        print("아이디,비밀번호 일치")
        print("접근을 허용합니다")
    else:
        print("아이디나 비밀번호가 틀렸습니다")