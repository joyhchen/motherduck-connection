from pandas import DataFrame
from streamlit.connections import ExperimentalBaseConnection
from streamlit.runtime.caching import cache_resource
import streamlit as st

import duckdb


class MotherDuckConnection(
    ExperimentalBaseConnection[duckdb.DuckDBPyConnection]
):
    def _connect(self, database=None, **kwargs) -> duckdb.DuckDBPyConnection:
        """
        Creates a connection to MotherDuck.

        Args:
            database (str): The path to the DuckDB database.
            If no path is given, the connection will use the
            default database set in MotherDuck (my_db).

        Returns:
            A DuckDBPyConnection object representing the connection to the database.
        """

        return duckdb.connect('md:?motherduck_token='+st.secrets['MOTHERDUCK_SERVICE_TOKEN'])

    def query(self, query: str) -> DataFrame:
        """
        Executes a SQL query and returns the result as a DataFrame.

        Args:
            query (str): The SQL query to execute.

        Returns:
            DataFrame: The result of the query as a DataFrame.
        """

        @cache_resource
        def _query(_self, query: str) -> DataFrame:
            conn = _self._connect()
            return conn.sql(query=query).df()

        return _query(self, query)
