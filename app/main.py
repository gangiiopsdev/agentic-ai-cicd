from fastapi import FastAPI, HTTPException
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        # Sanitize the input to avoid command injection
        if '&&' in host or ';' in host or '|' in host or '`' in host or '&' in host or '>' in host or '<' in host or '$' in host or '(' in host or ')' in host or '\' in host or '/' in host:
            raise HTTPException(status_code=400, detail="Invalid input")
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}