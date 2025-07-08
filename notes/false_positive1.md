# Bug report

False positive, there is no transaction, so the user shouldn't be able to execute `END TRANSACTION;`

## sqlancer output

```sql
-- Time: 2025/07/04 00:07:04
-- Database: database0
-- Database version: 
-- seed value: 1751602024732
CREATE TABLE IF NOT EXISTS t0 (c0 INT ); -- 0ms;
CREATE TABLE IF NOT EXISTS t1 (c0 BLOB , c1 REAL , c2 TEXT ); -- 0ms;
PRAGMA legacy_file_format = false; -- 0ms;
INSERT INTO t0(c0) VALUES (0.09127442686320586); -- 0ms;
PRAGMA auto_vacuum; -- 0ms;
PRAGMA main.journal_mode; -- 0ms;
CREATE TABLE IF NOT EXISTS t2 (c0 INT , c1 INTEGER , c2 INTEGER ); -- 0ms;
CREATE TABLE IF NOT EXISTS t3 (c0 INTEGER ); -- 1ms;
PRAGMA integrity_check; -- 0ms;
INSERT INTO t0(c0) VALUES ('-1453765701'); -- 0ms;
INSERT INTO t1 VALUES (NULL, NULL, NULL), ('-1453765701', x'', '-1453765701'), (x'', '', ''); -- 0ms;
PRAGMA auto_vacuum; -- 0ms;
INSERT INTO t1(c0) VALUES (x'3dc7'); -- 0ms;
PRAGMA legacy_file_format; -- 0ms;
INSERT INTO t0(c0) VALUES (''); -- 1ms;
PRAGMA legacy_file_format = false; -- 0ms;
CREATE TABLE IF NOT EXISTS  t4 (c0 REAL , c1 REAL , c2 INT ); -- 0ms;
INSERT INTO t4(c0, c2, c1) VALUES ('', '-1e500', -1.453765701E9); -- 0ms;
CREATE TABLE IF NOT EXISTS t5 (c0 BLOB NOT NULL ); -- 0ms;
PRAGMA temp.legacy_file_format; -- 1ms;
PRAGMA main.auto_vacuum; -- 0ms;
CREATE TABLE IF NOT EXISTS  t6 (c0 INT ); -- 0ms;
PRAGMA journal_mode = TRUNCATE; -- 0ms;
CREATE TABLE IF NOT EXISTS t7 (c0 TEXT ); -- 0ms;
PRAGMA main.journal_mode = DELETE; -- 0ms;
INSERT INTO t0(c0) VALUES (NULL); -- 0ms;
END TRANSACTION;
```

## rust error

```txt
java.lang.AssertionError: END TRANSACTION;
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

