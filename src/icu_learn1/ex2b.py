"""
ja-JP-u-kf-upper-ks-level1でソートする
"""

from icu_learn1.jp_hira_kana import collator, ldml_tag

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

print("ソート前:")
for word in japanese_words:
    print(f"  {word}")

# Collatorを使ってソート
sorted_words = sorted(japanese_words, key=lambda x: collator.getSortKey(x))

print(f"\nソート後 ({ldml_tag}):")
for word in sorted_words:
    print(f"  {word}")
