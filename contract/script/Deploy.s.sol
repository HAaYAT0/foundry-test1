// SPDX-License-Identifier: MIT
pragma solidity >=0.8.19;

import {Script} from "forge-std/Script.sol";
import {SampleNFT} from "../src/SampleNFT.sol";

contract Deploy is Script {
    address internal deployer;
    SampleNFT internal sampleNFT;

    function setUp() public virtual {
        (deployer, ) = deriveRememberKey(vm.envString("MNEMONIC"), 0);
    }

    function run() public {
        vm.startBroadcast(deployer);
        sampleNFT = new SampleNFT();
        vm.stopBroadcast();
    }
}
