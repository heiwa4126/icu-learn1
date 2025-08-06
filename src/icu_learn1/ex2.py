"""
u-kf-upperでソートする
"""

from icu_learn1.u_kf_upper import collator

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
    "tokyo",
]

print("ソート前:")
for word in japanese_words:
    print(f"  {word}")

# Collatorを使ってソート
sorted_words = sorted(japanese_words, key=lambda x: collator.getSortKey(x))

print("\nソート後 (u-kf-upper):")
for word in sorted_words:
    print(f"  {word}")
