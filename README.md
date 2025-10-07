[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/YuDOvrIX)
# Config Lookup — Find It in the JSON

## Story
You inherited a messy configuration: nested dicts and lists. You need a quick lookup to find the **first occurrence** of a key anywhere in the structure so you can confirm a flag or default.

## Technical Description
Write:

```py
find_key(data, key) -> any | None
```

where `data` is a nested structure of dicts, lists, and tuples, and `key` is a string.

### data can be:

- dict: search keys; recurse into values
- list/tuple: recurse into elements
- anything else: ignore
- Return the first value found in a depth-first, left-to-right search, or None if absent.

### Hints
- Base: non-collection → None.
- Dict: check if key exists here before recursing into values.
- Lists: scan in order.

### Run Tests Locally
```bash
python -m pytest -q
```
## Common Problems

- Searching lists but skipping dicts inside.
- Returning False instead of None when value is falsy (0, "", False).
- Not short-circuiting after a match.