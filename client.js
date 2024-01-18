/**
 * Create Retrieve Update Delete (CRUD)
 */

const patientService = require('./patientService');

console.log("===ADD===");
patientService.addPatient('Doe', 'John');
patientService.addPatient('Elton', 'John');

console.log("===LIST===");
console.log(patientService.getPatientList());

console.log("===UPDATE===");
patientService.savePatient(1, 'John', 'Elton');
console.log(patientService.getPatientList());

console.log("===GET===");
console.log(patientService.getPatient(1));