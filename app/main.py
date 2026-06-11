from fastapi import FastAPI
import subprocess

def sanitize_input(input_str):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-_'
    return ''.join(filter(lambda x: x in allowed_chars, input_str))

def validate_ip_address(ip_address):
    try:
        socket.inet_aton(ip_address)
        return True
    except socket.error:
        return False

app = FastAPI()

@app.get('/ping')
def ping(host: str):  
    if not validate_ip_address(host):
        return {'status': 'failed', 'error': 'Invalid IP address'}
    sanitized_host = sanitize_input(host)
    try:
        subprocess.run(['ping', '-c', '1', sanitized_host], check=True, shell=False)
        return {'status': 'completed'}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}