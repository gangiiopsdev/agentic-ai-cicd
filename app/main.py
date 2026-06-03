from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    try:
        output = subprocess.run(['ping', subprocess.check_output(['echo', host]).decode()], capture_output=True, text=True)
        return output.stdout
    except Exception as e:
        return f'Error: {e}'

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)