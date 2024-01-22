const patientCommandDAO = require('./patientCommandDAO');
const Patient = require('./patient');
const eventStore = require('./eventStore');

function addPatient(lastName, firstName) {
    let newPatient = new Patient(lastName, firstName, -1);
    // patientCommandDAO.insertPatient(newPatient);
    // patientCommandDAO.insertPatientIntoList(newPatient);
    // patientCommandDAO.insertPatientCache(newPatient);

    eventStore.addEvent(newPatient, 'patientAdded', newPatient.id);
}

function savePatient(id, lastName, firstName) {
    // const patient = patientCommandDAO.getPatientByID(id);
    // patient.updateName(lastName, firstName);
    // patientCommandDAO.updatePatient(patient);
    // const patient2 = patientCommandDAO.getPatientByID(id, true);
    // patient2.lastName = lastName;
    // patient2.firstName = firstName;
    // patientCommandDAO.updatePatientList(patient2);

    // const patientCache = patientCommandDAO.getPatientCacheByID(id);
    // patientCache.name = firstName+' '+lastName;
    // patientCommandDAO.updatePatientCache(patientCache);

    const patient = eventStore.restorePatient(id);
    patient.lastName = lastName;
    patient.firstName = firstName;
    eventStore.addEvent(patient, 'patientSaved', id);
}

module.exports = {addPatient, savePatient};