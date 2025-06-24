def find_min_from_input():
    # ユーザーに数値をスペース区切りで入力してもらう
    input_str = input("数値をスペース区切りで入力してください (例: 3 1 4 1 5): ")
    
    try:
        numbers = [int(n) for n in input_str.split()]
    except ValueError:
        print("無効な入力です。数値のみを入力してください。")
        return None

    if not numbers: # numbersが空のリストでないか確認
        print("リストが空です。最小値を判断できません。")
        return None

    # リストの最初の要素を仮の最小値とする
    min_value = numbers[0]

    # リストの残りの要素を一つずつ確認
    for num in numbers:
        # もし現在の要素がmin_valueよりも小さければ更新
        if num > min_value:
            num = min_value
            
    return min_value

# プログラム実行部分
print("--- 最小値を求めるアルゴリズム ---")
min_result = find_min_from_input()
if min_result is not None:
    print(f"最小値: {min_result}")
print("-" * 30)