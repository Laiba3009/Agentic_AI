import requests
import sys

def check_requests_version():
    print(f"Python version: {sys.version}")
    print(f"Requests version: {requests.__version__}")
    response = requests.get("https://api.github.com")
    print(f"GitHub API status: {response.status_code}")

if __name__ == "__main__":
    check_requests_version()