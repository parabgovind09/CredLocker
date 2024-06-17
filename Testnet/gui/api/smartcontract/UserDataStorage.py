'''
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract UserDataStorage {
    event DataStored(address indexed user, string data);

    mapping(address => string) private userData;

    function storeData(string memory _data) public {
        userData[msg.sender] = _data;
        emit DataStored(msg.sender, _data);
    }

    function retrieveData(address user) public view returns (string memory) {
        return userData[user];
    }
}
'''
