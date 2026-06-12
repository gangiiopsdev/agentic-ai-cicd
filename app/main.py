from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    try:
        output = subprocess.run(['ping', host], capture_output=True, text=True)
        return output.stdout
    except Exception as e:
        return f'Error: {str(e)}'

@app.get("/ping")
def ping(host: str):