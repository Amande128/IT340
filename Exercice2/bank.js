const DAO = require('./bankDAO');
// function retrieveBalance() { DAO.retrieveBalance();}
function getBalance(accountID) {
    DAO.retrieveBalance(accountID);
}

module.exports = getBalance;