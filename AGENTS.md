# Base44 Dev Environment

## Project Overview
A simple Python calculator module (`calculator.py`) with pytest tests (`test_calculator.py`).
A Flask web app (`app.py`) provides a browser UI so the calculator is visible in the preview.

## Running
```
docker compose -f docker-compose.base44.yml up -d
```
- Web UI on port 3000 (Flask dev server, auto-reloads on file change).
## Tests
```
docker compose -f docker-compose.base44.yml run --rm web sh -c "pip install -q -r requirements.txt && python -m pytest -v"
```

## No external secrets required.
