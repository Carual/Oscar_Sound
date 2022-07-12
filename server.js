const WebSocket = require('ws');
const { SerialPort } = require('serialport');
const { ReadlineParser } = require('@serialport/parser-readline');

const server = new WebSocket.Server({ port: 8080 });
// Create a port
const port = new SerialPort({
	path: 'COM3',
	baudRate: 9600,
});

server.on('connection', (ws) => {
	port.pipe(new ReadlineParser({ delimiter: '\r\n' })).on('data', (data) => {
		data = parseInt(data);
		if (data > 1000) {
			ws.send(data);
		}
	});

	ws.on('message', (message) => {
		console.log(message);
	});
});
