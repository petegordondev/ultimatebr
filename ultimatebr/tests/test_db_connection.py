from django.db import connections, OperationalError
from django.test import SimpleTestCase

class PrimaryDatabaseConnectionTest(SimpleTestCase):
    databases = {'default'}  # Explicitly allow database access for this test case

    def test_primary_database_connection(self):
        """Test connection to the primary database."""
        db_conn = connections['default']
        try:
            db_conn.ensure_connection()
            self.assertTrue(db_conn.is_usable(), "Database connection is working.")
        except OperationalError as e:
            self.fail(f"Database connection failed: {e}")
