# Version Management & Release Consistency

- Tags must follow `vX.Y.Z` (e.g., `v0.2.1`).
- `[project].version` in `pyproject.toml` must equal the tag without the leading `v`.
- Never create a Git tag before updating and committing the version.

## Pre-Release Checklist

```bash
# 1) Update version in pyproject.toml to X.Y.Z
uv run python -m build
ls -la dist/  # verify X.Y.Z

git add pyproject.toml
git commit -m "feat: Bump version to X.Y.Z"
git push origin main

git tag vX.Y.Z
git push origin vX.Y.Z
```

## CI Guardrail

Add a check in the release workflow to fail if the tag does not match `pyproject.toml`.

```yaml
- name: Verify version matches tag
  if: startsWith(github.ref, 'refs/tags/')
  run: |
    TAG="${GITHUB_REF_NAME#v}"
    PYPROJECT_VERSION=$(python - <<'PY'
import sys
try:
    import tomllib
except ModuleNotFoundError:
    import tomli as tomllib
with open('pyproject.toml','rb') as f:
    print(tomllib.load(f)['project']['version'])
PY
    )
    echo "Tag: $TAG"
    echo "Project version: $PYPROJECT_VERSION"
    if [ "$TAG" != "$PYPROJECT_VERSION" ]; then
      echo "ERROR: Tag ($TAG) does not match project version ($PYPROJECT_VERSION)" >&2
      exit 1
    fi
```

## Versioning Policy

- Semantic Versioning: MAJOR.MINOR.PATCH
- Patch: fixes/internal changes
- Minor: backward-compatible features
- Major: breaking changes

