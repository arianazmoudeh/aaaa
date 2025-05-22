import json
from typing import Any, Dict
from fastapi import FastAPI
from fastapi.responses import JSONResponse
import urllib.request
import urllib.error

app = FastAPI()

API_BASE_URL = "https://api.instantly.ai/api/v2"
API_KEY = "YOUR_API_KEY"  # Replace with your Instantly API key


def call_instantly(endpoint: str, method: str = "GET", data: Dict[str, Any] | None = None) -> Dict[str, Any]:
    url = f"{API_BASE_URL}{endpoint}"
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
        "Accept": "application/json",
    }
    req_data = None
    if data is not None:
        req_data = json.dumps(data).encode("utf-8")
    req = urllib.request.Request(url, data=req_data, headers=headers, method=method)
    try:
        with urllib.request.urlopen(req) as resp:
            resp_data = resp.read().decode("utf-8")
            return json.loads(resp_data)
    except urllib.error.HTTPError as e:
        error_msg = e.read().decode("utf-8")
        return {"error": e.code, "message": error_msg}
    except urllib.error.URLError as e:
        return {"error": "network", "message": str(e.reason)}


@app.get("/campaigns")
def list_campaigns():
    result = call_instantly("/campaigns")
    return JSONResponse(content=result)


@app.post("/campaigns")
def create_campaign(payload: Dict[str, Any]):
    result = call_instantly("/campaigns", method="POST", data=payload)
    return JSONResponse(content=result)


@app.get("/")
def read_root():
    return {"status": "Instantly MCP server running"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
