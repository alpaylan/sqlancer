# Duplicate bug report

## sqlancer output

```sql
-- Time: 2025/07/03 22:43:13
-- Database: database0
-- Database version: 
-- seed value: 1751596993822
CREATE TABLE IF NOT EXISTS  t0 (c0 INTEGER ); -- 0ms;
UPDATE t0 SET (c0, c0, c0)=(NULL, 'HS', NULL) WHERE t0.c0;
```

```sql
-- Time: 2025/07/03 22:50:43
-- Database: database0
-- Database version: 
-- seed value: 1751597443752
CREATE TABLE IF NOT EXISTS t0 (c0 REAL ); -- 1ms;
UPDATE t0 SET c0='', c0=NULL WHERE LIKELY(t0.c0 COLLATE RTRIM); -- 0ms;
UPDATE t2 SET c0=NULL; -- 0ms;
UPDATE t2 SET c0=NULL WHERE ((((((t2.c0) ISNULL))OR(((((t2.c0)AND(t2.c0)))AND(t2.c0)))))AND((t2.c0 IN (t2.c0)))); -- 1ms;
UPDATE t5 SET (c0)=(-546619394); -- 0ms;
UPDATE t2 SET (c0, c0, c0)=(x'a599', 0Xffffffffdf6b3ffe, NULL) WHERE (((((((((NULL)OR(t2.c0)))AND(t2.c0)))AND(t2.c0)))AND(t2.c0)) IN (t2.c0 COLLATE RTRIM, t2.c0));
```


```sql
-- Time: 2025/07/03 22:52:30
-- Database: database0
-- Database version: 
-- seed value: 1751597550968
CREATE TABLE IF NOT EXISTS t0 (c0 BLOB , c1 BLOB , c2 TEXT ); -- 0ms;
UPDATE t1 SET (c0)=(0.4832662518529298); -- 0ms;
UPDATE t6 SET c0=NULL, c0=NULL; -- 0ms;
UPDATE t6 SET c0=0.9529198879574851, c0=x''; -- 0ms;
CREATE TABLE IF NOT EXISTS t8 (c0 INT ); -- 1ms;
INSERT INTO t0(c0) VALUES (',ᛗ'), (NULL), ('-56488775'); -- 0ms;
UPDATE t5 SET (c0, c0, c0)=(-18308481, -18308481, 'u^') WHERE (((LTRIM(t5.c0, t5.c0)))<>((LIKE(t5.c0, t5.c0, 'y'))));
```

## rust error

```txt
java.lang.AssertionError: UPDATE t0 SET (c0, c0, c0)=(NULL, 'HS', NULL) WHERE t0.c0;
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
Caused by: tech.turso.exceptions.LimboException: LimboErrorCode{code=1200, message='Failed to prepare statement'} (column "c0" specified more than once at (1, 23))
        at tech.turso.utils.LimboExceptionUtils.buildLimboException(LimboExceptionUtils.java:39)
        at tech.turso.utils.LimboExceptionUtils.throwLimboException(LimboExceptionUtils.java:20)
        at tech.turso.core.LimboConnection.throwLimboException(LimboConnection.java:122)
        at tech.turso.core.LimboConnection.prepareUtf8(Native Method)
        at tech.turso.core.LimboConnection.prepare(LimboConnection.java:81)
        at tech.turso.jdbc4.JDBC4Connection.prepare(JDBC4Connection.java:30)
        at tech.turso.jdbc4.JDBC4Statement.lambda$execute$1(JDBC4Statement.java:175)
        at tech.turso.jdbc4.JDBC4Statement.withConnectionTimeout(JDBC4Statement.java:372)
        at tech.turso.jdbc4.JDBC4Statement.execute(JDBC4Statement.java:170)
        at sqlancer.common.query.SQLQueryAdapter.execute(SQLQueryAdapter.java:100)
```
