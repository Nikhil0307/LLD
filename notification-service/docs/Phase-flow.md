### 🚦 PHASE 1: Core Architecture & Interfaces

**Goal:** Define the basic building blocks of the service.

* What are the core entities? (e.g., `Notification`, `Channel`, `Dispatcher`)
* How would you represent different channels (email, SMS) generically?
* How will you send a notification through a generic interface?

---

### 🧩 PHASE 2: Channel Implementations

**Goal:** Implement individual notification channels.

* How do you implement specific channels like `EmailChannel` or `SMSChannel`?
* How do you ensure they conform to a common interface?
* How would you mock these for local testing?

---

### 🕹️ PHASE 3: Dispatcher and Queueing Logic

**Goal:** Handle queuing, retrying, and priority.

* How will you prioritize messages?
* How would you implement retries and backoffs?
* Will you use threads, a queue, or both?

---

### 🔌 PHASE 4: Extensibility & Configuration

**Goal:** Make the system configurable and plug-n-play.

* How can a new channel be added with minimal code changes?
* How will configs be used to enable/disable channels dynamically?

---

### 📊 PHASE 5: Metrics, Logging, and Observability

**Goal:** Make the system monitorable.

* What metrics would you track? (e.g., delivery success rate, latency)
* How would you expose those metrics?
* How would you handle logging across retries and failures?
