const DAO = require('./bankDAO');
const bank = require('./bankTransfert');
// function retrieveBalance() { DAO.retrieveBalance();}
function getBalance(accountID) {
    return DAO.retrieveBalance(accountID);
}

function transferMoney(accountID, amount) {
    bank.transfer(accountID, amount);
}

module.exports = getBalance,transferMoney;