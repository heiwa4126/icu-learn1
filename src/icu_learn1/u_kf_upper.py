"""
PyICUのAPIを使用して
u-kf-upper (ひらがなカタカナ区別なし)相当のcollatorを作る
"""

import icu

locale = icu.Locale("ja_JP")
collator = icu.Collator.createInstance(locale)

# u-kf-upper設定(ひらがなカタカナ区別なし)
# kf = kana_type, upper = カタカナに統一
collator.setAttribute(
    icu.UCollAttribute.CASE_FIRST, icu.UCollAttributeValue.UPPER_FIRST
)
collator.setAttribute(
    icu.UCollAttribute.HIRAGANA_QUATERNARY_MODE, icu.UCollAttributeValue.ON
)
