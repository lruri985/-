// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;
//keccak256 函數可以用於生成一個 256 位的數字
//使用keccak256 函數生成一個1~100的數字
contract BigOrSmall {
    uint256 public YourNumber;
    uint256 public CompetitorNumber;
    bool private IsBig;//布林值選擇比大(true)或比小(false)
    string public GameResult;

    //使用keccak256 函數生成一個1~100的數字
    function RandomNumber() private view returns (uint256) {
        return uint256(keccak256(abi.encodePacked(block.timestamp, block.difficulty))) % 100 + 1;
    }

    constructor() {
        YourNumber=RandomNumber();   
    }
    //開始遊戲
    function play(bool SelectedBig) public {
        CompetitorNumber=RandomNumber();
        IsBig=SelectedBig;

        if ((IsBig && CompetitorNumber<YourNumber) || (!IsBig && CompetitorNumber>YourNumber)) {
            GameResult="you win";
        } else {
            GameResult="you lose";
        }
    }
    //重新設定玩家數字、結果即可重複玩遊戲
    function PlayAgain() public {
        YourNumber = RandomNumber();
        GameResult="";
    }
    
}
