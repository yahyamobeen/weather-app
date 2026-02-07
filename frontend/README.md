# Weather frontend

Simple static frontend that accepts a city name and POSTs it to the server endpoint `/weather` as JSON: `{ "city": "City Name" }`.

Usage

- Serve the `frontend` folder (recommended) so fetch requests use the same origin as your FastAPI server, or configure CORS on the FastAPI side.

Run a quick static server from the `frontend` folder:

```bash
cd frontend
python -m http.server 8000
# then open http://localhost:8000 in your browser
```

FastAPI endpoint

- The frontend sends a POST to `/weather`. Implement a matching FastAPI route (POST `/weather`) that accepts JSON `{ "city": "..." }` and returns JSON with weather data.
