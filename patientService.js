const Patient = require('./patient');
const patientDAO = require('./patientDAO');

function addPatient(lastName, firstName) {
    let newPatient = new Patient(lastName, firstName);
    patientDAO.insertPatient(newPatient);
}

function getPatientList() {
    return patientDAO.retrievePatientList();
}

function savePatient(id, lastName, firstName) {
    const patient = patientDAO.getPatientByID(id);
    patient.updateName(lastName, firstName);
    patientDAO.updatePatient(patient);
}

function getPatient(id) {
    return patientDAO.retrievePatient(id);
}

module.exports = {addPatient, getPatientList, savePatient, getPatient};