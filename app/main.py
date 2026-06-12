from fastapi import FastAPI
import shlex
def safe_ping(host: str):
    try:
        # Using subprocess.run instead of subprocess.call with proper quoting to prevent injection attacks
        result = subprocess.run(['ping', shlex.quote(host)], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed', 'output': result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'message': str(e)}

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Sanitize the input to prevent injection
    if not host.isalnum():
        return {'status': 'error', 'message': 'Invalid input'}
    return safe_ping(host)