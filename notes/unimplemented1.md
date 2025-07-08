# Unimplemented Limbo feature example 

## sqlancer output

```sql
-- Time: 2025/07/03 22:24:11
-- Database: database0
-- Database version: 
-- seed value: 1751595851843
CREATE TABLE IF NOT EXISTS t0 (c0 INT , c1 REAL , c2 INTEGER ); -- 1ms;
INSERT INTO t0(c0) VALUES (93679030); -- 1ms;
INSERT INTO t1(c0, c4, c2, c3, c1) VALUES ('93679030', '93679030', '1l*c+', NULL, NULL), (x'', 0X5956db6, x'fbe8', 1114721350, NULL), (NULL, NULL, NULL, '䱆涶', x'92ff'); -- 0ms;
UPDATE t0 SET (c0)=(x'') WHERE (0.060953660537542476 IN ()); -- 0ms;
INSERT INTO t0 VALUES (''); -- 0ms;
INSERT INTO t0 VALUES (''), (x''), (x'8084b1b0'); -- 0ms;
CREATE TABLE IF NOT EXISTS t98 (c0 REAL NOT NULL ); -- 0ms;
UPDATE t98 SET c0=NULL; -- 0ms;
UPDATE t98 SET c0='zD' WHERE ((t98.c0)+(((t98.c0)&(t98.c0)))); -- 0ms;
INSERT INTO t98 VALUES ('d涶~'); -- 0ms;
UPDATE t98 SET c0=x'' WHERE (((t98.c0 IN (t98.c0)))GLOB(((t98.c0) BETWEEN (t98.c0) AND (t98.c0))));
```

## rust error

```txt
thread '<unnamed>' panicked at core/translate/expr.rs:1971:37:
not yet implemented
note: run with `RUST_BACKTRACE=1` environment variable to display a backtrace
```
