# ⌨️ Commands and developer reference

The project is static and does not currently define npm scripts or a build command.

## Clone repository

```bash
git clone https://github.com/Brajesh31/Art-Gallery.git
cd Art-Gallery
```

## Start local preview

```bash
python -m http.server 8000
```

Open `http://localhost:8000`.

## Run repository validator

```bash
python scripts/validate_repository.py
```

## Run validator unit tests

```bash
python -m unittest discover -s tests -v
```

## Stop local preview

Press `Ctrl+C` in the terminal running the server.

## Notes

These commands use Python's standard library. They do not install application dependencies or modify the website's runtime. External CDNs still require network access for their resources.
