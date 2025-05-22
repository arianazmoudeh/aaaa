import json
from typing import Dict, Any
import urllib.request
import urllib.error


def send_request(url: str, method: str = "GET", data: Dict[str, Any] | None = None) -> Dict[str, Any]:
    """Send an HTTP request to the MCP server."""
    req_data = None
    if data is not None:
        req_data = json.dumps(data).encode("utf-8")
    req = urllib.request.Request(url, data=req_data, method=method)
    req.add_header("Content-Type", "application/json")
    try:
        with urllib.request.urlopen(req) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        return {"error": e.code, "message": e.read().decode("utf-8")}
    except urllib.error.URLError as e:
        return {"error": "network", "message": str(e.reason)}


def run_chat(api_base: str) -> None:
    """Simple interactive chat with the MCP server."""
    print("Instantly MCP chat client")
    print("Type 'help' for commands, 'exit' to quit.")
    while True:
        try:
            user_input = input("> ").strip()
        except EOFError:
            break
        if not user_input:
            continue
        command = user_input.lower()
        if command in {"exit", "quit"}:
            break
        if command == "help":
            print("Commands:\n  list campaigns\n  create campaign {json}\n  status")
            continue
        if command.startswith("list campaigns"):
            resp = send_request(f"{api_base}/campaigns")
            print(json.dumps(resp, indent=2))
            continue
        if command.startswith("create campaign"):
            payload = user_input[len("create campaign"):].strip()
            if not payload:
                print("Payload required after 'create campaign'")
                continue
            try:
                data = json.loads(payload)
            except json.JSONDecodeError as e:
                print(f"Invalid JSON: {e}")
                continue
            resp = send_request(f"{api_base}/campaigns", method="POST", data=data)
            print(json.dumps(resp, indent=2))
            continue
        if command == "status":
            resp = send_request(f"{api_base}/")
            print(json.dumps(resp, indent=2))
            continue
        print("Unknown command. Type 'help' for options.")


if __name__ == "__main__":
    import os
    API_BASE = os.getenv("INSTANTLY_CHAT_BASE", "http://localhost:8000")
    run_chat(API_BASE)
