from fastapi import FastAPI
import subprocess
cimport socketio

app = FastAPI()
sio = socketio.Client()

@app.get("/ping")
def ping(host: str):
    try:
        # Use socket to ping the host safely
        response = socketio.emit('ping', {'host': host}, namespace='/test')
        return {"status": "completed", "response": response}
    except Exception as e:
        return {"status": "failed", "error": str(e)}