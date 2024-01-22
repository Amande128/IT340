const Event = require('./event');
const Patient = require('./patient');

eventList = [];

function addEvent(payload, eventName, patientID) {
    const event = new Event(eventName, payload, patientID);
    eventList.push(event);
    console.log(eventList);
}

function restorePatient(id) {
    const eventPatient = eventList.filter((event) => event.patientID === id);
    return retrieveEvents(eventPatient);
}

function retrieveEvents(events) {
    const patientReduce = events.reduce((patient, currentEvent) => {
        switch(currentEvent.name) {
            case ("patientAdded"):
                patient.id = currentEvent.patientID;
                patient.lastName = currentEvent.payload.lastName;
                patient.firstName = currentEvent.payload.firstName;
                patient.creationDate = currentEvent.payload.creationDate;
                return patient;
            case ("patientSaved"):
                patient.lastName = currentEvent.payload.lastName;
                patient.firstName = currentEvent.payload.firstName;
                return patient;
            default:
                break;
        }
    }, { });
    const patientFinal = new Patient(patientReduce.lastName, patientReduce.firstName, patientReduce.id);
    patientFinal.creationDate = patientReduce.creationDate;
    return patientFinal;
}

module.exports = {addEvent, restorePatient};