
### 📄 `phases.md`

---

#### **Phase 1: Interface Design**

* Define the `RateLimiter` interface.
* Determine the public methods (e.g., `allow_request(client_id)`).
* Think about how to initialize with parameters like `N`, `T`.

---

#### **Phase 2: Choose Initial Strategy**

* Pick a basic rate-limiting strategy (e.g., **fixed window** or **sliding window log**).
* Justify the choice (e.g., easier to implement vs more accurate).

---

#### **Phase 3: Core Data Structure**

* Design how you’ll store request timestamps per client.
* Choose an efficient structure (list, deque, heap?).

---

#### **Phase 4: Implementation**

* Implement `allow_request(client_id)` using the chosen strategy.
* Enforce per-client isolation.
* Reject requests appropriately.

---

#### **Phase 5: Thread Safety**

* Make your implementation thread-safe.
* Use `threading.Lock` or `collections.defaultdict` with locks per client.

---

#### **Phase 6: Testing**

* Simulate requests from different clients and assert the expected behavior.
* Write tests for edge cases (e.g., exactly at the limit, just over the limit, etc.).

---

#### **Phase 7: Extensibility Hooks**

* Make space in the design to support switching strategies easily later.
* Use strategy pattern if needed.

---