# Unimplemented Limbo feature example 

## sqlancer output

```sql
-- Time: 2025/07/03 22:41:27
-- Database: database0
-- Database version: 
-- seed value: 1751596887199
CREATE TABLE IF NOT EXISTS  t0 (c0 BLOB ); -- 2ms;
UPDATE t2 SET c0=NULL; -- 1ms;
UPDATE t2 SET (c0)=(x'') WHERE ((((t2.c0)<(t2.c0))) BETWEEN ((((t2.c0)) NOT BETWEEN ((t2.c0)) AND ((t2.c0)))) AND (t2.c0)); -- 0ms;
UPDATE t2 SET c0='7S2', c0=NULL; -- 0ms;
UPDATE t2 SET (c0)=(NULL) WHERE (((t2.c0 IN (t2.c0))) NOTNULL);
```

## rust error

```txt
thread '<unnamed>' panicked at core/translate/expr.rs:1971:37:
not yet implemented
note: run with `RUST_BACKTRACE=1` environment variable to display a backtrace
```
