from fastapi import FastAPI
import subprocess
get_ip_info = lambda ip: subprocess.run(['ping', '-c', '1', '--'], stdout=subprocess.PIPE, text=True)

def escape_input(input_string):
    return ''.join(c for c in input_string if c.isalnum() or c.isdigit())

app = FastAPI()

@app.get('/')
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get('/ping')
def ping(host: str):
    sanitized_host = escape_input(host)
    result = get_ip_info(sanitized_host)
    if result.returncode == 0:
        return {"status": "completed", "output": result.stdout}
    else:
        return {"status": "failed"}