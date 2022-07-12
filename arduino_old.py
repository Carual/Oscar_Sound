import time
import requests
import serial.tools.list_ports


def conectarClip(urlCon, nota):
    headersPost = {'HTTP_ACCEPT': '*/*', 'Content-Type': 'application/json'}
    response = requests.post(urlCon + nota + "/connect", data="true", headers=headersPost)
    if response.status_code == 204:
        print(urlCon + nota + "/connect")
        requests.post(urlCon + nota + "/connect", data="false", headers=headersPost)
        print("POST CONNECT exitoso!")
    else:
        print("ERROR")


def conectarColumna(urlCon, numero):
    headersPost = {'HTTP_ACCEPT': '*/*', 'Content-Type': 'application/json'}
    response = requests.post(urlCon + numero + "/connect", data="true", headers=headersPost)
    if response.status_code == 204:
        print(urlCon + numero + "/connect")
        requests.post(urlCon + numero + "/connect", data="false", headers=headersPost)
        print("POST CONNECT exitoso!")
    else:
        print("ERROR")


if __name__ == '__main__':

    url = "http://172.31.128.1:8080/api/v1/composition/columns/"
    serial_int = serial.Serial()
    serial_int.baudrate = 9600
    serial_int.port = "/dev/cu.usbserial-1470"
    serial_int.open()

    while True:
        if serial_int.in_waiting:
            packet = int(serial_int.readline().decode("utf"))
            print(packet)
            if 200 >= packet >= 0:
                conectarClip(url, "1")
            elif 400 >= packet >= 201:
                conectarClip(url, "2")
            elif packet >= 401:
                conectarClip(url, "3")
            else:
                raise RuntimeError