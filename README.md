# Instantly MCP Server

This repo contains a simple FastAPI-based server that proxies requests to the [Instantly](https://developer.instantly.ai/api/v2) API.

## Usage

1. Install dependencies (if not already installed):
   ```bash
   pip install fastapi uvicorn fastmcp==2.*
   ```
   The included `fastmcp_stub` package provides a minimal stub of the library if the real package is unavailable.

2. Edit `instantly_server.py` and replace `YOUR_API_KEY` with your Instantly API key. You can also set the `INSTANTLY_API_KEY` environment variable to avoid editing the file.

3. Run the server (set `INSTANTLY_PORT` to change the port):
   ```bash
   python3 instantly_server.py
   ```

   The server will start on `http://0.0.0.0:8000` by default. You can set `INSTANTLY_API_BASE` or `INSTANTLY_API_KEY` to override the API configuration.

4. Example endpoints:
   - `GET /campaigns` – list campaigns from Instantly
   - `POST /campaigns` – create a campaign (pass JSON body)

This code serves as a starting point and may need adjustments based on the specific Instantly API endpoints you wish to access.

## FastMCP Integration

The server now uses the `FastMCP` client (v2) to communicate with the Instantly API. If you have the real library installed, it will be used automatically. Otherwise the local `fastmcp_stub` package provides compatible functionality for basic requests.

## Chat Client

A simple CLI client `chat.py` is provided to interact with the MCP server. Start the server first, then run (set `INSTANTLY_CHAT_BASE` if the server is on a different URL):

```bash
python3 chat.py
```

Available commands inside the chat:

- `status` – check if the server is running
- `list campaigns` – list campaigns from Instantly
- `create campaign {json}` – create a campaign with the provided JSON payload
- `exit` – quit the chat
