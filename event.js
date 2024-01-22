class Event {
    constructor (name, payload, patientID) {
        this.name = name;
        this.patientID = patientID;
        this.payload = payload;
        this.creationDate = new Date();
    }
}

module.exports = Event;