const { SerialPort } = require('serialport');
const { ReadlineParser } = require('@serialport/parser-readline');

// Create a port
const port = new SerialPort({
	path: 'COM3',
	baudRate: 9600,
});

