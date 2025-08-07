import icu

collator = icu.Collator.createInstance(icu.Locale("ja-JP-u-ks-level1"))
print(collator.getRules())
