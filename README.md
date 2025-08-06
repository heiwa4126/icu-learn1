# icu-learn1

libicu を Python の [pyicu](https://pypi.org/project/pyicu/) 経由で使ってみる。

## pyicu のインストール

Ubuntu 22.04.5 LTS では libicu-dev が必要だった。

```sh
sudo apt install libicu-dev -y
export ICU_VERSION=70  # これ要るか不明
#
uv add pyicu
# または `uv sync`
```

## 実行

uv+poe 使用

```sh
# 準備
uv sync  # 前節参照

# 日本語文字列を u-kf-upper (ひらがなカタカナ区別なし)で比較する
poe ex1  # 比較
poe ex2  # ソート
```

## 参考リンク

- [International Components for Unicode - Wikipedia](https://ja.wikipedia.org/wiki/International_Components_for_Unicode)
- [ICU - International Components for Unicode](https://icu.unicode.org/)
- [ICU Documentation | ICU is a mature, widely used set of C/C++ and Java libraries providing Unicode and Globalization support for software applications. The ICU User Guide provides documentation on how to use ICU.](https://unicode-org.github.io/icu/)
- [unicode-org/icu: The home of the ICU project source code.](https://github.com/unicode-org/icu)
