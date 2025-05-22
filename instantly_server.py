import json
from typing import Any, Dict
from fastapi import FastAPI
from fastapi.responses import JSONResponse

from fastmcp import FastMCP

app = FastAPI()

API_BASE_URL = "https://api.instantly.ai/api/v2"
API_KEY = "YOUR_API_KEY"  # Replace with your Instantly API key

# Initialize FastMCP client (v2)
client = FastMCP(api_key=API_KEY, base_url=API_BASE_URL)


def call_instantly(endpoint: str, method: str = "GET", data: Dict[str, Any] | None = None) -> Dict[str, Any]:
    """Wrapper around the FastMCP client."""
    return client.call(endpoint, method=method, data=data)


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
