let database = require('./database');
let cache = require('./cache');

function retrievePatientList() {
    return database.patientList;
    // return database.patient.map(({creationDate, ...patient}) => patient);
}

function retrievePatient(id) {
    return cache.patientCache[id];
    // const patient = database.patient.filter((patient) => patient.id === id)
    // return patient.map(({firstName, lastName, ...patient}) => {
    //     patient.name = firstName+' '+lastName;
    //     return patient;
    // })[0];
}

module.exports = {retrievePatientList, retrievePatient};