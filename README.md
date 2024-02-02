# export_by_md_from_knowledge
knowledgeの全記事をmarkdown形式で出力するスクリプトです。  
knowledgeは管理者であれば記事のエクスポートが可能ですが、それが何らかの理由で不可能な際に利用できるスクリプトがこちらになります。

想定しているユースケース：
- knowledgeの管理者が失踪し、エクスポート機能が使えなくなった
- 管理者パスワードを忘れ、エクスポート機能が使えない

## 機能
- 記事タイトル、本文、コメントをmarkdown形式で出力

現状、全記事をまとめて1つのプレーンテキストで出力する方式をとっています。気が向いたら個別のmdファイルで出力するよう改造します。

## how to use
`main.py`の`base_url`にknowledgeのURLを、`n_articles`に大まかな全記事数を記載し、実行してください。

### 必要なモジュール
- markdownify
- requests
- bs4(BeautifulSoup)


## 仕組み
単純にknowledgeからスクレイピングするだけです。
