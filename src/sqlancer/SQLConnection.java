package sqlancer;

import java.sql.Connection;
import java.sql.DatabaseMetaData;
import java.sql.SQLException;
import java.sql.Statement;
import java.sql.PreparedStatement;

public class SQLConnection implements SQLancerDBConnection {

    private final Connection connection;

    public SQLConnection(Connection connection) {
        this.connection = connection;
    }

    @Override
    public String getDatabaseVersion() throws SQLException {
        DatabaseMetaData meta = connection.getMetaData();
        return meta.getDatabaseProductVersion();
    }

    @Override
    public void close() throws SQLException {
        connection.close();
    }

    public PreparedStatement prepareStatement(String arg) throws SQLException {
        return connection.prepareStatement(arg);
    }

    public Statement createStatement() throws SQLException {
        return connection.createStatement();
    }
}
