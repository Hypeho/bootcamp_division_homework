"""
    main 함수 안의 내용만 수정해주세요.
    수정할 경우, 자동 채점 프로그램이 제대로 동작하지 않을 가능성이 있습니다.
"""

def main():
    # 이곳에 코드를 작성해주세요!
    alpha = input()

    a = ["b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","v","w","x","y","z"]
    b = ["a","e","i","o","u"]

    if alpha in a:
        print("X")
    elif alpha in b:
        print("O")
    else:
        print("error")

    return


if __name__ == '__main__':
    main()
