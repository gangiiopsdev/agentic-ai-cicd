from fastapi import FastAPI
import subprocess

app = FastAPI()

def execute_ping(host):
    if host in ['127.0.0.1', 'localhost']:  # Add more allowed hosts as needed
        try:
            output = subprocess.run(['ping', '-c', '4', host], capture_output=True, text=True, check=True)
            return output.stdout
        except subprocess.CalledProcessError as e:
            return str(e)
    else:
        return "Invalid host"

@app.get("/ping")
def ping(host: str):
    result = execute_ping(host)
    return {"status": "completed", "output": result}