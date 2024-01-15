function validatePassword(password, length=8, specialCharactersRegex=/[!@#$%^&*()_+{}\[\]:;<>,.?~\\/-]/) {
    if (password.length >= length) {
        if (password.match(/[0-9]+/)) {
            if (password.match(/[a-z,A-Z]+/)) {
                if(password.match(specialCharactersRegex)) {
                    return true;
                }
                return false;
            }
            return false;
        }
        return false;
    }
    return false;
}

module.exports = validatePassword;