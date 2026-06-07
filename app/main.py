from fastapi import FastAPI
import subprocess
def escape_shell_input(input):
    return input.replace(';', '').replace('&', '').replace('|', '')

app = FastAPI()

def ping(host: str):
    safe_host = escape_shell_input(host)
    result = subprocess.run(['ping', safe_host], capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}