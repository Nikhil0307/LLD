### 📄 `probstatement.md`

**Title**: Build a Low-Level Rate Limiter in Python

**Problem Statement**:
Design and implement a low-level, in-memory rate limiter in Python that can throttle incoming requests based on specified constraints. The rate limiter should be generic and reusable. It should support multiple clients and apply rate limits individually per client.

**Requirements**:

* Each client should be allowed **N requests per T seconds**.
* Requests beyond the threshold should be rejected until the window resets.
* The limiter should work **without relying on external systems** like Redis or databases.
* It should support **thread-safe operations**.

**Goals**:

* Correctness: Enforce limits accurately.
* Efficiency: Handle a high volume of requests with minimal overhead.
* Extensibility: Should support different rate limiting strategies (fixed window, sliding window, token bucket) in the future.

---