/**
 * Question 6 et 7 pas faites
 */

const getBalance = require('./bank');
const transferMoney = require('./bank');

const DAO = require('./bankDAO');
const bank = require('./bankTransfert');

afterEach(() => {
    // restaure l'espion créé avec spyOn
    jest.restoreAllMocks();
});
test('callToFunction', () => {
    // getBalance();
    const spy = jest.spyOn(DAO, 'retrieveBalance').mockImplementation(()=>{});
    getBalance(1568);
    expect(spy).toHaveBeenCalled();
});

test('parameters', () => {
    const spyTransfer = jest.spyOn(bank, 'transfer');
    transferMoney(226541);
    expect(spyTransfer).toHaveBeenCalled();
});