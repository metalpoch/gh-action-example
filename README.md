# gh-action-example

Proyecto Python de ejemplo con variables, bucles y funciones, dockerizado y publicado automáticamente en **GitHub Container Registry (GHCR)** mediante GitHub Actions.

## Contenido

| Archivo | Descripción |
| --- | --- |
| `main.py` | Script de ejemplo en Python |
| `Dockerfile` | Imagen basada en `python:3.12-slim` con usuario no-root |
| `.github/workflows/black.yml` | Formatea el código con **Black** y hace commit |
| `.github/workflows/docker.yml` | Construye y publica la imagen en **GHCR** |

## Ejecutar localmente

```bash
python main.py
```

## Docker

Construir la imagen:

```bash
docker build -t gh-action-example .
```

Ejecutar el contenedor:

```bash
docker run --rm gh-action-example
```

## Imagen publicada en GHCR

La imagen se publica en:

```
ghcr.io/metalpoch/gh-action-example
```

Descargar y ejecutar:

```bash
docker pull ghcr.io/metalpoch/gh-action-example:latest
docker run --rm ghcr.io/metalpoch/gh-action-example:latest
```

### Etiquetas (tags)

| Evento | Tags generados |
| --- | --- |
| Push a `main` / `master` | `latest`, `main`, `sha-<commit>` |
| Tag `vX.Y.Z` | `X.Y.Z`, `X.Y`, `sha-<commit>` |
| Pull request | `pr-<numero>`, `sha-<commit>` (solo build, sin push) |

## CI/CD

- **Black**: en cada push/PR formatea el código y commitea los cambios (`style: format code with black`).
- **Docker/GHCR**: en cada push/PR construye la imagen; en pushes y tags la publica en GHCR usando `GITHUB_TOKEN` (permisos `packages: write`).

> Si el paquete queda privado y quieres hacerlo público, ve a **Package settings → Change visibility**.

## Autenticación para descargar la imagen

Si el paquete es privado, inicia sesión antes del `pull`:

```bash
echo $GITHUB_TOKEN | docker login ghcr.io -u <usuario> --password-stdin
```
