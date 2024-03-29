import requests
from log import *
import json

def wavySendMessage(data):    
    log('***Invocando API send message de wavy***\n')
    url = 'https://api-messaging.wavy.global/v1/whatsapp/send'
    urlHeaders = {'Content-type': 'application/json','UserName': 'wa_telectronicperusac_pe','AuthenticationToken': 'nouxAVNgqztEWAgVyYfj1qI2i8g-DToSty6bGz1P'}
    response = requests.post(url, json.dumps(data), headers = urlHeaders)
    log(f'Json devuelto: {response.json()}')
    print(log('*Evento finalizado*\n'))


def wavyTextJson(data):
    log('***Preparando JSON para wavy***\n')
    number = data['externalId']
    message = data ['text']
    correlationId = data['messageId']
    
    cjson =  {
            "destinations": [{
                "correlationId": f"{correlationId}",
                "destination": f"{number}"
            }],
            "message": {
                "messageText": f"{message}"
            }
        }
    log(f'Json a enviar: {cjson}\n')    
    wavySendMessage(cjson)

def wavyImageJson(data, url):
    log('***Preparando JSON para wavy***\n')
    number = data['externalId']
    correlationId = data['messageId']
    
    cjson =  {
            "destinations": [{
                "correlationId": f"{correlationId}",
                "destination": f"{number}"
            }],
            "message": {
                "image": {
                    "type": "JPG",
                    "url": f"{url}"
                }
            }
        }
    log(f'Json a enviar: {cjson}\n')    
    wavySendMessage(cjson)

def wavyVideoJson(data, url):
    log('***Preparando JSON para wavy***\n')
    number = data['externalId']
    correlationId = data['messageId']
    
    cjson =  {
            "destinations": [{
                "correlationId": f"{correlationId}",
                "destination": f"{number}"
            }],
            "message": {
                "audio": {
                    "type": "MP4",
                    "url": f"{url}"
                }
            }
        }
    log(f'Json a enviar: {cjson}\n')    
    wavySendMessage(cjson)


def wavyPDFJson(data, url):
    log('***Preparando JSON para wavy***\n')
    number = data['externalId']
    correlationId = data['messageId']    
    cjson =  {
            "destinations": [{
                "correlationId": f"{correlationId}",
                "destination": f"{number}"
            }],
            "message": {
                "document": {
                    "type": "PDF",
                    "url": f"{url}",
                    "caption": "PDF"
                }
            }
        }
    log(f'Json a enviar: {cjson}\n')    
    wavySendMessage(cjson)

def wavyMP3Json(data, url):
    log('***Preparando JSON para wavy***\n')
    number = data['externalId']
    correlationId = data['messageId']    
    cjson =  {
            "destinations": [{
                "correlationId": f"{correlationId}",
                "destination": f"{number}"
            }],
            "message": {
                "audio": {
                    "type": "MP3",
                    "url": f"{url}"
                }
            }
        }
    log(f'Json a enviar: {cjson}\n')    
    wavySendMessage(cjson)

