from fastapi import FastAPI
import subprocess
generate_ping_command = lambda host: f'ping {host}'

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        # Enhanced input sanitization
        sanitized_host = ''.join(e for e in host if e.isalnum() or e in ['.', '-'])
        subprocess.run(generate_ping_command(sanitized_host).split(), check=True)
        return {"status": "completed"}
    except Exception as e:
        return {"error": str(e)}, 500