from fastapi import FastAPI
import subprocess
generate_safe_command = {'ping': ['ping', '{}']}
app = FastAPI()
@app.get('/ping')
def ping(host: str):
    if host in generate_safe_command:
        safe_host = subprocess.quote(host)
        subprocess.call(generate_safe_command[host].format(safe_host))
    else:
        raise ValueError('Unsafe input detected')
    return {'status': 'completed'}