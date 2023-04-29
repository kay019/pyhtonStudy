def print_hi():
    print("2023 1학기 방송통신대학교 파이썬프로그래밍 기초 과제")
    print("202134-154039 김정훈")


def print_table():
    print("A안")
    print("n   n**2   n***3")
    print("================")
    for i in range(1, 8):
        if i % 2 != 0:
            print(i, "  ", (i ** 2), "  ", (i ** 3))

    print("B안")
    print("n   n**2   n***3")
    print("================")
    print("1    1     1")
    print("3    9     27")
    print("5    25    125")
    print("7    49    343")


def print_point():
    score = int(input("점수를 입력 하세요 : "))

    if score < 0 or score > 100:
        print("잘못된 점수입니다.")
    elif score >= 90:
        print("성적은 A 입니다.")
    elif score >= 80:
        print("성적은 B 입니다.")
    elif score >= 70:
        print("성적은 C 입니다.")
    elif score >= 60:
        print("성적은 D 입니다.")
    else:
        print("성적은 F 입니다.")


if __name__ == '__main__':
    print_hi()
    print_table()
    print_point()

