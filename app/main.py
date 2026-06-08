from fastapi import FastAPI
import subprocess
def execute_ping(host):
    try:
        # Use a whitelist of allowed hosts or validate input
        if host not in ['example.com', 'test.com']:
            raise ValueError('Invalid host')
        output = subprocess.run(['ping', host], capture_output=True, text=True, check=True, shell=False)
        return output.stdout
    except subprocess.CalledProcessError as e:
        return str(e)
    except ValueError as e:
        return str(e)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get="/ping")
def ping(host: str):
    return execute_ping(host)