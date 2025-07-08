
# Unimplemented Limbo feature example 

## sqlancer output

```sql
-- Time: 2025/07/03 22:32:28
-- Database: database0
-- Database version: 
-- seed value: 1751596348851
CREATE TABLE IF NOT EXISTS t0 (c0 BLOB ); -- 1ms;
PRAGMA temp.shrink_memory;
```

## rust error

```txt
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
