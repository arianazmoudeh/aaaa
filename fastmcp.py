from __future__ import annotations

import json
from typing import Any, Dict, Optional
import urllib.request
import urllib.error


class FastMCP:
    """Minimal stub implementation of the FastMCP v2 client."""

    def __init__(self, api_key: str, base_url: str) -> None:
        self.api_key = api_key
        self.base_url = base_url.rstrip("/")

    def call(self, endpoint: str, method: str = "GET", data: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        url = f"{self.base_url}{endpoint}"
        headers = {
            "Authorization": f"Bearer {self.api_key}",
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
