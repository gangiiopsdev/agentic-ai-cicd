from fastapi import FastAPI, HTTPException
global ALLOWED_HOSTS = ['example.com']

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if host in ALLOWED_HOSTS:
        # Use subprocess.run instead of subprocess.call for better security
        try:
            result = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True, check=True)
            return {"status": "completed", "output": result.stdout}
        except subprocess.CalledProcessError as e:
            return {"status": "failed", "error": str(e)}
    else:
        raise HTTPException(status_code=403, detail="Unauthorized host")