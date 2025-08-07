import icu

collator = icu.Collator.createInstance(icu.Locale("ja-u-co-private-kana"))
print(collator.getRules())
