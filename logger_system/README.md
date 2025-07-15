---

# 📝 Custom Python Logger

A **lightweight, thread-safe, asynchronous logging system** built from scratch in Python — complete with log level filtering, rotation, formatting, singleton pattern, and daily file handling. This logger is designed to be production-ready and extensible.

---

## 📦 Features

* ✅ Singleton design to avoid duplicate instances
* ✅ Thread-safe asynchronous logging via `queue.Queue`
* ✅ Configurable log levels: `DEBUG`, `INFO`, `WARNING`, `ERROR`
* ✅ Log rotation based on file size
* ✅ Daily log files with date-based naming
* ✅ Custom log format templates
* ✅ Optional console + file output support
* ✅ Extensible with metrics and structured logging

---

## 📂 Directory Structure

```
logger/
├── src/
│   └── logger.py          # Main Logger implementation
├── conf/
│   └── Constants.py       # Log level constants
├── logs/
│   └── YYYY-MM-DD.log     # Auto-created log files
└── main.py                # Sample usage
```

---

## ⚙️ Usage

### 1. ✅ Import and Initialize

```python
from src.logger import Logger
from conf.Constants import Constants

logger = Logger(
    log_dir='./logs',
    current_log_level=Constants.INFO,
    log_format="[{time}] {level}: {message}",
    max_log_size=5 * 1024 * 1024  # 5 MB
)
```

### 2. ✅ Log Messages

```python
logger.log("This is an info message.", level=Constants.INFO)
logger.log("This is a warning.", level=Constants.WARNING)
logger.log("Something went wrong!", level=Constants.ERROR)
logger.log("Debug details here.", level=Constants.DEBUG)
```

### 3. ✅ Shutdown on Exit

```python
logger.shutdown()
```

> 💡 *Alternatively, register shutdown with `atexit` to handle auto-cleanup.*

---

## 🛠 Constants Definition Example

```python
# conf/Constants.py
class Constants:
    DEBUG = "DEBUG"
    INFO = "INFO"
    WARNING = "WARNING"
    ERROR = "ERROR"
```

---

## 🧠 Design Highlights

| Feature                  | Description                                                     |
| ------------------------ | --------------------------------------------------------------- |
| **Singleton**            | Ensures one logger instance across app using `__new__`.         |
| **Thread Safety**        | Uses `threading.Lock` and background thread for writes.         |
| **Asynchronous Logging** | Messages are queued and written in a non-blocking way.          |
| **Log Rotation**         | Automatically rotates files if they exceed `max_log_size`.      |
| **Daily Files**          | New log file per day based on current date.                     |
| **Flexible Format**      | Supports custom templates like `"[{time}] {level}: {message}"`. |
| **Filter by Level**      | Skip messages lower than `current_log_level`.                   |

---

## 🌍 Coming Soon / To-Dos

* [ ] Support both file + console output targets
* [ ] JSON-formatted logs for machine parsing
* [ ] Metrics tracking (e.g., logs per level)
* [ ] Log retention policy (auto-delete old files)
* [ ] Remote logging over TCP/HTTP

---

## 📌 Example Output

```
[2025-07-15 22:14:59] INFO: App started successfully
[2025-07-15 22:15:01] WARNING: High memory usage
[2025-07-15 22:15:03] ERROR: Unable to connect to database
```

---

## 🧪 Test This Logger

```python
# main.py
from src.logger import Logger
from conf.Constants import Constants

if __name__ == "__main__":
    logger = Logger()
    for i in range(10):
        logger.log(f"Test info {i}", level=Constants.INFO)
        logger.log(f"Test warn {i}", level=Constants.WARNING)
        logger.log(f"Test error {i}", level=Constants.ERROR)
    logger.shutdown()
```

---

## 👨‍💻 Author

Built by \[Nikhil Baskar] as a hands-on exercise in building low-level systems in Python.

---