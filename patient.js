let patient_id = 0;
function incrementID() {
    return patient_id++;
}

class Patient {
    constructor(lastName, firstName) {
        this.id = incrementID();
        this.lastName = lastName;
        this.firstName = firstName;
        this.creationDate = new Date();
    }

    updateName(lastName, firstName) {
        this.lastName = lastName;
        this.firstName = firstName;
    }
}

module.exports = Patient;