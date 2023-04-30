const WebSocket = require('ws')
const { SerialPort } = require('serialport')
const { ReadlineParser } = require('@serialport/parser-readline')
// Create a port

//OSCAR SOLO CAMBIE ESTO:
const ENTRADA = 'COM3'
const PUERTO = 3000
//NADA MAS

const server = new WebSocket.Server({ port: PUERTO })
const port = new SerialPort({
	path: ENTRADA,
	baudRate: 9600,
})

clients = []
var data_old = [100, 100, 100, 100, 100]
server.on('connection', ws => {
	console.log('Nueva conexion')
	clients.push(ws)

	ws.on('close', () => {
		console.log('Conexion cerrada')
		clients = clients.filter(client => client !== ws)
	})
})

port.pipe(new ReadlineParser({ delimiter: '\r\n' })).on('data', data => {
	data = data.split(',').map(element => {
		return parseInt(element)
	})
	console.log('Datos:', data, 'Clientes:', clients.length)
	clients.forEach(client => {
		client.send(JSON.stringify(data))
	})
})
