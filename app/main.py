from fastapi import FastAPI
import subprocess

app = FastAPI()

def escape_command_arg(arg):
    return arg.replace(';', ' ').replace('&', ' ').replace('|', ' ')

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    if host.isalnum():
        subprocess.call(['ping', escape_command_arg(host)])
    else:
        return {'status': 'invalid input'}
    return {'status': 'completed'}