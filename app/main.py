from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        # Use the `subprocess.run` function to avoid shell=True and potential injection
        result = subprocess.run(['ping', host], check=True, text=True, capture_output=True)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}

if __name__ == "__main__":
    import uvicorn
    # Use a specific host instead of '0.0.0.0'
    uvicorn.run(app, host="127.0.0.1", port=8000)