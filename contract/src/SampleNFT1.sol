// SPDX-License-Identifier: MIT

pragma solidity ^0.8.14;

import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";

contract SampleNFT1 is ERC721Enumerable {
    mapping(uint256 => bytes) private _sentences;

    constructor() ERC721("SampleNFT", "SPLNFT") {}

    /**
     * NFTのmint
     */
    function mintNft(address ownerAddress, string memory sentence) public {
        // 最新のトークンIDを取得する。
        uint256 tokenId = totalSupply();
        // トークンIDに文章を紐付け
        _sentences[tokenId] = bytes(sentence);
        // NFTの発行
        _mint(ownerAddress, tokenId);
    }

    /**
     * トークンIDに紐づく文章を表示する
     */
    function getSentence(uint256 tokenId) public view returns (string memory) {
        return string(_sentences[tokenId]);
    }
}
