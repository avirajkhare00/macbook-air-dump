pragma solidity ^0.4.11;

//take signatures which are necessary for token transfer

contract ERC20Interface {
    
    function allowance(address tokenOwner, address spender) public constant returns (uint remaining);

    function transfer(address to, uint tokens) public returns (bool success);
    
    function transferFrom(address from, address to, uint tokens) public returns (bool success);
    
}


contract AssetToken {
    
    address businessAddress;
    address assetCreatorAddress;
    address owner;
    string ipfsHash;
    string ipdbHash;
    address tokenAddress;
    uint256 tokenAmount;
    bool isTradable;
    bool ownerAllowedTrade;
    
    //here we will have constructor function, 1 buy method in which token amount will be deducted
    //requires 1 more step to give allowance to withdraw token from buyer to seller
    function AssetToken (address _businessAddress, string _ipfsHash, string _ipdbHash, address _tokenAddress, uint256 _tokenAmount, bool _isTradable) public {
        
        businessAddress = _businessAddress;
        assetCreatorAddress = msg.sender;
        ipfsHash = _ipfsHash;
        ipdbHash = _ipdbHash;
        tokenAddress = _tokenAddress;
        tokenAmount = _tokenAmount;
        isTradable = _isTradable;
        
    }
    
    function buy () public returns (bool) {
        
        //first we will check allowance
        //if allowance equals or greater then tokenAmount then withdraw to businessAddress and then make that buyer owner
        //also buyer can't be business issuing token
        if(businessAddress == msg.sender){
            throw;
        }
        
        require(ERC20Interface(tokenAddress).allowance(msg.sender, address(this)) >= tokenAmount);
            
        //first we transfer amount to business
        //then we make owner to that address
        require(ERC20Interface(tokenAddress).transferFrom(msg.sender, businessAddress, tokenAmount));
        
        //make buyer a new owner and add this token into basket token holder
        owner = msg.sender;
        
    }
    
    function checkTradable () public returns (bool) {
        
        return(isTradable);
        
    }
    
    function allowTradeOwner () public returns (bool) {
        
        require(owner == msg.sender);
        require(isTradable == true);
        
        ownerAllowedTrade = true;
        
    }
    
    function updateTradeAmount (uint256 _newTokenAmount) public returns (bool) {
        
        require(owner == msg.sender);
        require(isTradable == true);
        
        tokenAmount = _newTokenAmount;
        
    }
    
    function trade(uint256 _tokenAmount) public returns (bool) {
        
        require(isTradable == true);
        
        if(owner == msg.sender){
            throw;
        }
        
        require(ERC20Interface(tokenAddress).allowance(msg.sender, address(this)) >= tokenAmount);
            
        //first we transfer amount to business
        //then we make owner to that address
        require(ERC20Interface(tokenAddress).transfer(businessAddress, tokenAmount));
        
        //make buyer a new owner and add this token into basket token holder
        owner = msg.sender;
        
        ownerAllowedTrade = false;
        
    }
    
    
}
