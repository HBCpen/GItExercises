# Gitでマージを行う手順

## 1. 現在のブランチを確認

```terminal
git branch
```

## 2. マージ先のブランチに切り替える

```terminal
git checkout main
```

## 3. 最新の状態に更新

```terminal
git merge feature-branch
```

## 4. マージを実行

```terminal
git merge feature-branch
```

## 5. コンフリクトが発生した場合

**コンフリクト**が発生した場合、Gitは該当するファイルを表示します。
該当ファイルを編集してコンフリクトを解消します。
解消後、以下のコマンドで解決を記録します

```terminal
git add <解消したファイル>
```

その後、マージを完了します(commitした時点でマージは完了している)。

```terminal
git commit
```

最後に：リモートリポジトリにプッシュ

```terminal
git push origin main
```
