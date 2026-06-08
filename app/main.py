from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping_route(host: str):
    # Validate input to prevent OS command injection
    if not host.isalnum() or ' ' in host:
        return {"status": "error", "message": "Invalid input"}
    try:
        output = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {"status": "completed", "output": output.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "error", "message": str(e)}

# Additional preventive controls
@app.on_event("startup")
def startup_event():
    app.include_router(ping_route)

@app.on_event("shutdown")
def shutdown_event():
    pass