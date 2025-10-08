def add_from_str(s: str) -> int:
    """
    接收一个字符串 s（例如 "12 34"），返回两个整数之和（int）。
    不要在这个函数里做 input/print。
    提示：用正确的方式捕获字符串s中的两个数，然后对它们进行加法计算。
    """
   num1, num2 = map(int, s.split())
    return num1 + num2

if __name__ == "__main__":
    # 程序入口：要求必须使用 input()/print()
    line = input()
    result = add_from_str(line)
    print(result)
