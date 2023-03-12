# RemoteProcedureCall

## Overview
<br />

## [JSON](https://qiita.com/Morio/items/7538a939cc441367070d)
* JSONとは
	* 「JavaScript Object Notation」の略で、「JavaScript言語の表記法をベースにしたデータ形式」である.
	* 表記がJavaScriptベースなだけで、それ以外の言語でも利用可能.
	* JSONでは、ある数値と、その数値の名前であるキーのペアをコロン（:）で対にして、それらをコンマで区切り、全体を波括弧で括って表現する.
		```json
		{
			"book1":{
				"title": "Python Beginners",
				"year": 2005,
				"page": 399
			},
			"book2":{
				"title": "Python Developers",
				"year": 2006,
				"page": 650
			}
		}
		```
* JSONの操作
	* JSONファイルの読み込み
		1 JSONファイルを開く
		2 開いたファイルをJSONとして読み込む
		```python
		import json

		var1 = open("読み込むJSONファイルパス", 'r')	# (1)
		var2 = json.load(var1)	# (2)
		```
		* JSONファイルをload関数で読み込むと、Pythonで扱いやすいように辞書型で保存される.
		* JSON形式の文字列として扱いたい場合は、辞書型からJSON形式の文字列へ変換する必要がある.
	* JSONの変換
		```python
		import json
		
		var1 = open("読み込むJSONファイルパス", 'r')
		var2 = json.load(var1)

		var3 = json.dumps(var2)	# var2は辞書型
		```
		* 辞書型からJSON形式の文字列への変換はdumps関数を使用する.
<br />

## Reference
* [【Python入門】JSON形式データの扱い方](https://qiita.com/Morio/items/7538a939cc441367070d)
* [Pythonで画像データをJSONにしてネットワーク越しに送受信する](https://qiita.com/Motonaga/items/8da21f52e379469d744b)
