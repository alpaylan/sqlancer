
# Unimplemented Limbo feature example 

## sqlancer output

```sql
-- Time: 2025/07/03 23:50:49
-- Database: database0
-- Database version: 
-- seed value: 1751601049155
CREATE TABLE IF NOT EXISTS  t0 (c0 INTEGER ); -- 1ms;
UPDATE t0 SET (c0)=('6I') WHERE CAST(CASE t0.c0  WHEN t0.c0 THEN NULL WHEN t0.c0 THEN t0.c0 WHEN t0.c0 THEN t0.c0 END AS INTEGER); -- 0ms;
UPDATE t0 SET (c0)=(-1996272085); -- 0ms;
INSERT INTO t0(c0) VALUES ('-1996272085'), ('-1996272085'), (0.7607565872434432); -- 0ms;
UPDATE t0 SET c0='1877036750'; -- 0ms;
PRAGMA main.cache_size; -- 0ms;
UPDATE t0 SET (c0)=('-1717372044') WHERE ((t0.c0)|(((t0.c0)<=(t0.c0)))); -- 0ms;
PRAGMA main.mmap_size;
```

## rust error

```txt
java.lang.AssertionError: PRAGMA main.mmap_size;
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
Caused by: tech.turso.exceptions.LimboException: LimboErrorCode{code=1200, message='Failed to prepare statement'} (Parse error: Not a valid pragma name)
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
