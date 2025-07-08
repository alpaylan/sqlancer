
# Unimplemented Limbo feature example 

## sqlancer output

```sql
-- Time: 2025/07/03 23:33:23
-- Database: database0
-- Database version: 
-- seed value: 1751600003787
CREATE TABLE IF NOT EXISTS  t0 (c0 INT ); -- 2ms;
PRAGMA auto_vacuum; -- 0ms;
UPDATE t1 SET c0=x''; -- 0ms;
INSERT INTO t0(c0) VALUES (x''); -- 0ms;
UPDATE t0 SET c2=x'' WHERE ((((t0.c1)||(t0.c2))) IS TRUE);
```

## rust error

```txt
thread '<unnamed>' panicked at core/vdbe/execute.rs:6349:17:
not yet implemented: TODO: Handle Blob conversion to String
note: run with `RUST_BACKTRACE=1` environment variable to display a backtrace
```
