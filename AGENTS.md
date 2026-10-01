# Base44 Dev Environment

## Project Overview
A simple Python calculator module (`calculator.py`) with pytest tests (`test_calculator.py`).
A Flask web app (`app.py`) provides a browser UI so the calculator is visible in the preview.

## Running
```
docker compose -f docker-compose.base44.yml up -d
```
- Web UI on port 3000 (Flask dev server, auto-reloads on file change).
- Tests run as a one-shot `test` service after the web service is healthy.

## Tests
```
docker compose -f docker-compose.base44.yml run --rm test
```

## No external secrets required.
