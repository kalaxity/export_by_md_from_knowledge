# export_by_md_from_knowledge
knowledgeの全記事をmarkdown形式で出力するスクリプトです。  
現状、全記事をまとめて1つのプレーンテキストで出力する方式をとっています。気が向いたら個別のmdファイルで出力するよう改造します。

## 機能
- 記事タイトル、本文、コメントをmarkdown形式で出力

## how to use
`main.py`の`base_url`にknowledgeのURLを、`n_articles`に大まかな全記事数を記載し、実行してください。

### 必要なモジュール
- markdownify
- requests
- bs4(BeautifulSoup)


## 仕組み
単純にknowledgeからスクレイピングするだけです。
