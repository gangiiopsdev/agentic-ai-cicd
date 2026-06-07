from fastapi import FastAPI
import subprocess
def escape_cmd_arg(arg):
    return arg.replace(';', '').replace('&', '')
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    safe_host = escape_cmd_arg(host)
    result = subprocess.run(['ping', safe_host], capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}