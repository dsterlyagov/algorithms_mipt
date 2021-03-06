def generate_number(N: int, M: int, prefix=None):
    """"Генерируем все числа с лидирующими незначащими нулями
        в N-ричной системе счисления (N<=10)
    """
    prefix = prefix or []
    if M == 0:
        print(prefix)
        return
    for digit in range(N):
        prefix.append(digit)
        generate_number(N, M-1,prefix)
        prefix.pop()


generate_number(2,5)