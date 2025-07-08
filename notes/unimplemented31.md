
# Unimplemented Limbo feature example 

False flag error, the problem is the `PRAGMA temp.cache_size = 0; -- 0ms;` which is not yet implemented, but the sqlancer error message is misleading.

```txt
something bad happened
java.lang.AssertionError: COMMIT TRANSACTION;
        at sqlancer.common.query.SQLQueryAdapter.checkException(SQLQueryAdapter.java:124)
        at sqlancer.common.query.SQLQueryAdapter.execute(SQLQueryAdapter.java:106)
        at sqlancer.Main$QueryManager.execute(Main.java:393)
        at sqlancer.GlobalState.executeStatement(GlobalState.java:108)
        at sqlancer.limbo.LimboProvider.generateDatabase(LimboProvider.java:175)
        at sqlancer.limbo.LimboProvider.generateDatabase(LimboProvider.java:1)
        at sqlancer.ProviderAdapter.generateAndTestDatabase(ProviderAdapter.java:57)
        at sqlancer.Main$DBMSExecutor.run(Main.java:506)
        at sqlancer.Main$2.run(Main.java:813)
        at sqlancer.Main$2.runThread(Main.java:780)
        at sqlancer.Main$2.run(Main.java:767)
        at java.base/java.util.concurrent.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1144)
        at java.base/java.util.concurrent.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:642)
        at java.base/java.lang.Thread.run(Thread.java:1589)
Caused by: java.sql.SQLException: step() returned invalid result: LimboStepResult{stepResultName=ERROR, result=null}
        at tech.turso.core.LimboResultSet.next(LimboResultSet.java:90)
        at tech.turso.core.LimboStatement.execute(LimboStatement.java:45)
        at tech.turso.jdbc4.JDBC4Statement.lambda$execute$1(JDBC4Statement.java:176)
        at tech.turso.jdbc4.JDBC4Statement.withConnectionTimeout(JDBC4Statement.java:372)
        at tech.turso.jdbc4.JDBC4Statement.execute(JDBC4Statement.java:170)
        at sqlancer.common.query.SQLQueryAdapter.execute(SQLQueryAdapter.java:100)
```

## sqlancer output

```sql
-- Time: 2025/07/03 23:54:27
-- Database: database0
-- Database version: 
-- seed value: 1751601267610
CREATE TABLE IF NOT EXISTS t0 (c0 INT , c1 REAL , c2 TEXT ); -- 1ms;
PRAGMA temp.cache_size = 0; -- 0ms;
PRAGMA auto_vacuum; -- 1ms;
CREATE TABLE IF NOT EXISTS t1 (c0 BLOB ); -- 1ms;
PRAGMA auto_vacuum = FULL; -- 0ms;
CREATE TABLE IF NOT EXISTS t2 (c0 INTEGER ); -- 0ms;
UPDATE t1 SET c0=0.4427479526784235 WHERE (t1.c0 COLLATE RTRIM IN ()); -- 0ms;
PRAGMA main.integrity_check; -- 0ms;
PRAGMA main.cache_size = 0; -- 0ms;
INSERT INTO t0 VALUES (0.9327886134372394, '', '-757883197'), (x'', '', -757883197), (NULL, x'', NULL); -- 0ms;
CREATE TABLE IF NOT EXISTS t3 (c0 BLOB ); -- 0ms;
PRAGMA auto_vacuum = NONE; -- 0ms;
CREATE TABLE IF NOT EXISTS  t4 (c0 BLOB , c1 INTEGER , c2 INTEGER , c3 INTEGER , c4 BLOB NOT NULL ); -- 0ms;
CREATE TABLE IF NOT EXISTS t5 (c0 REAL NOT NULL ); -- 0ms;
CREATE TABLE IF NOT EXISTS  t6 (c0 REAL , c1 INT , c2 INTEGER ); -- 1ms;
PRAGMA main.journal_mode; -- 0ms;
PRAGMA main.journal_mode = WAL; -- 0ms;
PRAGMA legacy_file_format; -- 0ms;
CREATE TABLE IF NOT EXISTS t7 (c0 TEXT ); -- 1ms;
CREATE TABLE IF NOT EXISTS  t8 (c0 TEXT , c1 INTEGER , c2 TEXT ); -- 0ms;
PRAGMA main.integrity_check; -- 0ms;
PRAGMA cache_size; -- 1ms;
PRAGMA integrity_check; -- 0ms;
INSERT INTO t7 VALUES ('-757883197'), (x'e1b7'), ('-757883197'); -- 0ms;
COMMIT TRANSACTION;
```