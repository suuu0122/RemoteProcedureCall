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
	* JSONの変換（from辞書型toJSON文字列）
		```python
		import json
		
		var1 = open("読み込むJSONファイルパス", 'r')
		var2 = json.load(var1)

		var3 = json.dumps(var2)	# var2は辞書型
		```
		* 辞書型からJSON形式の文字列への変換はdumps関数を使用する.
	* JSONの変換（fromJSON文字列to辞書型）
		```python
		import json
		
		var1 = open("読み込むJSONファイルパス", 'r')
		var2 = json.load(var1)

		var3 = json.dumps(var2)	# var2は辞書型

		var4 = json.load(var3)	# var3はJSON文字列
		```
		* JSON形の文字列から辞書型への変換はload関数を使用する.
<br />

## Reference
* [M1 MacにNode.jsとnpmをインストールする方法](https://nullnull.dev/blog/how-to-install-node-js-and-npm-on-m1-mac/)
* [【Python入門】JSON形式データの扱い方](https://qiita.com/Morio/items/7538a939cc441367070d)
* [PythonでJSONを編集するならこれを見てくれ](https://qiita.com/Intel0tw5727/items/5e3e2f229d4bddcde3b7)
* [Pythonで画像データをJSONにしてネットワーク越しに送受信する](https://qiita.com/Motonaga/items/8da21f52e379469d744b)
* [socket](https://www.aihara.co.jp/~junt/program/socket.html)
* [ソケットプログラミング HOWTO](https://docs.python.org/ja/3.10/howto/sockets.html)
* [PythonでUnixドメインソケットを使って通信する](https://tokibito.hatenablog.com/entry/20150927/1443286053)
* [PythonソケットによるTCP通信入門](https://nayutari.com/python-socket)
* [Pythonのクラスメソッド（@classmethod）とは？使いどころとメソッドとの違いを解説](https://blog.pyq.jp/entry/Python_kaiketsu_190205)
* [【Python】クラスの中のメソッドからメソッドを呼び出す](https://rurukblog.com/post/python-class-method-method/)
* [Python型名を文字列で取得する](https://www.sukerou.com/2018/12/python_5.html)
* [class UNIXSocket](https://docs.ruby-lang.org/ja/latest/class/UNIXSocket.html)
* [【Ruby入門】ファイルの読み込みと書き込みまとめ(File open)](https://www.sejuku.net/blog/14388)
* [module function JSON.#dump](https://docs.ruby-lang.org/ja/latest/method/JSON/m/dump.html)
