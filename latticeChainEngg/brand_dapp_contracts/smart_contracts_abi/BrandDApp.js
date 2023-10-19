var _businessName = /* var of type string here */ ;
var _businessEmail = /* var of type string here */ ;
var _ipfsHash = /* var of type string here */ ;
var _ipdbHash = /* var of type string here */ ;
var _tokenAddress = /* var of type address here */ ;
var branddappContract = web3.eth.contract([{"constant":false,"inputs":[{"name":"_ipfsHash","type":"string"},{"name":"_ipdbHash","type":"string"},{"name":"_tokenAddress","type":"address"},{"name":"_tokenAmount","type":"uint256"},{"name":"_isTradable","type":"bool"}],"name":"tokenizeItem","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"_itemIndex","type":"uint256"}],"name":"removeItem","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"_tokenAddress","type":"address"}],"name":"addToken","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"inputs":[{"name":"_owner","type":"address"},{"name":"_businessName","type":"string"},{"name":"_businessEmail","type":"string"},{"name":"_ipfsHash","type":"string"},{"name":"_ipdbHash","type":"string"},{"name":"_tokenAddress","type":"address"}],"payable":false,"stateMutability":"nonpayable","type":"constructor"}]);

