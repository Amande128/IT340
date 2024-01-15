/**
 * Question 6 et 7 pas faites
 */

const getBalance = require('./bank');

const DAO = require('./bankDAO');

afterEach(() => {
    // restaure l'espion créé avec spyOn
    jest.restoreAllMocks();
});
test('callToFunction', () => {
    // getBalance();
    const spy = jest.spyOn(DAO, 'retrieveBalance').mockImplementation(()=>{});
    getBalance();
    expect(spy).toHaveBeenCalled();
})