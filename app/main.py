from fastapi import FastAPI
import subprocess
class ShellEscaped:
    def __init__(self, value):
        self.value = value.replace(';', ';')

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    sanitized_host = ShellEscaped(host).value
    subprocess.call(['ping', sanitized_host], shell=False)
    return {'status': 'completed'}