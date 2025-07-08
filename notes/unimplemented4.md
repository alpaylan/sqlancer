
# Unimplemented Limbo feature example 

## sqlancer output

```sql
-- Time: 2025/07/03 22:40:19
-- Database: database0
-- Database version: 
-- seed value: 1751596819006
CREATE TABLE IF NOT EXISTS  t0 (c0 INTEGER ); -- 1ms;
UPDATE t0 SET (c0)=(NULL); -- 0ms;
CREATE TABLE IF NOT EXISTS t2 (c0 REAL ); -- 1ms;
UPDATE t1 SET (c0)=('1941513480'); -- 0ms;
PRAGMA wal_checkpoint(TRUNCATE);
```

## rust error

```txt
--java.lang.AssertionError: PRAGMA wal_checkpoint(TRUNCATE);
--      at sqlancer.common.query.SQLQueryAdapter.checkException(SQLQueryAdapter.java:124)
--      at sqlancer.common.query.SQLQueryAdapter.execute(SQLQueryAdapter.java:106)
--      at sqlancer.Main$QueryManager.execute(Main.java:393)
--      at sqlancer.GlobalState.executeStatement(GlobalState.java:108)
--      at sqlancer.StatementExecutor.executeStatements(StatementExecutor.java:70)
--      at sqlancer.limbo.LimboProvider.generateDatabase(LimboProvider.java:169)
--      at sqlancer.limbo.LimboProvider.generateDatabase(LimboProvider.java:1)
--      at sqlancer.ProviderAdapter.generateAndTestDatabase(ProviderAdapter.java:57)
--      at sqlancer.Main$DBMSExecutor.run(Main.java:506)
--      at sqlancer.Main$2.run(Main.java:813)
--      at sqlancer.Main$2.runThread(Main.java:780)
--      at sqlancer.Main$2.run(Main.java:767)
--      at java.base/java.util.concurrent.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1144)
--      at java.base/java.util.concurrent.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:642)
--      at java.base/java.lang.Thread.run(Thread.java:1589)
--Caused by: tech.turso.exceptions.LimboException: LimboErrorCode{code=1200, message='Failed to prepare statement'} (Parse error: only Passive mode supported)
--      at tech.turso.utils.LimboExceptionUtils.buildLimboException(LimboExceptionUtils.java:39)
--      at tech.turso.utils.LimboExceptionUtils.throwLimboException(LimboExceptionUtils.java:20)
--      at tech.turso.core.LimboConnection.throwLimboException(LimboConnection.java:122)
--      at tech.turso.core.LimboConnection.prepareUtf8(Native Method)
--      at tech.turso.core.LimboConnection.prepare(LimboConnection.java:81)
--      at tech.turso.jdbc4.JDBC4Connection.prepare(JDBC4Connection.java:30)
--      at tech.turso.jdbc4.JDBC4Statement.lambda$execute$1(JDBC4Statement.java:175)
--      at tech.turso.jdbc4.JDBC4Statement.withConnectionTimeout(JDBC4Statement.java:372)
--      at tech.turso.jdbc4.JDBC4Statement.execute(JDBC4Statement.java:170)
--      at sqlancer.common.query.SQLQueryAdapter.execute(SQLQueryAdapter.java:100)
```
