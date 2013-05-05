'''
Created on 02 May 2013

@author: elif
'''

import SocketServer
import SimpleHTTPServer
import requests

PORT = 8081
IP = ''
CLIENTS_URL = "The url where the list of clients is kept"
USER = "modem admin user"
PASSWORD = "password"
SSID = "ssid name"

def get_file():
    html_str = None
    
    try:
        response = requests.get(CLIENTS_URL, auth=(USER, PASSWORD), stream=False)
        html_str = response.text
    except Exception, e:
        print(str(e))
            
    return html_str
        
def count_clients(html_string):
    if html_string is None or "" == html_string:
        return -1 
    else:
        return html_string.count(SSID)

class CustomHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path=='/kac-cihaz' or self.path=='/kac-cihaz/':
            html_content = get_file()            
            device_count = count_clients(html_content)            
            self.send_response(200)
            self.send_header('Content-type','text/html')
            self.end_headers()
            self.wfile.write(str(device_count))
            return
        else:
            self.send_response(200)
            self.send_header('Content-type','text/html')
            self.end_headers()
            self.wfile.write("Kimi aramistiniz?")
            return
            

httpd = SocketServer.TCPServer((IP, PORT),CustomHandler)

print 'Port=', PORT
httpd.serve_forever()

