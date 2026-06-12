from fastapi import FastAPI
import subprocess
def escape_shell_argument(arg):
    return arg.replace(';', '').replace('&', '').replace('|', '')

app = FastAPI()

@app.get("/ping")
def ping(host: str):    
    # Secure implementation using subprocess.run with shell=False and proper argument handling
    escaped_host = escape_shell_argument(host)
    result = subprocess.run(['ping', escaped_host], capture_output=True, text=True)
    return {"status": "completed", "output": result.stdout}