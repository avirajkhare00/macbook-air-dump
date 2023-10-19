pragma solidity ^0.4.11;

import './BrandDApp.sol';

contract ERC20Interface1 {
    
    function allowance(address tokenOwner, address spender) public constant returns (uint remaining);

    function transfer(address to, uint tokens) public returns (bool success);
    
    function transferFrom(address from, address to, uint tokens) public returns (bool success);
    
}

contract BrandDAppCreator {
    
    //mapping to hold all business along with their business addresses
    //function to create a new listing smart contract
    //inside that smart contract, it will tokenize any product and when any buyer buys it, buyer will become owner of that token
    //we need to include erc20 token for payment too, so will be needing one more contract for erc20 token
    
    //one address can create 1 business marketplace.
    
    address owner;
    address creatorTokenAddress;
    uint256 creatorTokenAmount;
    
    struct BrandDAppDetails {
        
        address brandDAppAddress;
        bool isActive;
        string businessName;
        string businessEmail;
        
    }
    
    function BrandDAppCreator (address _creatorTokenAddress, uint256 _creatorTokenAmount) {
        
        owner = msg.sender;
        creatorTokenAddress = _creatorTokenAddress;
        creatorTokenAmount = _creatorTokenAmount;
        
    }
    
    
    
    mapping(address => BrandDAppDetails) BrandDAppMapping;
    
    function createNewMarketPlace (string _businessName, string _businessEmail, string _ipfsHash, string _ipdbHash, address _tokenAddress) public returns (bool) {
        
        //condition1 - check if dApp creator is having existing marketplace
        require(BrandDAppMapping[msg.sender].isActive == false);
        
        //now we need to create new smart token for marketplace. Also token Amount will go to us.
        
        require(ERC20Interface1(creatorTokenAddress).allowance(msg.sender, address(this)) >= creatorTokenAmount);
        
        require(ERC20Interface1(creatorTokenAddress).transferFrom(msg.sender, owner, creatorTokenAmount));
        
        //Creator name, business name, business email, ipsh hash, ipdb hash
        BrandDApp new_DApp = new BrandDApp(msg.sender, _businessName, _businessEmail, _ipfsHash, _ipdbHash, _tokenAddress);
        
        
        BrandDAppDetails new_market_place = BrandDAppMapping[msg.sender];
        
        new_market_place.isActive = true;

        new_market_place.brandDAppAddress;
        
        return true;
        
        
    }
    
    
    function kill() public {
        
        require(owner == msg.sender);
        
        selfdestruct(owner);
        
    }
    
    
    
}
