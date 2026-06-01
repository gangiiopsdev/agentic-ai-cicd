from fastapi import FastAPI
import subprocess
def run_ping(host: str):    # Helper function to safely ping a host
    args = ['ping', '-c', '4', host]  # Use list for arguments
    result = subprocess.run(args, capture_output=True, text=True)  # Run the command safely
    return result.stdout
class PingRouter:
    @staticmethod
    def ping(host: str):        if not host.isdigit():            raise ValueError("Invalid input")        return run_ping(host)
class PingApp(FastAPI):
    ping_router = PingRouter()
app = PingApp()

@app.get="/ping")
def ping(host: str):    try:
        response = PingApp.ping_router.ping(host)  # Use the safe function
        return {"status": "completed", "response": response}
    except ValueError as e:
        return {"error": str(e), "status": "failed"}