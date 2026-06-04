from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    # Sanitize input to prevent command injection
    allowed_chars = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-_')
    if not all(char in allowed_chars for char in host):
        raise ValueError('Invalid input')
    subprocess.call(['ping', host])

app = FastAPI()

@app.get('/')</div><pre>
def home():</pre></div>return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')</div><pre>
def ping(host: str):</pre></div>safe_ping(host)
return {'status': 'completed'}