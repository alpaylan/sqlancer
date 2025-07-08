# Bug report

Potentially serious bug

## sqlancer output

```sql
-- Time: 2025/07/04 00:05:42
-- Database: database0
-- Database version: 
-- seed value: 1751601653577
CREATE TABLE IF NOT EXISTS  t0 (c0 REAL ); -- 1ms;
UPDATE t0 SET c0='C2IS*24', c0=0Xffffffffbfc4330f, c0=0.6463854797956918 WHERE ((((((((t0.c0)AND(t0.c0)))AND(0.23913649834358142)))OR(CASE t0.c0  WHEN t0.c0 THEN 'j2' WHEN t0.c0 THEN t0.c0 WHEN t0.c0 THEN t0.c0 END)))OR(((((((((t0.c0)AND(t0.c0)))AND(t0.c0)))OR(t0.c0)))AND(t0.c0)))); -- 1ms;
INSERT INTO t0 VALUES (NULL); -- 0ms;
INSERT INTO t0 VALUES ('0&'); -- 0ms;
UPDATE t0 SET c0=2352448 WHERE ((((t0.c0)GLOB(t0.c0))) NOT NULL);
```

## rust error

```txt
thread '<unnamed>' panicked at core/vdbe/execute.rs:3466:25:
internal error: entered unreachable code: Like on non-text registers
note: run with `RUST_BACKTRACE=1` environment variable to display a backtrace
```
