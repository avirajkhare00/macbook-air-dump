pragma solidity ^0.4.11;

import './AssetToken.sol';


contract BrandDApp {
    
    //here business will be able to upload new items, those will then be tokenized in new smart contracts.
    //will be able to choose and update payment currency.
    
    address owner;
    address brandDAppCreatorAddress;
    address tokenAddress;
    string ipfsHash;
    string ipdbHash;
    
    struct TokenItem {
        
        address tokenItemAddress;
        bool isActive;
        
    }
    
    mapping(uint256 => TokenItem) TotalTokenItems;
    
    uint256 TotalTokenItemsCounter;
    
    function BrandDApp (address _owner, string _businessName, string _businessEmail, string _ipfsHash, string _ipdbHash, address _tokenAddress) {
        
        owner = _owner;
        brandDAppCreatorAddress = msg.sender;
        ipfsHash = _ipfsHash;
        ipdbHash = _ipdbHash;
        tokenAddress = _tokenAddress;
        
        TotalTokenItemsCounter = 0;
        
    }
    
    function tokenizeItem (string _ipfsHash, string _ipdbHash, address _tokenAddress, uint256 _tokenAmount, bool _isTradable) {
        
        
        AssetToken new_asset = new AssetToken(
                owner,
                _ipfsHash,
                _ipdbHash,
                _tokenAddress,
                _tokenAmount,
                _isTradable
            );
            
        TokenItem new_asset_struct = TotalTokenItems[TotalTokenItemsCounter];
        
        new_asset_struct.tokenItemAddress = address(new_asset);
        
        new_asset_struct.isActive = true;
        
    }
    
    function removeItem (uint256 _itemIndex) returns (bool) {
        
        require(owner == msg.sender);
        
        TokenItem new_asset_struct = TotalTokenItems[_itemIndex];
        
        new_asset_struct.isActive = false;
        
    }
    
    function addToken (address _tokenAddress) returns (bool) {
        
        //let's do it simple. Let's generate token address in new contracts and only update address here
        tokenAddress = _tokenAddress;
        
    }
    
    
}
