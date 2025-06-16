"""Tools for /api/v2/audit-log/filters operations"""

import logging
from typing import Dict, Any
from mcp_komodor.api.client import make_api_request


def assemble_nested_body(flat_body: Dict[str, Any]) -> Dict[str, Any]:
    '''
    Convert a flat dictionary with underscore-separated keys into a nested dictionary.

    Args:
        flat_body (Dict[str, Any]): A dictionary where keys are underscore-separated strings representing nested paths.

    Returns:
        Dict[str, Any]: A nested dictionary constructed from the flat dictionary.

    Raises:
        ValueError: If the input dictionary contains invalid keys that cannot be split into parts.
    '''
    nested = {}
    for key, value in flat_body.items():
        parts = key.split("_")
        d = nested
        for part in parts[:-1]:
            d = d.setdefault(part, {})
        d[parts[-1]] = value
    return nested


# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger("mcp_tools")


async def get_api_v2_audit_log_filters(param_startTime: str = None, param_endTime: str = None) -> Dict[str, Any]:
    '''
    Get available filter values for Query Audit Logs.

    Args:
        param_startTime (str, optional): Start time of the audit logs filters. If not provided, the default is 8 hours ago.
        param_endTime (str, optional): End time of the audit logs filters. If not provided, the default is now.

    Returns:
        Dict[str, Any]: The JSON response from the API call containing available filter values.

    Raises:
        Exception: If the API request fails or returns an error.
    '''
    logger.debug("Making GET request to /api/v2/audit-log/filters")

    params = {}
    data = {}

    if param_startTime is not None:
        params["startTime"] = str(param_startTime).lower() if isinstance(param_startTime, bool) else param_startTime

    if param_endTime is not None:
        params["endTime"] = str(param_endTime).lower() if isinstance(param_endTime, bool) else param_endTime

    flat_body = {}
    data = assemble_nested_body(flat_body)

    success, response = await make_api_request("/api/v2/audit-log/filters", method="GET", params=params, data=data)

    if not success:
        logger.error(f"Request failed: {response.get('error')}")
        return {"error": response.get("error", "Request failed")}
    return response