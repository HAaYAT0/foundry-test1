// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.13;

import "forge-std/Test.sol";
import "../src/SampleNFT.sol";

contract SampleNFTTest is Test {
    SampleNFT public sampleNFT;
    address someRandomUser = vm.addr(1);

    function setUp() public {
        sampleNFT = new SampleNFT();
    }

    function testMinNft() public {
        string memory testSentence = "testSentence";
        sampleNFT.mintNft(someRandomUser, testSentence);

        assertEq(testSentence, sampleNFT.getSentence(0)); // mintされた文章を取得できることを確認
        assertEq(someRandomUser, sampleNFT.ownerOf(0)); // 所有者を確認
    }
}
