def count_occurrences_from_input():
    # リストの要素をスペース区切りで入力してもらう (文字列でも可)
    items_str = input("リストの要素をスペース区切りで入力してください (例: りんご バナナ りんご): ")
    items = items_str.split() # 文字列のリストとして扱う
    
    # 数えたい要素を入力してもらう
    target_item = input("数えたい要素を入力してください: ")

    if not items:
        print("リストが空です。出現回数を計算できません。")
        return None

    count = 0 # 出現回数を格納する変数を0で初期化

    for item in items:
        if item == target_item: # 現在の要素がターゲットと一致するか？
            count += 1 # 一致したらカウントを増やす

    return item

# プログラム実行部分
print("--- 要素の出現回数を数えるアルゴリズム ---")
occurrences_result = count_occurrences_from_input()
if occurrences_result is not None:
    print(f"指定された要素の出現回数: {occurrences_result}")
print("-" * 30)