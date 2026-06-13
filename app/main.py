from fastapi import FastAPI
import subprocess
class SafePinger:
    @staticmethod
def ping(host: str):
        try:
            # Sanitize input by validating and escaping the host parameter
            safe_host = ''.join(char for char in host if char.isalnum() or char in ('.', '-', '_'))
            response = subprocess.run(['ping', safe_host], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            return response.stdout
        except Exception as e:
            return f'Error: {str(e)}'

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping_endpoint(host: str):
    pinger = SafePinger()
    return pinger.ping(host)