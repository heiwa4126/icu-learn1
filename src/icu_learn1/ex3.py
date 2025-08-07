"""
ソートの実験
"""

from icu import Collator, Locale


def create_collator(unicode_id: str):
    """
    Create a Collator instance using a BCP 47 locale tag (LDML format).

    Args:
      unicode_id (str): BCP 47 locale tag in LDML format (e.g., "ja-JP-u-ks-level1")

    Returns:
      Collator: ICU Collator instance configured with the specified locale

    Example:
      >>> collator = create_collator("ja-JP-u-ks-level1")
      >>> # Use collator for string comparison with Japanese locale settings
    """

    locale = Locale.createFromName(unicode_id)
    collator = Collator.createInstance(locale)
    return collator


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
# c1 = create_collator("ja@collation=phonebook")
# c1 = create_collator("ja-u-ks-level2-kf-upper")
# c1 = create_collator("ja-u-co-unihan-kf-upper-ka-shifted")
# c1 = create_collator("ja-JP-ks-level1")
# c1 = create_collator("C")
# c1 = create_collator("u-kf-lower")
c1 = create_collator("js-u-ks-level4")
sorted_words = sorted(japanese_words, key=c1.getSortKey)

print("\nソート後:")
for word in sorted_words:
    print(f"  {word}")
