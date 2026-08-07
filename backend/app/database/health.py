from typing import Dict, Any
from .connection import check_database_connection, get_db_connection_info
from .initializer import ensure_db_directory


def verify_database_health() -> Dict[str, Any]:
    """
    Performs comprehensive diagnostic checks on database infrastructure.
    Returns structured health telemetry for system health endpoints.
    """
    is_connected = check_database_connection()
    conn_info = get_db_connection_info()
    db_path = ensure_db_directory()

    return {
        "status": "PASS" if is_connected else "FAIL",
        "details": {
            "connected": is_connected,
            "dialect": conn_info.get("dialect", "unknown"),
            "driver": conn_info.get("driver", "unknown"),
            "storage_path": db_path,
            "is_sqlite": conn_info.get("is_sqlite", True)
        }
    }
