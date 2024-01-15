/**
 * Arrêt à la question 5 (faite sauf la selection du nombre de chiffres et de lettres)
 */

const validatePassword = require('./password');

test('validation', () => {

    const goodPassword = validatePassword('Amande128!');
    expect(goodPassword).toBe(true);
});

test('length', () => {
    const lengthEqual8 = validatePassword('aaaaaa!1');
    expect(lengthEqual8).toBe(true);

    const badLength = validatePassword('a1:');
    expect(badLength).toBe(false);

    const withLength9 = validatePassword('Amande1^', 9);
    expect(withLength9).toBe(false);
});

test('numbers', () => {
    const noNumbers = validatePassword('aaaaaaaaa*');
    expect(noNumbers).toBe(false);
});

test('letters', () => {
    const noLetter = validatePassword('123456789[');
    expect(noLetter).toBe(false);
});

test('specialCharacters', () => {
    const noSpecialCharacter = validatePassword('Amande128');
    expect(noSpecialCharacter).toBe(false);

    const myRegex = validatePassword('Amande128$', specialCharactersRegex=/[!@&*()_+{}\[\]:;,.?\\/-]/);
    expect(myRegex).toBe(false);
});