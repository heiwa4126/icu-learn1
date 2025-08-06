"""
BCP 47 ロケールタグ(LDML形式)を使ってCollator を作る
"""

from icu import Collator, Locale

# ldml_tag = "ja-JP-u-kf-upper-ks-level1"
ldml_tag = "ja-JP-u-ks-level1"


# BCP 47 形式のロケールタグを指定
locale = Locale.createFromName(ldml_tag)
collator = Collator.createInstance(locale)
