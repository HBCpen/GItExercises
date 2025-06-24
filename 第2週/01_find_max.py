def find_max_from_input():
    # ユーザーに数値をスペース区切りで入力してもらう
    input_str = input("数値をスペース区切りで入力してください (例: 3 1 4 1 5): ")
    
    # 入力文字列をスペースで分割し、各要素を整数に変換してリストにする
    # 空の入力や、数値でない文字が含まれる場合はエラーになる可能性があるので注意
    try:
        numbers = [int(n) for n in input_str.split()]
    except ValueError:
        print("無効な入力です。数値のみを入力してください。")
        return None

    if not numbers: # numbersが空のリストでないか確認
        print("リストが空です。最大値を判断できません。")
        return None

    # リストの最初の要素を仮の最大値とする
    max_value = numbers[0]

    # リストの残りの要素を一つずつ確認
    for num in numbers:
        # もし現在の要素がmax_valueよりも大きければ更新
        if num > max_value:
             max_value = num
            
    return max_value

# プログラム実行部分
print("--- 最大値を求めるアルゴリズム ---")
max_result = find_max_from_input()
if max_result is not None:
    print(f"最大値: {max_result}")
print("-" * 30)
