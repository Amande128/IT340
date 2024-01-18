let database = require('./database');

function insertPatient(patient) {
    database.patient.push(patient);
    console.log(database);
}

function retrievePatientList() {
    return database.patient.map(({creationDate, ...patient}) => patient);
}

function getPatientIndexByID(id) {
    return database.patient.findIndex((patient) => patient.id === id);
}

function getPatientByID(id) {
    return database.patient[getPatientIndexByID(id)];
    // return database.patient.filter((patient) => patient.id === id)[0];
}

function updatePatient(patient) {
    //database.patient[getPatientIndexByID(patient.id)] = patient;
    console.log(database.patient);
}

function retrievePatient(id) {
    const patient = database.patient.filter((patient) => patient.id === id)
    return patient.map(({firstName, lastName, ...patient}) => {
        patient.name = firstName+' '+lastName;
        return patient;
    })[0];
}

module.exports = {insertPatient, retrievePatientList, updatePatient, getPatientByID, retrievePatient};