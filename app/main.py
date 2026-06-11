from fastapi import FastAPI
import subprocess
def shell_quote(cmd):
    return ' '.join(subprocess.list2cmdline([arg]) for arg in cmd)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        # Validate and sanitize input
        if not host.isalnum() or len(host) > 64:
            raise ValueError('Invalid hostname')
        output = subprocess.run([shell_quote(['ping', host])], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': output.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'error': str(e)}
    except ValueError as ve:
        return {'status': 'error', 'error': str(ve)}