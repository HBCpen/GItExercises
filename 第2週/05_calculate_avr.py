def calculate_average_from_input():
    # ユーザーに数値をスペース区切りで入力してもらう
    input_str = input("数値をスペース区切りで入力してください (例: 10 20 30): ")
    
    try:
        numbers = [int(n) for n in input_str.split()]
    except ValueError:
        print("無効な入力です。数値のみを入力してください。")
        return None

    if not numbers: # 空のリストの場合の処理
        print("リストが空です。平均値を計算できません。")
        return None # または 0 など、要件による

    total = 0
    for num in numbers:
        total += num # 合計を計算

    count = len(numbers) # 要素の数を取得 (Pythonのlen()関数を使用)
    average = total / count # 合計を要素数で割る
    
    return average

# プログラム実行部分
print("--- 平均値を求めるアルゴリズム ---")
average_result = calculate_average_from_input()
if average_result is not None:
    print(f"平均値: {average_result}")
print("-" * 30)