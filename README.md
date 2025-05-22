# Instantly MCP Server

This repo contains a simple FastAPI-based server that proxies requests to the [Instantly](https://developer.instantly.ai/api/v2) API.

## Usage

1. Install dependencies (if not already installed):
   ```bash
   pip install fastapi uvicorn
   ```
   The server uses only built-in modules for HTTP requests, so no external HTTP client is required.

2. Edit `instantly_server.py` and replace `YOUR_API_KEY` with your Instantly API key.

3. Run the server:
   ```bash
   python3 instantly_server.py
   ```

   The server will start on `http://0.0.0.0:8000`.

4. Example endpoints:
   - `GET /campaigns` – list campaigns from Instantly
   - `POST /campaigns` – create a campaign (pass JSON body)

This code serves as a starting point and may need adjustments based on the specific Instantly API endpoints you wish to access.
