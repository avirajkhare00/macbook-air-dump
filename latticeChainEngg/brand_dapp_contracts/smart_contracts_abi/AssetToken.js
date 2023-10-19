var _businessAddress = /* var of type address here */ ;
var _ipfsHash = /* var of type string here */ ;
var _ipdbHash = /* var of type string here */ ;
var _tokenAddress = /* var of type address here */ ;
var _tokenAmount = /* var of type uint256 here */ ;
var _isTradable = /* var of type bool here */ ;
var assettokenContract = web3.eth.contract([{"constant":false,"inputs":[{"name":"_newTokenAmount","type":"uint256"}],"name":"updateTradeAmount","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[],"name":"allowTradeOwner","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[],"name":"checkTradable","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[],"name":"buy","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"_tokenAmount","type":"uint256"}],"name":"trade","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"inputs":[{"name":"_businessAddress","type":"address"},{"name":"_ipfsHash","type":"string"},{"name":"_ipdbHash","type":"string"},{"name":"_tokenAddress","type":"address"},{"name":"_tokenAmount","type":"uint256"},{"name":"_isTradable","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"constructor"}]);

