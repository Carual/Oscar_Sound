const WebSocket = require('ws')
const { SerialPort } = require('serialport')
const { ReadlineParser } = require('@serialport/parser-readline')
var fs = require('fs')
var files_1 = fs.readdirSync('imagenes_1/').filter(word => {
	return word.endsWith('.tif')
})
var files_2 = fs.readdirSync('imagenes_2/').filter(word => {
	return word.endsWith('.tif')
})
var files_3 = fs.readdirSync('imagenes_3/').filter(word => {
	return word.endsWith('.tif')
})
var files_4 = fs.readdirSync('imagenes_4/').filter(word => {
	return word.endsWith('.tif')
})
console.log(files_1, files_2, files_3, files_4)
const server = new WebSocket.Server({ port: 8080 })
// Create a port
const port = new SerialPort({
	path: '/dev/cu.usbserial-1410',
	baudRate: 9600,
})
var data_old = [1000, 1000, 1000, 1000, 1000]
server.on('connection', ws => {
	port.pipe(new ReadlineParser({ delimiter: '\r\n' })).on('data', data => {
		data = data.split(',')
		console.log(data)
		for (let i = 0; i < data.length; i++) {
			const element = parseInt(data[i])
			if (data_old[i] > 550 && element < 550) {
				file_send = ''
				switch (i) {
					case 0:
						file_send = 'imagenes_1/' + files_1[Math.floor(Math.random() * files_1.length)]
						break
					case 1:
						file_send = 'imagenes_2/' + files_2[Math.floor(Math.random() * files_2.length)]
						break
					case 2:
						file_send = 'imagenes_3/' + files_3[Math.floor(Math.random() * files_3.length)]
						break
					case 3:
						file_send = 'imagenes_4/' + files_4[Math.floor(Math.random() * files_4.length)]
						break

					default:
						break
				}
				console.log(file_send)
				ws.send(file_send)

				console.log('CHANGE:', i)
			}
			data_old[i] = element
		}
	})

	ws.on('message', message => {
		console.log(message)
	})
})
