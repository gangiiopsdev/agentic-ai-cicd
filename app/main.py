from fastapi import FastAPI
import subprocess
def safe_git_command(command):
    subprocess.run(' '.join(command), check=True, shell=False)
# Example usage: safe_git_command(['git', 'pull'])