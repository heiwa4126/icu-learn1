from icu import ICU_VERSION, Collator, Locale

# 環境のICUバージョンを確認
print(f"PyICU version: {ICU_VERSION}")


def create_collator(unicode_id: str):
    """指定されたロケールIDからCollatorオブジェクトを生成する"""
    locale = Locale.createFromName(unicode_id)
    collator = Collator.createInstance(locale)
    # 大文字と小文字を区別
    collator.setStrength(Collator.QUATERNARY)
    return collator


def create_custom_sort_key(word):
    """カスタムソートキーを生成する関数"""
    # 基本的なソートキーを取得
    base_key = collator.getSortKey(word)

    # 大文字のラテン文字を優先するための調整
    if word.isupper() and word.isascii():
        return (0, base_key)  # 大文字のASCII文字を最優先
    elif word.islower() and word.isascii():
        return (1, base_key)  # 小文字のASCII文字を次
    else:
        return (2, base_key)  # その他（日本語文字）


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

# 新しいロケールタグでCollatorを生成
# ja: 日本語, u: 拡張, kf-upper: 大文字優先, kh-true: ひらがなをカタカナの前に置く
collator = create_collator("ja")

# getSortKeyをキーとしてリストをソート
sorted_words = sorted(japanese_words, key=create_custom_sort_key)

print("\n--- ソート結果 ---")
for word in sorted_words:
    print(f"  {word}")
