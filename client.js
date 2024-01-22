/**
 * Create Retrieve Update Delete (CRUD)
 * Command and Query Responsibility Segregation (CQRS)
 */

const patientService = require('./patientService');
const patientCommand = require('./patientCommand');
const patientQuery = require('./patientQuery');

// console.log("========CRUD========\n");

// console.log("===ADD===\n");
// patientService.addPatient('Doe', 'John');
// patientService.addPatient('Elton', 'John');

// console.log("===LIST===\n");
// console.log(patientService.getPatientList());

// console.log("===UPDATE===\n");
// patientService.savePatient(1, 'John', 'Elton');
// console.log(patientService.getPatientList());

// console.log("===GET===\n");
// console.log(patientService.getPatient(1));

console.log("========CQRS========\n");

console.log("===ADD===\n");
patientCommand.addPatient('Doe', 'Jane');
patientCommand.addPatient('Elton', 'John');

console.log("===LIST===\n");
console.log(patientQuery.getPatientList());

console.log("===UPDATE===\n");
patientCommand.savePatient(1, 'John', 'Elton');
console.log(patientQuery.getPatientList());

console.log("===GET===\n");
console.log(patientQuery.getPatient(1));