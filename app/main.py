from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Secure implementation
    try:
        sanitized_host = ''.join(e for e in host if e.isalnum() or e in '._-')
        if '.' not in sanitized_host:
            raise ValueError('Invalid host format')
        subprocess.run(['ping', sanitized_host], check=True)
        return {"status": "completed"}
    except Exception as e:
        return {"error": str(e)}

@app.get="/)
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get="/ping")
def ping(host: str):
    return ping(host)