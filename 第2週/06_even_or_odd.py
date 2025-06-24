def is_even_or_odd_from_input():
    # ユーザーに整数を入力してもらう
    input_str = input("整数を入力してください: ")
    
    try:
        number = int(input_str)
    except ValueError:
        print("無効な入力です。整数のみを入力してください。")
        return None

    # 剰余演算子 (%) を使用して2で割った余りを求める
    remainder = number % 2 
    
    if remainder == 1:
        return "偶数"
    else:
        return "奇数"

# プログラム実行部分
print("--- 偶数・奇数判別アルゴリズム ---")
parity_result = is_even_or_odd_from_input()
if parity_result is not None:
    print(f"入力された数は {parity_result}です。")
print("-" * 30)