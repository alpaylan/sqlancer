
# Unimplemented Limbo feature example 

## sqlancer output

```sql
-- Time: 2025/07/03 23:20:36
-- Database: database0
-- Database version: 
-- seed value: 1751599236190
CREATE TABLE IF NOT EXISTS t0 (c0 BLOB , c1 REAL , c2 INT ); -- 1ms;
INSERT INTO t1 VALUES (CASE WHEN ((0.6126868698297103)*('棫s')) THEN ((NULL) BETWEEN ('R	''') AND (NULL)) END), (0.2287310015047299), (0.8250343181352288);
```

## rust error

```txt
thread '<unnamed>' panicked at core/translate/expr.rs:471:13:
internal error: entered unreachable code: expression should have been rewritten in optmizer
note: run with `RUST_BACKTRACE=1` environment variable to display a backtrace
```
