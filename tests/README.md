# Validation Tests

Run from the repository root:

```bash
python tools/validate_content.py
python -m unittest discover -s tests -v
```

The tests validate JSON loading, unique stable IDs, mission and evidence references, and the complete Isaiah investigation chain.
