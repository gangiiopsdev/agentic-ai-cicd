from fastapi import FastAPI
import subprocess

app = FastAPI()

def escape_host(host):
    return ''.join(char if char.isalnum() else '_' for char in host)

def ping(host: str):
    escaped_host = escape_host(host)
    command = ['ping', escaped_host]
    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    return {'status': 'completed', 'output': result.stdout}