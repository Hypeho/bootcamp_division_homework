"""
    main 함수 안의 내용만 수정해주세요.
    수정할 경우, 자동 채점 프로그램이 제대로 동작하지 않을 가능성이 있습니다.
"""

def main():
    # 이곳에 코드를 작성해주세요!
    n = int(input())

    if 0<=n<=12:
        sum = 0; i = 1
        result = 1

        while i<=n:
            sum+=i
            i+=1
        
        for j in range(1, n+1):
            result *= j
    
        print(sum)
        print(result)

    else:
        False

    return


if __name__ == '__main__':
    main()
