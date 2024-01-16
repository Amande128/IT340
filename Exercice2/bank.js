const DAO = require('./bankDAO');
// function retrieveBalance() { DAO.retrieveBalance();}
function getBalance(accountID) {
    return DAO.retrieveBalance(accountID);
}

module.exports = getBalance;