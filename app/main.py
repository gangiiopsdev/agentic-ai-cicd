from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    if not host.isdigit():
        return "Invalid input"
    ping_command = ['ping', host]
    process = subprocess.Popen(ping_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()
    if error:
        return error.decode('utf-8')
    return output.decode('utf-8')

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)