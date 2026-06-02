from fastapi import FastAPI
import subprocess

app = FastAPI()

def escape_command_input(input_str):
    return input_str.replace(';', '').replace('&', '').replace('|', '')

@app.get("/ping")
def ping(host: str):
    escaped_host = escape_command_input(host)
    try:
        result = subprocess.run(['ping', escaped_host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {"status": "completed", "output": result.stdout.decode('utf-8')}
    except subprocess.CalledProcessError as e:
        return {"status": "error", "stderr": e.stderr.decode('utf-8')}