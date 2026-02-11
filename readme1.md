Below is a **very simple, beginner-friendly solution** that you can run in **VS Code**.
It avoids advanced concepts and uses only **basic Python**, `regex`, and `pytest`.

---

## What this program does (in simple words)

✔ Removes comments
✔ Ignores empty lines
✔ Reads valid `key = value` pairs
✔ Detects **malformed lines** using regex
✔ Stores config data in a **dictionary**
✔ Includes **pytest tests** to catch bad input

---

## 1️⃣ Example config file (`config.txt`)

```txt
# This is a comment
host = localhost
port = 8080

debug = true
port = 9090   # duplicate key (last one wins)

wrongline
= novalue
```

---

## 2️⃣ Main Python file (`config_sanitizer.py`)

```python
import re

def load_config(text):
    config = {}
    errors = []

    # regex for valid key=value
    pattern = re.compile(r'^\s*([a-zA-Z_]+)\s*=\s*(.+)\s*$')

    lines = text.splitlines()

    for line_number, line in enumerate(lines, start=1):
        line = line.strip()

        # ignore empty lines and comments
        if not line or line.startswith("#"):
            continue

        match = pattern.match(line)
        if match:
            key = match.group(1)
            value = match.group(2)
            config[key] = value  # duplicate keys overwritten
        else:
            errors.append((line_number, line))

    return config, errors
```

---

## 3️⃣ How to run it manually (optional test)

```python
from config_sanitizer import load_config

with open("config.txt") as f:
    text = f.read()

config, errors = load_config(text)

print("CONFIG:", config)
print("ERRORS:", errors)
```

---

## 4️⃣ Pytest file (`test_config_sanitizer.py`)

> Install pytest first (only once):

```bash
pip install pytest
```

```python
from config_sanitizer import load_config

def test_valid_config():
    text = """
    host = localhost
    port = 8080
    """
    config, errors = load_config(text)
    assert config["host"] == "localhost"
    assert config["port"] == "8080"
    assert errors == []

def test_malformed_lines():
    text = """
    host localhost
    = no_key
    """
    config, errors = load_config(text)
    assert len(errors) == 2

def test_duplicate_keys():
    text = """
    port = 8080
    port = 9090
    """
    config, errors = load_config(text)
    assert config["port"] == "9090"
```

---

## 5️⃣ Run tests in VS Code terminal

```bash
pytest
```

---

## ✅ Optimized Structure Used

* **Dictionary (`dict`)** → fast lookup, simple, efficient
* No classes
* No complex patterns
* Easy to read & modify

---

## 🧠 Summary (for exams / interviews)

* Regex validates `key=value`
* Comments & empty lines ignored
* Malformed lines collected with line numbers
* Duplicate keys overridden
* Pytest ensures reliability

---

If you want:

* 🔹 even simpler version
* 🔹 comments removed automatically
* 🔹 error messages printed nicely

Just tell me 👍
----------------------------------

No problem 👍 I’ll make it **VERY EASY**, step-by-step, with **clear comments** so you can understand everything.

---

### ✅ FULL SIMPLE CODE (WITH EXPLANATION COMMENTS)

```python
import re   # used to match key = value format

def read_config(lines):
    config = {}   # store correct key-value pairs
    errors = []   # store wrong lines

    # this pattern checks: word = something
    pattern = re.compile(r"(\w+)\s*=\s*(.+)")

    # go through each line one by one
    for line_no, line in enumerate(lines, 1):

        line = line.strip()   # remove spaces and new line

        # if line is empty OR starts with #
        # then ignore it
        if line == "" or line.startswith("#"):
            continue

        # check if line matches "key = value"
        match = pattern.match(line)

        if match:
            # group(1) is the key
            key = match.group(1)

            # group(2) is the value
            value = match.group(2)

            # save in dictionary
            config[key] = value
        else:
            # line is wrong format, save error
            errors.append((line_no, line))

    # return good data and bad data
    return config, errors
```

---

### 🧪 EXAMPLE INPUT

```python
lines = [
    "# comment line",
    "name = John",
    "age = 25",
    "wrong line"
]
```

---

### ▶️ RUN THE FUNCTION

```python
config, errors = read_config(lines)

print("Config:", config)
print("Errors:", errors)
```

---

### 🟢 OUTPUT

```
Config: {'name': 'John', 'age': '25'}
Errors: [(4, 'wrong line')]
```

---

### 🧠 VERY SIMPLE LOGIC

1. Read one line
2. Remove spaces
3. Skip empty or comment lines
4. If line looks like `key = value` → save it
5. Else → mark as error

---

If you want **WITHOUT regex**, or **even simpler version**, tell me and I’ll rewrite it again 👌
