# Python Dapps Sample

## 概要

本リポジトリは下記の記事で利用したソースコードです。

- [web3.py を利用して Python から Solidity のコントラクトを呼び出して NFT を発行する - Qiita](https://qiita.com/sey323/items/81fd07947dc34cf84644)
- [Solidity で NFT を作成し Foundry を利用してローカルのテストネットにデプロイする- Qiita](https://qiita.com/sey323/items/6701b34d66a2e8c5ea17)

## 環境

- foundary([インストールはこちら](https://book.getfoundry.sh/getting-started/installation))
- poetry([インストールはこちら](https://python-poetry.org/docs/))
- Python = 3.10.0

## Quick Start

`.env.sample`を参考に`.env`を作成する。`PRIVATE_KEY`と`CONTRACT_ADDRESS`はのち程更新するため、空白のままで良い

コントラクトの実行に必要なライブラリをインストールする。

```sh:
forge install
```

環境変数を設定し、テストネットを起動する。

```sh:
source .env
anvil -m $MNEMONIC
```

スマートコントラクトのビルドと、ABI ファイルの作成を行う。

```sh:
forge build --force --extra-output-files abi
```

スマートコントラクトをデプロイする。

```sh:
forge script Deploy --broadcast --rpc-url $FOUNDRY
```

デプロイが完了したら、`.env`の値を更新する。どの値を参照するかは[こちら](https://qiita.com/sey323/items/81fd07947dc34cf84644)の記事を参照。

- `PRIVATE_KEY`: コントラクトを実行するアカウントのプライベートキー
- `CONTRACT_ADDRESS`: コントラクトアドレス

その後、環境変数を再度更新する。

```sh:
source .env
```

次に Python で利用するライブラリをインストールする。

```sh:
poetry install
```

下記のコマンドで実行を行い、nft の mint と情報の取得ができれば完了。

```sh:
poetry run python client/app/main.py
```
