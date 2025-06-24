def calculate_sum_from_input():
    # ユーザーに数値をスペース区切りで入力してもらう
    input_str = input("数値をスペース区切りで入力してください (例: 1 2 3 4 5): ")
    
    try:
        numbers = [int(n) for n in input_str.split()]
    except ValueError:
        print("無効な入力です。数値のみを入力してください。")
        return None

    total = 0 # 合計値を格納する変数を0で初期化

    for num in numbers:
        total += num
            
    return total

# プログラム実行部分
print("--- 合計を求めるアルゴリズム ---")
sum_result = calculate_sum_from_input()
if sum_result is not None:
    print(f"合計値: {sum_result}")
print("-" * 30)