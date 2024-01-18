let database = require('./database');

function insertPatient(patient) {
    database.patient.push(patient);
    console.log(database.patient);
}

function insertPatientIntoList({creationDate, ...patient}) {
    database.patientList.push(patient);
    console.log(database.patientList);
}

function getPatientIndexByID(id, list) {
    if (list) {
        return database.patientList.findIndex((patient) => patient.id === id);
    }
    return database.patient.findIndex((patient) => patient.id === id);
}

function getPatientByID(id, list) {
    if (list) {
        return database.patientList[getPatientIndexByID(id)];
    }
    return database.patient[getPatientIndexByID(id)];
    // return database.patient.filter((patient) => patient.id === id)[0];
}

function updatePatient(patient) {
    //database.patient[getPatientIndexByID(patient.id)] = patient;
    console.log(database.patient);
}

module.exports = {insertPatient, updatePatient, getPatientByID, insertPatientIntoList};