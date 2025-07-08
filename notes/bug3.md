# Duplicate bug report

Not sure if it's a bug, doesn't show up on the CLI

## sqlancer output

```sql
-- Time: 2025/07/03 23:47:09
-- Database: database0
-- Database version: 
-- seed value: 1751600810502
CREATE TABLE IF NOT EXISTS t0 (c0 INT ); -- 1ms;
CREATE TABLE IF NOT EXISTS t1 (c0 INTEGER , c1 INTEGER NOT NULL , c2 BLOB ); -- 0ms;
UPDATE t0 SET c0=-1853344503, c0=-1228129389 WHERE CASE WHEN (~ (t0.c0)) THEN CAST(t0.c0 AS TEXT) END; -- 0ms;
UPDATE t0 SET c0=NULL; -- 0ms;
INSERT INTO t1(c0, c1) VALUES ('', NULL);
```

## rust error

```txt
bindings/java/src/main/java/tech/turso/jdbc4/JDBC4Connection.java:27 Preparing statement with SQL: INSERT INTO t1(c0, c1) VALUES ('', NULL);
something bad happened
java.lang.AssertionError: INSERT INTO t1(c0, c1) VALUES ('', NULL);
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
        ... 13 more
```
