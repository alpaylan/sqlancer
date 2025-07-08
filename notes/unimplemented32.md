

## sqlancer log

```sql
-- Time: 2025/07/04 09:24:09
-- Database: database0
-- Database version: 
-- seed value: 1751635449099
CREATE TABLE IF NOT EXISTS  t0 (c0 BLOB ); -- 1ms;
CREATE TABLE IF NOT EXISTS t1 (c0 REAL ); -- 0ms;
PRAGMA temp.journal_mode = TRUNCATE; -- 0ms;
CREATE TABLE IF NOT EXISTS  t2 (c0 INT , c1 BLOB , c2 TEXT ); -- 0ms;
INSERT INTO t2(c2) VALUES (''); -- 0ms;
PRAGMA journal_mode = PERSIST; -- 0ms;
UPDATE t0 SET (c0)=(NULL); -- 1ms;
CREATE TABLE IF NOT EXISTS t3 (c0 REAL ); -- 0ms;
INSERT INTO t0(c0) VALUES (NULL), (0.031441761362288156), ('1164173707'); -- 0ms;
INSERT INTO t2 VALUES (NULL, NULL, 'HScf\n'), (0.031441761362288156, 0.5948388866875784, NULL), (NULL, 0.5948388866875784, '-1571318406'); -- 0ms;
UPDATE t0 SET c0=1164173707 WHERE ((((t0.c0)OR(t0.c0)))AND(((t0.c0)>(x'')))); -- 0ms;
CREATE TABLE IF NOT EXISTS t99 (c0 INTEGER COLLATE NOCASE , c1 TEXT NOT NULL , c2 INT ); -- 0ms;
UPDATE t2 SET c2=x'', c1=x'', c1='-1571318406'; -- 0ms;
UPDATE t99 SET (c0)=(0.3478166586951804) WHERE ((((HEX(t99.c0))AND((NOT ('n')))))OR((+ (t99.c2)))); -- 0ms;
INSERT INTO t3 VALUES (0.7088607832382681); -- 1ms;
CREATE TABLE IF NOT EXISTS  t4 (c0 BLOB ); -- 0ms;
PRAGMA main.integrity_check; -- 0ms;
UPDATE t3 SET (c0)=(NULL); -- 0ms;
PRAGMA legacy_file_format = true; -- 1ms;
PRAGMA temp.integrity_check; -- 0ms;
PRAGMA auto_vacuum = INCREMENTAL; -- 0ms;
PRAGMA journal_mode; -- 0ms;
INSERT INTO t0 VALUES (x''); -- 0ms;
CREATE TABLE IF NOT EXISTS  t5 (c0 INT );
```

## limbo error

```txt
thread '<unnamed>' panicked at core/storage/pager.rs:532:21:
not implemented
note: run with `RUST_BACKTRACE=1` environment variable to display a backtrace
```