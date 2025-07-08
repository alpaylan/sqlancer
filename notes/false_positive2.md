# Bug report

False positive, the error is in the last 2 interactions where `t1` has the `NOT NULL` constraint but the `INSERT` statement tries to insert a `NULL` value. SQLancer gives this as a bug.

## sqlancer output

```sql
-- Time: 2025/07/04 00:16:14
-- Database: database0
-- Database version: 
-- seed value: 1751602574808
CREATE TABLE IF NOT EXISTS  t0 (c0 BLOB ); -- 1ms;
INSERT INTO t0 VALUES (''); -- 1ms;
PRAGMA temp.auto_vacuum; -- 0ms;
PRAGMA journal_mode = WAL; -- 1ms;
INSERT INTO t0(c0) VALUES (x'c2fb'); -- 0ms;
INSERT INTO t0 VALUES (''); -- 0ms;
PRAGMA auto_vacuum = NONE; -- 0ms;
INSERT INTO t0(c0) VALUES (NULL); -- 1ms;
INSERT INTO t0 VALUES (0.6665612729498067); -- 0ms;
INSERT INTO t0(c0) VALUES (0.5634832719424407); -- 0ms;
PRAGMA main.legacy_file_format; -- 0ms;
INSERT INTO t0(c0) VALUES (-1704494650), (NULL), (0.6094110206918171); -- 0ms;
INSERT INTO t0(c0) VALUES (0.6094110206918171); -- 1ms;
PRAGMA journal_mode = WAL; -- 0ms;
CREATE TABLE IF NOT EXISTS t1 (c0 BLOB NOT NULL ); -- 0ms;
INSERT INTO t1 VALUES (NULL);
```

## rust error

```txt
something bad happened
java.lang.AssertionError: INSERT INTO t1 VALUES (NULL);
        at sqlancer.common.query.SQLQueryAdapter.checkException(SQLQueryAdapter.java:124)
        at sqlancer.common.query.SQLQueryAdapter.execute(SQLQueryAdapter.java:106)
        at sqlancer.Main$QueryManager.execute(Main.java:393)
        at sqlancer.GlobalState.executeStatement(GlobalState.java:108)
        at sqlancer.StatementExecutor.executeStatements(StatementExecutor.java:70)
        at sqlancer.limbo.LimboProvider.generateDatabase(LimboProvider.java:169)
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
