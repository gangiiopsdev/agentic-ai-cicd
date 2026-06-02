from fastapi import FastAPI
import subprocess

def safe_ping(host: str):
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True, check=True)
    return result.stdout

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        # Validate and sanitize the input to prevent shell injection
        if not host.isalnum() or '..' in host or '!' in host or ';' in host or '(' in host or ')' in host or '|' in host or '&' in host or '<' in host or '>' in host or '{' in host or '}' in host:
            raise ValueError('Invalid hostname')
        return safe_ping(host)
    except subprocess.CalledProcessError as e:
        return {"error": str(e)}