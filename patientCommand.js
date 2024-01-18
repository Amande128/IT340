const patientCommandDAO = require('./patientCommandDAO');
const Patient = require('./patient');

function addPatient(lastName, firstName) {
    let newPatient = new Patient(lastName, firstName);
    patientCommandDAO.insertPatient(newPatient);
    patientCommandDAO.insertPatientIntoList(newPatient);
}

function savePatient(id, lastName, firstName) {
    const patient = patientCommandDAO.getPatientByID(id);
    patient.updateName(lastName, firstName);
    patientCommandDAO.updatePatient(patient);
    const patient2 = patientCommandDAO.getPatientByID(id, true);
    patient2.lastName = lastName;
    patient2.firstName = firstName;
}

module.exports = {addPatient, savePatient};