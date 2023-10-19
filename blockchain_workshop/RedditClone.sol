pragma solidity ^0.4.11;

contract RedditClone {
    
    struct newsData {
        
        string news_title;
        string news_url;
        
    }
    
    address owner;
    
    mapping (uint256 => newsData) newsDataMap;
    
    uint256[] public newsDataAccs;
    
    function RedditClone () public {
        
        owner = msg.sender;
        
    }
    
    function pushNews (string _news_title, string _news_url) returns (bool) {
        
        newsData new_news = newsDataMap[newsDataAccs.length];
        
        new_news.news_title = _news_title;
        new_news.news_url = _news_url;
        
        newsDataAccs.push(newsDataAccs.length) -1;
        
        return true;
        
    }
    
    function fetchNews (uint256 _i) public constant returns (string _news_title, string _news_url) {
        
        return (newsDataMap[_i].news_title, newsDataMap[_i].news_url);
        
    }
    
    function fetchNewsArrayLength () public constant returns (uint256 _i) {
        
        return newsDataAccs.length;
        
    }
    
}
