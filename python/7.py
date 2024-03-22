"""
    main 함수 안의 내용만 수정해주세요.
    수정할 경우, 자동 채점 프로그램이 제대로 동작하지 않을 가능성이 있습니다.
"""

def main():
    # 이곳에 코드를 작성해주세요!
    def IsLeapYear(year):
        if (year%4==0) and (year%100!=0) or (year%400==0):
            return True
        else:
            return False
    
    def GetDayOfMonth(year, month):
        if month==2:
            if IsLeapYear(year):
                return 29
            else:
                return 28
        if month==4 or month==6 or month==9 or month==11:
            return 30
        return 31
    
    y = int(input())
    m = int(input())
    result = GetDayOfMonth(y, m)

    print(result)

    return


if __name__ == '__main__':
    main()
