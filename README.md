[![Build Status](https://api.travis-ci.org/kyuridenamida/atcoder-tools.svg?branch=stable)](https://travis-ci.org/kyuridenamida/atcoder-tools)
[![codecov](https://codecov.io/gh/kyuridenamida/atcoder-tools/branch/master/graph/badge.svg)](https://codecov.io/gh/kyuridenamida/atcoder-tools)
[![PyPI](https://img.shields.io/pypi/v/atcoder-tools.svg)](https://pypi.python.org/pypi/atcoder-tools)


重要!
===
2020-05-17 02:57 に デフォルトのブランチがmasterからstableに変わりました。
この変更の背景には、1.1.6以降の変更のverificationが終わっておわず、また完了するにも時間がかかることが見込まれるため、一時的なロールバックをしたかったというものがあります。
現状masterは1.1.6以降のマージの一時退避場所になっていますが、それらの検証が終わった後のmasterの運用は未定です。デフォルトブランチについては今後もstableを使っていく予定です。つきましては、今後のマージリクエストはstable branchから派生し、stableブランチへのPull Requestを送って頂くようお願い申し上げます。
送っていただいている既存のマージリクエストについては個別に対応いたします。

AtCoder Tools
====
Python 3.6 以降で動作する [AtCoder](https://atcoder.jp/) からサンプル入力をダウンロードしたりする際に便利なツールです。

このツールには次のような機能があります。
- AtCoderへのログイン，入出力例データなどの抽出
- 枝刈り探索による高精度・高速な入力フォーマット解析 (ARC、ABC、AGCについては約9割ほど)
- 問題文中に含まれるMOD値、YES/NO文字列、誤差ジャッジのための誤差値等の定数値抽出
- サンプルのローカルテスト機能
    - 誤差ジャッジ・特殊ジャッジに対応 by [@chaemon](https://github.com/chaemon/)
- コード提出機能
- 入力フォーマット解析結果や抽出した定数値を用いたテンプレートからのコード自動生成(以下の表に記載されている言語をサポートしています)
    - カスタムテンプレートに対応
    - 他言語対応のためのコントリビューション(≒中間形式からコードに変換する部分のPR)を募集中です!

|対応言語  |Contributor 1|Contributor 2|
|---:|:---:|:---:|
|C++|[@kyuridenamida](https://github.com/kyuridenamida/) (generator, template)|[@asi1024](https://github.com/asi1024/) (template)|
|Java|[@kyuridenamida](https://github.com/kyuridenamida/) (generator, template)||
|Rust|[@fukatani](https://github.com/fukatani/) (generator, template)|[@koba-e964](https://github.com/koba-e964/) (template, CR)|
|Python3|[@kmyk](https://github.com/kmyk/) (generator, template)|[@penpenpng](https://github.com/penpenpng/) (generator)|
|D|[@penpenpng](https://github.com/penpenpng/) (generator, template)||
|Nim|[@chaemon](https://github.com/chaemon/) (generator, template)||
|C#|[@chaemon](https://github.com/chaemon/) (generator, template)||
|Swift|[@firewood](https://github.com/firewood/) (generator, template)||

## Demo
<img src="https://user-images.githubusercontent.com/233559/52807100-f6e2d300-30cd-11e9-8906-82b9f9b2dff7.gif" width=70%>

## How to install
`pip3 install atcoder-tools` 

ただの`pip`だとPython 2系を使ってインストールされる可能性があるためうまくいかないかもしれません。

## Userscript by [@kmyk](https://github.com/kmyk/) (NEW! 2019/03/06)
Tampermonkey(各種ブラウザで動作)でインストールすることが可能なUserscriptです。公開されている過去問を対象として、atcoder-toolsで自動生成されたコードをそのままAtCoderのスニペット上で利用できます。
1. Tampermonkey をインストールする ([Chrome](https://chrome.google.com/webstore/detail/tampermonkey/dhdgffkkebhmkfjojejmpbldmpobfkfo), [FireFox](https://addons.mozilla.org/en-US/firefox/addon/tampermonkey/))
2. https://kyuridenamida.github.io/atcoder-tools/index.user.js にアクセスしてUserscriptをインストール
3. ログインした状態で適当な問題ページに行く(e.g. https://atcoder.jp/contests/abc120/tasks/abc120_d)
4. 正しくインストールされている場合、ページ下部のコードスニペットにコードが標準で埋め込まれている (atcoder-toolsの対応言語のみ)
<img src="https://user-images.githubusercontent.com/233559/53821542-56d3e780-3fb1-11e9-89d9-24a3d0e9af5c.png" width=50%>

## Analysis
https://kyuridenamida.github.io/atcoder-tools/

各問題ごとの解析結果などが載っています。

## 使用方法


*重要: かつてパスワード入力なしでログインを実現するために`AccountInformation.py`にログイン情報を書き込むことを要求していましたが、セキュリティリスクが高すぎるため、セッション情報のみを保持する方針に切り替えました。
今後はできるだけ保持されているセッション情報を利用してAtCoderにアクセスし、必要に応じて再入力を要求します。
過去のユーザーの皆様には`AccountInformation.py`を削除して頂くようお願い申し上げます。*


- `atcoder-tools gen {contest_id}` コンテスト環境を用意します。
- `atcoder-tools codegen {problem_url}` 指定されたURLが示す問題に対するソースコードを生成し、標準出力に出力します。
- `atcoder-tools test` カレント・ディレクトリ上に実行ファイルと入出力(in_\*.txt, out_\*.txt)がある状態で実行するとローカルテストを行います。
- `atcoder-tools submit` カレント・ディレクトリ上で実行すると対応する問題がサンプルに通る場合ソースコードを提出します。既にAtCoder上にその問題に対する提出がある場合、`-u`を指定しないと提出できないようになっています。
- `atcoder-tools version` 現在の atcoder-tools のバージョンを出力します。
- `atcoder-tools compile` カレント・ディレクトリ上で実行するとコードをコンパイルします。
- `atcoder-tools set` 現在のジャッジタイプを変更します。


使用方法を確認するためには`atcoder-tools (コマンド名) --help`を用います。
例えば`atcoder-tools gen --help`で`atcoder-tools gen`の引数の詳細について確認することができます。

例: 
```console
atcoder-tools gen agc001
cd ~/atcoder-workspace/agc001/A
g++ main.cpp
atcoder-tools test
```

`--without-login` 引数を指定するとログインなしでデータをダウンロードできます(一般公開されているコンテストのみ)。

```console
$ atcoder-tools gen  [contest_id] --without-login
```

### gen の詳細
```
usage: atcoder-tools gen
       [-h] [--without-login] [--workspace WORKSPACE] [--lang LANG]
       [--template TEMPLATE] [--parallel] [--save-no-session-cache]
       [--skip-existing-problems] [--config CONFIG]
       contest_id

positional arguments:
  contest_id            Contest ID (e.g. arc001)

optional arguments:
  -h, --help            show this help message and exit
  --without-login       Download data without login
  --workspace WORKSPACE
                        Path to workspace's root directory. This script will create files in {WORKSPACE}/{contest_name}/{alphabet}/ e.g. ./your-workspace/arc001/A/
                        [Default] /home/kyuridenamida/atcoder-workspace
  --lang LANG           Programming language of your template code, cpp or java or rust or python or nim or d or cs.
                        [Default] cpp
  --template TEMPLATE   File path to your template code
                        [Default (C++)] /atcodertools/tools/templates/default_template.cpp
                        [Default (Java)] /atcodertools/tools/templates/default_template.java
                        [Default (Rust)] /atcodertools/tools/templates/default_template.rs
                        [Default (Python3)] /atcodertools/tools/templates/default_template.py
                        [Default (NIM)] /atcodertools/tools/templates/default_template.nim
                        [Default (D)] /atcodertools/tools/templates/default_template.d
                        [Default (C#)] /atcodertools/tools/templates/default_template.cs
  --parallel            Prepare problem directories asynchronously using multi processors.
  --save-no-session-cache
                        Save no session cache to avoid security risk
  --skip-existing-problems
                        Skip processing every problem for which a directory already exists
  --config CONFIG       File path to your config file
                        [Default (Primary)] /home/kyuridenamida/.atcodertools.toml
                        [Default (Secondary)] /atcoder-tools/atcodertools/tools/atcodertools-default.toml
```

### test の詳細

```
usage: ./atcoder-tools test [-h] [--exec EXEC]
                                                      [--num NUM] [--dir DIR]
                                                      [--timeout TIMEOUT]
                                                      [--knock-out]
                                                      [--skip-almost-ac-feedback]
                                                      [--judge-type JUDGE_TYPE]
                                                      [--error-value ERROR_VALUE]
                                                      [--compile-before-testing COMPILE_BEFORE_TESTING]
                                                      [--compile-only-when-diff-detected COMPILE_ONLY_WHEN_DIFF_DETECTED]
                                                      [--config CONFIG]

optional arguments:
  -h, --help            show this help message and exit
  --exec EXEC, -e EXEC  File path to the execution target. [Default] Automatically detected exec file
  --num NUM, -n NUM     The case number to test (1-origin). All cases are tested if not specified.
  --dir DIR, -d DIR     Target directory to test. [Default] Current directory
  --timeout TIMEOUT, -t TIMEOUT
                        Timeout for each test cases (sec) [Default] 1
  --knock-out, -k       Stop execution immediately after any example's failure [Default] False
  --skip-almost-ac-feedback, -s
                        Hide inputs and expected/actual outputs if result is correct and there are error outputs [Default] False,
  --judge-type JUDGE_TYPE, -j JUDGE_TYPE
                        error type must be one of [normal, absolute, relative, absolute_or_relative, multisolution, interactive]
  --error-value ERROR_VALUE, -v ERROR_VALUE
                        error value for decimal number judge: [Default] 1e-09
  --compile-before-testing COMPILE_BEFORE_TESTING, -c COMPILE_BEFORE_TESTING
                        compile source before testing [true, false]:  [Default]: false
  --compile-only-when-diff-detected COMPILE_ONLY_WHEN_DIFF_DETECTED
                        compile only when diff detected [true, false] [Default]: true
  --config CONFIG       File path to your config file
                        [Default (Primary)] ~/.atcodertools.toml
                        [Default (Secondary)] atcodertools-default.toml
```


### submit の詳細

```
usage: atcoder-tools submit [-h] [--exec EXEC] [--dir DIR]
                                           [--timeout TIMEOUT] [--code CODE]
                                           [--force] [--save-no-session-cache]
                                           [--unlock-safety]
                                           [--judge-type JUDGE_TYPE]
                                           [--error-value ERROR_VALUE]

optional arguments:
  -h, --help            show this help message and exit
  --exec EXEC, -e EXEC  File path to the execution target. [Default] Automatically detected exec file
  --dir DIR, -d DIR     Target directory to test. [Default] Current directory
  --timeout TIMEOUT, -t TIMEOUT
                        Timeout for each test cases (sec) [Default] 1
  --code CODE, -c CODE  Path to the source code to submit [Default] Code path written in metadata.json
  --force, -f           Submit the code regardless of the local test result [Default] False
  --save-no-session-cache
                        Save no session cache to avoid security risk
  --unlock-safety, -u   By default, this script only submits the first code per problem. However, you can remove the safety by this option in order to submit codes twice or more.
  --judge-type JUDGE_TYPE, -j JUDGE_TYPE
                        error type must be one of [normal, absolute, relative, absolute_or_relative]
  --error-value ERROR_VALUE, -v ERROR_VALUE
                        error value for decimal number judge: [Default] 1e-09
```

### codegen の詳細

```
usage: ./atcoder-tools codegen [-h] [--without-login] [--lang LANG]
                               [--template TEMPLATE] [--save-no-session-cache]
                               [--config CONFIG]
                               url

positional arguments:
  url                   URL (e.g. https://atcoder.jp/contests/abc012/tasks/abc012_3)

optional arguments:
  -h, --help            show this help message and exit
  --without-login       Download data without login
  --lang LANG           Programming language of your template code, cpp or java or rust.
                        [Default] cpp
  --template TEMPLATE   File path to your template code
                        [Default (C++)] /home/user/GitHub/atcoder-tools/atcodertools/tools/templates/default_template.cpp
                        [Default (Java)] /home/user/GitHub/atcoder-tools/atcodertools/tools/templates/default_template.java
                        [Default (Rust)] /home/user/GitHub/atcoder-tools/atcodertools/tools/templates/default_template.rs
  --save-no-session-cache
                        Save no session cache to avoid security risk
  --config CONFIG       File path to your config file
                        [Default (Primary)] /home/user/.atcodertools.toml
                        [Default (Secondary)] /home/user/GitHub/atcoder-tools/atcodertools/tools/atcodertools-default.toml
```


### set の詳細
```
usage: ./atcoder-tools set [-h]
                                                     [--judge-type JUDGE_TYPE]
                                                     [--error-value ERROR_VALUE]
                                                     [--lang LANG] [--dir DIR]

optional arguments:
  -h, --help            show this help message and exit
  --judge-type JUDGE_TYPE, -j JUDGE_TYPE
                        error type must be one of [normal, absolute, relative, absolute_or_relative, multisolution, interactive]
  --error-value ERROR_VALUE, -v ERROR_VALUE
                        error value for decimal number judge: [Default] 1e-09
  --lang LANG           Programming language of your template code, cpp or java or rust or python or nim or d or cs.
  --dir DIR, -d DIR     Target directory to test. [Default] Current directory

```


### compileの詳細
```
usage: Compile your program in the current directory (no argument)

optional arguments:
  -h, --help  show this help message and exit
```

## 設定ファイルの例
`~/.atcodertools.toml`に以下の設定を保存すると、コードスタイルや、コード生成後に実行するコマンドを指定できます。

### 仕様
現在 4 種類に大別される設定カテゴリがサポートされています。
- **codestyle**: コード生成時に使われるコードスタイル・テンプレートや出力先に関する設定
- **postprocess**: コード生成後の後処理に関する設定
- **run**: コードコンパイル・実行時に使われるコマンドに関する設定
- **etc**: その他の設定

バージョン1.1.7以降では、言語毎に`codestyle`, `postprocess`, `run`を指定できます。([言語毎の設定](#言語毎の指定)を参照してください)

### 有効なオプション
- **codestyle**
    - indent_type
    - indent_width
    - template_file
    - workspace_dir
    - lang (commonの設定内でのみ)
- **postprocess**: コード生成後の後処理に関する設定
- **run**: コードコンパイル・実行時に使われるコマンドに関する設定
- **etc**: その他の設定

### 例
以下は、次の挙動を期待する場合の`~/.atcodertools.toml`の例です。
- `indent_type='space'` スペースがインデントに使われる(`'tab'`を指定した場合はタブが使われる)
- `indent_width=4` インデント幅は4である (`indent_width`が無指定の場合`4`(nim言語以外), `2`(nim言語)が規定値として使われます。)
- `template_file='~/my_template.cpp'` コード生成テンプレートとして`~/my_template.cpp`を使う
- `workspace_dir='~/atcoder-workspace/'` ワークスペースのルートは `~/atcoder-workspace/`
- `lang='cpp'` 言語設定は `cpp` (提出時もしくはデフォルトのコードジェネレーター生成時に使われます)
- `code_generator_file="~/custom_code_generator.py"` カスタムコードジェネレーター `~/custom_code_generator.py`を指定する
- `exec_on_each_problem_dir='clang-format -i ./*.cpp'` `exec_on_contest_dir='touch CMakeLists.txt'`
    - 問題用ディレクトリ内で毎回`clang-format`を実行して、最後に`CMakeLists.txt`(空)をコンテスト用ディレクトリに生成する
- `download_without_login=false` AtCoderにログインせずにダウンロードを行う機能を使わない (公開コンテストに対してのみ可能)
- `parallel_download=false` データの並列ダウンロードを無効にする
- `save_no_session_cache=false` ログイン情報のクッキーを保存する
- `skip_existing_problems=false` ディレクトリが既に存在する問題の処理をスキップする
- `in_example_format="in_{}.txt"` テストケース(input)のフォーマットを`in_1.txt, in_2.txt, ...`とする
- `out_example_format="out_{}.txt"` テストケース(output)のフォーマットを`out_1.txt, out_2.txt, ...`とする
- `compile_command="g++ main.cpp -o main.out"` プログラムを`atcoder-tools compile`でコンパイルする場合に実行されるコマンド
- `run_command="./main.out"` コンパイルしたプログラムを`atcoder-tools test`で実行する場合に実行されるコマンド

```toml
[codestyle]
indent_type='space' # 'tab' or 'space'
indent_width=4
template_file='~/my_template.cpp'
workspace_dir='~/atcoder-workspace/'
lang='cpp' # Check README.md for the supported languages.
code_generator_file="~/custom_code_generator.py"
[postprocess]
exec_on_each_problem_dir='clang-format -i ./*.cpp'
exec_on_contest_dir='touch CMakeLists.txt'

[run]
compile_command="g++ main.cpp -o main.out"
run_command="./main.out"

[etc]
download_without_login=false
parallel_download=false
save_no_session_cache=false
skip_existing_problems=false
in_example_format="in_{}.txt"
out_example_format="out_{}.txt"
compile_before_testing=false
compile_only_when_diff_detected=false

```

### 言語毎の設定
バージョン1.1.7以降では、言語毎に`codestyle`, `postprocess`, `run`を指定できます。

`(言語名).(設定カテゴリ名)`に対して設定を行うと、言語毎の設定になります。言語名が無い場合の通常の指定は共通のデフォルト設定として扱われます。
atcoder-tools起動時に使われる言語固有の設定は、`--lang` プログラム引数が存在すればそれを、なければ`codestyle.lang`に指定された値に基づきます。
`(言語名).codestyle.lang`は無視されます。

以下の設定では、
- 共通のコードスタイルとしてインデント幅が4のスペースインデントを用いる。`--lang`引数無しで起動した際に使用される言語はPythonである。ただし
   - c++のコード生成においてはタブインデントを用い(幅は4のまま)、加えてC++用のpostprocess設定を用いる。
   - Pythonのコード生成においてはインデント幅を2とする。
```toml
[codestyle]
lang='python'
indent_type='space'
indent_width=4
[cpp.codestyle]
indent_type='tab'
code_generator_file="~/custom_code_generator.py"
[cpp.postprocess]
exec_on_each_problem_dir='clang-format -i ./*.cpp'
exec_on_contest_dir='touch CMakeLists.txt'
[java.run]

[python.codestyle]
indent_width=2
```


### カスタムコードジェネレーター
[標準のC++コードジェネレーター](https://github.com/kyuridenamida/atcoder-tools/blob/master/atcodertools/codegen/code_generators/cpp.py)に倣って、
`(CogeGenArgs) -> str(ソースコード)`が型であるような`main`関数を定義した.pyファイルを`code_generator_file`で指定すると、コード生成時にカスタムコードジェネレーターを利用できます。

### ユニバーサルコードジェネレーター
ユニバーサルコードジェネレータはループ・配列アクセス方法等のいくつかの言語仕様を記述するだけでカスタムコードジェネレータよりも簡単にコード生成することを意図して作成したジェネレータです。設定ファイル`(言語名).toml`を`atcodertools/codegen/code_generators/universal_generator`に配置してください。設定ファイルの書き方は以下です。

- *base_indent* 入力部分のインデント数
- *insert_space_around_operators* 入力部分の変数や演算子の間にスペースを入れるかどうかをtrue/falseで指定
- *newline_after_input* 入力部分で入力ごとに空行を入れるかどうかをtrue/falseで指定
- *global_prefix* グローバル変数の宣言時に入れる接頭辞(Javaなどでstaticを指定したりできます)

以下のようにテーブルを定義します

- *[index]* ループインデックスの名称を指定します。１重目を`i`, 2重目を`j`で指定してください。省略可能で省略した場合はi, jが指定されます。perl, phpなどの言語で$i, $jなどとi, j以外の名前を指定しなければならないとき用のつもりです。
- *[loop]* ループに関することを記述します
    - **header** ループの最初に記述する内容。ループを回すための変数は`{loop_var}`, 回す回数は`{length}`を用いてください。
    - **footer** ループの最後に記述する内容。C++, Javaでは閉じカッコになります。波括弧の場合は`}}`とエスケープする必要があることに注意してください。
- *[type]* タイプ(int, float, string)のタイプについて記述します。例を参照してください。
- *[default]* デフォルトの値について記述します。例を参照してください。
- *[declare]* int, float, string, 1次元可変配列(以下`seq`), 2次元可変配列(以下`2d_seq`)の宣言方法について記述します。変数名は`{name}`を使ってください。可変配列のベースとなるタイプは`{type}`を使ってください。
- *[allocate]* `seq`, `2d_seq`の確保の方法を記述します。ベースとなるタイプは`{type}`, 変数名は`{name}`, デフォルト値は`{default}`で指定します。タイプ、デフォルト値は上記で指定したものが入ります。長さについてはseqは`{length}`で、`2d_seq`は1番目の長さは`{length_i}`, 2番目の長さは`{length_j}`となります。順番を間違えると転置されるのでご注意ください。
- *[declare_and_allocate]* `seq`, `2d_seq`について宣言と確保を同時に行う方法について記述します。フォーマットに使用されるものは`[allocate]`と同じです。
- *[input]*

- *[arg]* solve関数の引数の記述方法について指定します。`int`, `float`, `string`, `seq`, `2d_seq`について記述してください。`{name}`が変数名, `{type}`が`seq`, `2d_seq`についてベースとなる型です。
- *[actual_arg]* `seq`, `2d_seq`についてsolve関数を呼び出す際の引数の渡し方について記述します。C++などでmoveをつかってメモリを節約したいときなどに指定できます。省略可能で、省略した場合はそのまま渡されます。

- *[access]* 配列のアクセス方法について記述します。`seq`, `2d_seq`について指定してください。`{name}`で変数名, `{index_i}`, `{index_j}`でインデックス名を指定します。

以下は入力コードの冗長性を下げる目的で指定するテーブルで省略可能なものです。指定方法についてはpythonの設定を参照してください。

- *[input_func]* int, float, stringについて入力時に呼び出す関数を記述します。
- *[allocate_and_input]* `seq`, `2d_seq`について確保と入力をまとめて行うことができる場合に記述します。省略した場合、上記で指定した確保と入力の方式を複合したものが挿入されます
- *[declare_and_allocate_and_input]* `seq`, `2d_seq`について宣言・確保・入力をまとめて行うことができる場合に記述します。省略した場合、上記で指定した宣言と確保と入力の方式を複合したものが挿入されます

例えばC++での設定方法は以下です。
```toml
base_indent = 1
insert_space_around_operators = false

# global変数宣言時の接頭辞
global_prefix = ""

# ループ
[loop]
header = "for(int {loop_var} = 0 ; {loop_var} < {length} ; {loop_var}++){{"
footer = "}}"

# タイプ
[type]
int = "long long"
float = "long double"
string = "std::string"

# デフォルト値
[default]
int = "0"
float = "0.0"
string = "\"\""

# 宣言
[declare]
int = "long long {name};"
float = "long double {name};"
string = "std::string {name};"
seq = "std::std::vector<{type}> {name};"
2d_seq = "std::vector<std::vector<{type}>> {name};"

# 確保
[allocate]
seq = "{name}.assign({length}, {default});"
2d_seq = "{name}.assign({length_i}, std::vector<{type}>({length_j}));"

# 宣言と確保
[declare_and_allocate]
seq = "std::vector<{type}> {name}({length});"
2d_seq = "std::vector<std::vector<{type}>> {name}({length_i}, std::vector<{type}>({length_j}));"

# 入力
[input]
#int = "std::cin >> {name};"
int = "scanf(\"%lld\",&{name});"
#float = "std::cin >> {name};"
float = "scanf(\"%Lf\",&{name});"
string = "std::cin >> {name};"

# 引数
[arg]
int = "long long {name}"
float = "double {name}"
string = "std::string {name}"
seq = "std::vector<{type}> {name}"
2d_seq = "std::vector<std::vector<{type}>> {name}"

# 引数への渡し方
[actual_arg]
seq = "std::move({name})"
2d_seq = "std::move({name})"

# 配列アクセス
[access]
seq = "{name}[{index_i}]"
2d_seq = "{name}[{index_i}][{index_j}]"
```

例えばpythonでの設定方法は以下です。
```toml
base_indent = 1
insert_space_around_operators = true

# global変数宣言時の接頭辞
global_prefix = ""

# インデックス
[index]
i = "i"
j = "j"

# ループ
[loop]
header = "for {loop_var} in range({length}):"
footer = ""

# タイプ
[type]
int = "int"
float = "float"
string = "str"

# デフォルト値
[default]
int = "int()"
float = "float()"
string = "str()"

# 宣言
[declare]
int = ""
float = ""
string = ""
seq = ""
2d_seq = ""

# 確保
[allocate]
seq = "{name} = [{default}] * ({length})"
2d_seq = "{name} = [[{default}] * ({length_j}) for _ in {length_i}]"

# 宣言と確保
[declare_and_allocate]
seq = "{name} = [{default}] * ({length})  # type: \"List[{type}]\""
self.declare_and_allocate_2d_seq = "{name} = [[{default}] * ({length_j}) for _ in {length_i}]  # type: \"List[List[{type}]]\""

# 入力関数
[input_func]
int = "int(next(tokens))"
float = "float(next(tokens))"
string = "next(tokens)"

# 入力
[input]
int = "{name} = int(next(tokens))"
float = "{name} = float(next(tokens))"
string = "{name} = next(tokens)"

# 宣言と入力
[declare_and_input]
int = "{name} = int(next(tokens))  # type: int"
float = "{name} = float(next(tokens))  # type: float"
string = "{name} = next(tokens)  # type: str"

# 確保と入力
[allocate_and_input]
seq = "{name} = [{input_func} for _ in range({length})]"
2d_seq = "{name} = [[{input_func} for _ in range({length_j})] for _ in range({length_i})]"

# 宣言と確保と入力
[declare_and_allocate_and_input]
seq = "{name} = [{input_func} for _ in range({length})]  # type: \"List[{type}]\""
2d_seq = "{name} = [[{input_func} for _ in range({length_j})] for _ in range({length_i})]  # type: \"List[List[{type}]]\""

# 引数
[arg]
int = "{name}: int"
float = "{name}: float"
string = "{name}: str"
seq = "{name}: \"List[{type}]\""
2d_seq = "{name}: \"List[List[{type}]]\""

# 配列アクセス
[access]
seq = "{name}[{index_i}]"
2d_seq = "{name}[{index_i}][{index_j}]"
```

## テンプレートの例
`atcoder-tools gen`コマンドに対し`--template`でテンプレートソースコードを指定できます。
テンプレートエンジンの仕様については[jinja2](http://jinja.pocoo.org/docs/2.10/) の公式ドキュメントを参照してください。

テンプレートに渡される変数は以下の通りです。


- **prediction_success** 入力形式の推論に成功したとき `True`、 失敗したとき `False`が格納されている。この値が`True`のとき次の3種類の変数も存在することが保証される。
    - **input_part** input用のコード
    - **formal_arguments** 型つき引数列
    - **actual_arguments** 型なし引数列

- **mod** 問題文中に存在するmodの整数値
- **yes_str** 問題文中に存在する yes や possible などの真を表しそうな文字列値
- **no_str** 問題文中に存在する no や impossible などの偽を表しそうな文字列値

```c++
#include <bits/stdc++.h>
using namespace std;

{% if mod %}
const long long MOD = {{ mod }};
{% endif %}
{% if yes_str %}
const string YES = "{{ yes_str }}";
{% endif %}
{% if no_str %}
const string NO = "{{ no_str }}";
{% endif %}

{% if prediction_success %}
void solve({{ formal_arguments }}){

}
{% endif %}

int main(){
    {% if prediction_success %}
    {{input_part}}
    solve({{ actual_arguments }});
    {% else %}
    // Failed to predict input format
    {% endif %}
    return 0;
}
```


## Contribution

[CONTRIBUTING.md](CONTRIBUTING.md) を参照してください。

## Licence

[MIT](https://github.com/kyuridenamida/ToolsForAtCoder/blob/master/LICENCE)

## Author

[kyuridenamida](https://github.com/kyuridenamida) ([@kyuridenamida](https://twitter.com/kyuridenamida))
