## 🔁 PHASE 1: Core Enhancements

### 1. ✅ Add Timestamps

**❓ How would you enhance your logger to include timestamps for each message?**

🔹 *Hint:* Use `datetime.now().strftime()` to format the current time and prepend it in the `log()` message.

---

### 2. ✅ Add Singleton Pattern

**❓ How can you avoid creating multiple Logger instances unnecessarily?**

🔹 *Hint:* Use a class-level variable to cache the instance and return that from a `get_instance()` method or override `__new__`.

---

### 3. ✅ Add Thread Safety

**❓ How would you ensure thread-safe writes to the log file?**

🔹 *Hint:* Use `threading.Lock()` in your class and acquire it before writing to the file. Release it after.

---

## 🔁 PHASE 2: Configurability

### 4. 🎛 Add Configurable Log Level Filtering

**❓ How would you skip writing DEBUG messages unless explicitly allowed?**

🔹 *Hint:* Store a `current_log_level` (e.g., INFO), and only write messages if their level is ≥ `current_log_level`.

---

### 5. 🛠 Add Custom Format Support

**❓ How would you let users define how logs are formatted? (e.g., with timestamps, line numbers, etc.)**

🔹 *Hint:* Accept a format string in `__init__`, like `"[{time}] {level}: {message}"`, and use `.format()` or f-strings with that.

---

## 🔁 PHASE 3: Production-Level Logging

### 6. 💥 Add Log Rotation

**❓ How would you rotate the log file if it exceeds a certain size (e.g., 5MB)?**

🔹 *Hint:* Check `os.path.getsize()` before writing. If size > limit, rename `application.log` → `application.log.1` and start a fresh one.

---

### 7. 📂 Support for Daily Log Files

**❓ How would you log to a file named with today’s date (e.g., `2025-07-15.log`)?**

🔹 *Hint:* Use `datetime.today().strftime("%Y-%m-%d")` to generate the filename in `__init__`.

---

### 8. 🧵 Add Asynchronous Logging (Optional Advanced)

**❓ How would you make logging non-blocking using a background thread or queue?**

🔹 *Hint:* Use a `queue.Queue()` to push log messages and let a background thread handle actual file writes.

---

### 9. 🌍 Add Console vs File Output

**❓ How would you support logging to both file and console?**

🔹 *Hint:* Accept an optional `output_targets` list (e.g., `['file', 'console']`) and log accordingly.

---

### 10. 📈 Add Metrics or Stats

**❓ How would you expose metrics like total logs written, logs by level, etc.?**

🔹 *Hint:* Use class-level counters to increment per `log()` call.

---