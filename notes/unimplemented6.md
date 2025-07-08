# Unimplemented Limbo feature example 

## sqlancer output

```sql
-- Time: 2025/07/03 22:42:25
-- Database: database0
-- Database version: 
-- seed value: 1751596945993
CREATE TABLE IF NOT EXISTS  t0 (c0 TEXT COLLATE BINARY ); -- 1ms;
INSERT INTO t0 VALUES (NULL); -- 0ms;
CREATE TABLE IF NOT EXISTS t3 (c0 TEXT , c1 BLOB NOT NULL , c2 REAL , c3 INTEGER NOT NULL , c4 TEXT ); -- 1ms;
INSERT INTO t1(c0) VALUES ('338092398'); -- 0ms;
CREATE TABLE IF NOT EXISTS  t4 (c0 BLOB ); -- 0ms;
UPDATE t0 SET c0=NULL, c0=0.6560648714580498 WHERE UNICODE(t0.c0) COLLATE NOCASE;
```

```sql
-- Time: 2025/07/03 23:01:28
-- Database: database0
-- Database version: 
-- seed value: 1751598088297
CREATE TABLE IF NOT EXISTS t0 (c0 REAL , c1 TEXT , c2 REAL ); -- 0ms;
CREATE TABLE IF NOT EXISTS  t70 (c0 BLOB ); -- 1ms;
UPDATE t70 SET c0=0.5230389713608085, c0='H~'; -- 0ms;
UPDATE t70 SET c0='-li[', c0=NULL, c0='1310335969' WHERE (((t70.c0, t70.c0, t70.c0)) BETWEEN ((t70.c0, t70.c0, t70.c0)) AND ((t70.c0, t70.c0, t70.c0))) COLLATE RTRIM;
```

## rust error

```txt
thread '<unnamed>' panicked at core/translate/expr.rs:402:18:
not yet implemented: expression Collate(FunctionCall { name: Id("UNICODE"), distinctness: None, args: Some([Column { database: None, table: TableInternalId(1), column: 0, is_rowid_alias: false }]), order_by: None, filter_over: None }, "NOCASE") not implemented
note: run with `RUST_BACKTRACE=1` environment variable to display a backtrace
```
