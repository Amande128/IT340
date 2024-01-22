let database = require('./database');
let cache = require('./cache');

function insertPatient(patient) {
    database.patient.push(patient);
    console.log(database.patient);
}

function insertPatientIntoList({creationDate, ...patient}) {
    database.patientList.push(patient);
    console.log(database.patientList);
}

function insertPatientCache({firstName, lastName, ...patient}) {
    patient.name = firstName+' '+lastName;
    cache.patientCache[patient.id] = patient;
    console.log(cache);
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

function getPatientCacheByID(id) {
    return cache.patientCache[id];
}

function updatePatient(patient) {
    //database.patient[getPatientIndexByID(patient.id)] = patient;
    console.log(database.patient);
}

function updatePatientList(patient) {
    //database.patientList[getPatientIndexByID(patient.id)] = patient;
    console.log(database.patientList);
}

function updatePatientCache(patient) {
    cache.patientCache[patient.id] = patient;
    console.log('===cache===\n');
    console.log(cache);
    console.log('\n===cache===\n');
}

module.exports = {insertPatient, updatePatient, getPatientByID, insertPatientIntoList, updatePatientList, insertPatientCache, getPatientCacheByID, updatePatientCache};