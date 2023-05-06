import json
from web3 import Web3
from eth_account import Account


class WalletAccount:
    def __init__(self, private_key: str) -> None:
        _account = Account.from_key(private_key)
        self.private_key = private_key
        self.address = _account.address
        print(f"アカウントのウォレットアドレス: {self.address}")


class SampleNFTContract:
    def __init__(
        self,
        account: WalletAccount,
        address: str,
        abi_path: str,
        http_provider: str = "http://127.0.0.1:8545",
    ):
        self.contract_owner = account
        self.network = Web3(Web3.HTTPProvider(http_provider))

        if not self.network.is_connected():
            print("Ethereum Networkとの接続に失敗しました。終了します。")
            exit(-1)
        self.contract = self.network.eth.contract(
            address=Web3.to_checksum_address(address), abi=self._load_abi(abi_path)
        )

        name = self.contract.functions.name().call()
        print(f"スマートコントラクトの初期化に成功しました. コントラクト名: {name}")

    @staticmethod
    def _load_abi(api_json_path: str):
        with open(api_json_path, "r") as j:
            return json.load(j)

    def _execute(self, tx):
        """トランザクション実行の共通処理"""
        signed_tx = self.network.eth.account.sign_transaction(
            tx, self.contract_owner.private_key
        )
        # トランザクションの送信
        tx_hash = self.network.eth.send_raw_transaction(signed_tx.rawTransaction)

        return self.network.eth.wait_for_transaction_receipt(tx_hash)

    def mint_nft(self, address: str, sentence: str):
        """NFTを発行する

        Args:
            address (str): 所有者のウォレットアドレス
            sentence (str): 文章
        """
        tx = self.contract.functions.mintNft(
            Web3.to_checksum_address(address), sentence
        ).build_transaction(
            {
                "nonce": self.network.eth.get_transaction_count(
                    self.contract_owner.address,
                ),
                "from": self.contract_owner.address,
            }
        )
        return self._execute(tx)

    def get_sentence(self, tokenId: int) -> str:
        """トークンIDからを文章を取得する

        Args:
            tokenId (int): 対象のトークンID

        Returns:
            str: NFTに記録された文字列
        """
        return self.contract.functions.getSentence(tokenId).call()
