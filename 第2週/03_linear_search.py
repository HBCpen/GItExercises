def linear_search_from_input():
    # リストの要素をスペース区切りで入力してもらう
    items_str = input("リストの要素をスペース区切りで入力してください (例: 10 20 30): ")
    items = items_str.split() # 文字列のまま探索できるよう、intには変換しない (今回は汎用性を高めるため)
    
    # 探す値を入力してもらう
    target = input("探す値を入力してください: ")

    if not items:
        print("リストが空です。探索できません。")
        return None
    
    # リストの要素をインデックスと値の両方で確認
    for i in range(len(items)): # i はインデックス (0, 1, 2...)
        if items[i] == target: # 現在の要素が探す値と一致するか？
            return i # 一致したらそのインデックスを返す
    
    return -1 # リストの最後まで見つからなかった場合

# プログラム実行部分
print("--- 線形探索アルゴリズム ---")
index_result = linear_search_from_input()
if index_result is not None: # リストが空でなければ結果を出力
    if index_result != -1:
        print(f"探す値はインデックス {index_result} で見つかりました。")
    else:
        print("探す値は見つかりませんでした。")
print("-" * 30)