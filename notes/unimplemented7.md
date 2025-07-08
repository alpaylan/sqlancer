# Unimplemented Limbo feature example 

## sqlancer output

```sql
-- Time: 2025/07/03 22:45:30
-- Database: database0
-- Database version: 
-- seed value: 1751597098669
CREATE TABLE IF NOT EXISTS t0 (c0 INTEGER ); -- 2ms;
CREATE TABLE IF NOT EXISTS t1 (c0 INT , c1 INTEGER , c2 INT , c3 TEXT , c4 BLOB ); -- 0ms;
UPDATE t1 SET (c3)=(0Xffffffff9d9b89f1) WHERE (((((t1.c2, t1.c2, t1.c0)) BETWEEN ((t1.c0, t1.c1, t1.c2)) AND ((t1.c2, t1.c1, t1.c3)))) NOT BETWEEN ((NOT (t1.c1))) AND (((t1.c3) NOT BETWEEN (t1.c0) AND (t1.c2))));
```

```sql
-- Time: 2025/07/03 22:58:23
-- Database: database0
-- Database version: 
-- seed value: 1751597903797
CREATE TABLE IF NOT EXISTS  t0 (c0 INT ); -- 1ms;
UPDATE t1 SET (c0)=('-839899768'); -- 0ms;
UPDATE t1 SET (c0)=(0xffffffff97df562a); -- 0ms;
UPDATE t1 SET c0=''; -- 0ms;
INSERT INTO t1 VALUES (NULL), (0X177e90b2), (x'6940'); -- 0ms;
UPDATE t1 SET c0='-839899768'; -- 1ms;
INSERT INTO t1 VALUES (0.18357126267598767); -- 0ms;
UPDATE t0 SET c0=NULL WHERE ((-839899768)<>((((t0.c0, t0.c0, t0.c0, t0.c0, t0.c0))<=((t0.c0, t0.c0, t0.c0, t0.c0, t0.c0)))));
```


## rust error

```txt
thread '<unnamed>' panicked at core/translate/expr.rs:2116:17:
not yet implemented: TODO: parenthesized expression with multiple arguments not yet supported
note: run with `RUST_BACKTRACE=1` environment variable to display a backtrace
```
