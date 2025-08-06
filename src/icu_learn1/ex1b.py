"""
ja-JP-u-kf-upper-ks-level1で比較する
"""

from icu_learn1.jp_hira_kana import collator

test_pairs = (
    ("ひらがな", "ヒラガナ"),
    ("カタカナ", "かたかな"),
    ("こんにちは", "コンニチハ"),
    ("さくら", "サクラ"),
    ("tokyo", "TOKYO"),
    ("東京", "とうきょう"),
    ("日本語", "にほんご"),
    ("にほんご", "日本語"),
)

for str1, str2 in test_pairs:
    result = collator.compare(str1, str2)

    # 結果の判定
    if result == 0:
        comparison = "=="
    elif result < 0:
        comparison = "<"
    else:
        comparison = ">"

    print(f"'{str1}' {comparison} '{str2}'")
