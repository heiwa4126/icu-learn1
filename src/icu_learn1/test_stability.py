import random

from icu_learn1.ex3b import create_collator

# 同じ単語リストを複数回ソートして結果を比較
japanese_words = [
    "ひらがな",
    "ヒラガナ",
    "カタカナ",
    "かたかな",
    "さくら",
    "サクラ",
    "桜",
    "こんにちは",
    "コンニチハ",
    "東京",
    "とうきょう",
    "トウキョウ",
    "TOKYO",
    "tokyo",
]

collator = create_collator("C")

# 複数回ソートして結果が同じかチェック
results = []
for i in range(100):
    shuffled_words = japanese_words.copy()
    random.shuffle(shuffled_words)
    sorted_words = sorted(shuffled_words, key=collator.getSortKey)
    results.append(sorted_words)

# 全ての結果が同じかチェック
all_same = all(result == results[0] for result in results)

print(f"100回のソート結果が全て同じ: {all_same}")
print("\n最初のソート結果:")
for word in results[-1]:
    print(f"  {word}")
