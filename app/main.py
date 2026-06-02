from fastapi import FastAPI
def safe_ping(host: str):
    try:
        # Validate and sanitize the host input
        if not host or not host.isalnum():
            return {'error': 'Invalid host'}
        args = ['ping', host]
        subprocess.run(args, check=True)
        return {'status': 'completed'}
    except subprocess.CalledProcessError as e:
        return {'error': str(e)}

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)