## TODO: Distributed Rate Limiting Strategy

### Goal:
Support high-availability, horizontally-scalable rate limiting with Redis coordination and local fallback.

---

### Tasks:
- [ ] Create `RedisFixedWindowStrategy` (uses atomic `INCR + EXPIRE`)
- [ ] Add fallback to `FixedWindowRateLimitingStrategy` when Redis is down
- [ ] Log Redis health events and fallback triggers
- [ ] Make fallback cache duration configurable (env or config)
- [ ] Add optional Redlock support for critical paths
- [ ] Make strategy pluggable via config (env: `RATE_LIMIT_STRATEGY=redis`)
- [ ] Write integration tests for Redis + fallback behavior
- [ ] Document the strategy and deployment recommendations

---

### Redis Keys
- Format: `rate_limit:{client_id}`
- TTL: 60s (same as window size)
