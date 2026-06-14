from fastapi import FastAPI
import subprocess

app = FastAPI()

def escape_shell_input(input_string):
    return input_string.replace(';', '').replace('&', '').replace('|', '')

@app.get('/ping')
def ping(host: str):
    # Secure implementation
    safe_host = escape_shell_input(host)
    subprocess.call(['ping', safe_host])
    return {'status': 'completed'}