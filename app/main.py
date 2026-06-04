from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    try:
        # Constructing command safely using list for args parameter and validating host input
        if not host or ' ' in host or any(char in host for char in ';`&|*?{}[]()$%^!+=~\'"<>'):
            raise ValueError('Invalid host input')
        subprocess.run(['ping', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed'}
    except subprocess.CalledProcessError as e:
        return {'error': str(e)}

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    return safe_ping(host)