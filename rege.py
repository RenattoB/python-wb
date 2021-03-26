import regex

url = 'video: https://upload.wikimedia.org/wikipedia/commons/0/0e/Tree_example_VIS.jpg'
if ':' in url:
    print('Se encontraron dos puntos')
    if url[:url.index(':')].lower() == 'video':
        print('Es un video')        
        url = url[url.index(':') + 1:].strip()
        print(f'La url es {url}')
    elif url[:url.index(':')].lower() == 'image':
        print('Es una imagen')        
        url = url[url.index(':') + 1:].strip()
        print(f'La url es {url}')
    else:
        print('Es un mensaje')
else:
    print('Es un mensaje')




