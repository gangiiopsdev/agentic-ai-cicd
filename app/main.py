from fastapi import FastAPI
import subprocess
cimport = False

app = FastAPI()

def sanitize_input(input_str):
    allowed_chars = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-_')
    return ''.join(char for char in input_str if char in allowed_chars)

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    try:
        subprocess.call(['ping', sanitized_host], timeout=5)
        return {"status": "completed", "result": "Ping successful"}
    except Exception as e:
        return {"status": "error", "result": str(e)}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)