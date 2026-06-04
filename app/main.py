from fastapi import FastAPI
import subprocess
global_params = '-c'
app = FastAPI()
def sanitize_input(input_string):
    return ''.join(filter(str.isalnum, input_string))
@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    # Safe implementation
    subprocess.call(['ping', global_params, sanitized_host])
    return {'status': 'completed'}