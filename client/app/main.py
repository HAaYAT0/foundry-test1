from contract import SampleNFTContract, WalletAccount


PRIVATE_KEY = "{コントラクトを実行するアカウントのプライベートキー}"
CONTRACT_ADDRESS = "{SampleNFTのコントラクトアドレス}"
ABI_PATH = "./contract/out/SampleNFT.sol/SampleNFT.abi.json"
HTTP_PROVIDER = "http://127.0.0.1:8545"

account = WalletAccount(private_key=PRIVATE_KEY)

snc = SampleNFTContract(
    account=account,
    address=CONTRACT_ADDRESS,
    abi_path=ABI_PATH,
    http_provider=HTTP_PROVIDER,
)


print(f"トランザクションの詳細: {snc.mint_nft(account.address, 'mint by python')}")

print(f"NFTに記録された文字列: {snc.get_sentence(tokenId=0)}")
