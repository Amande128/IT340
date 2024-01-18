function retrievePatientList() {
    return database.patientList.map(({creationDate, ...patient}) => patient);
}

function retrievePatient(id) {
    const patient = database.patient.filter((patient) => patient.id === id)
    return patient.map(({firstName, lastName, ...patient}) => {
        patient.name = firstName+' '+lastName;
        return patient;
    })[0];
}

module.exports = {retrievePatientList, retrievePatient};