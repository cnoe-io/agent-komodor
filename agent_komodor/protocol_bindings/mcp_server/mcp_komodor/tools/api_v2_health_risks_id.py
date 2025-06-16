"""Tools for /api/v2/health/risks/{id} operations"""

import logging
from typing import Dict, Any
from mcp_komodor.api.client import make_api_request


def assemble_nested_body(flat_body: Dict[str, Any]) -> Dict[str, Any]:
    '''
    Convert a flat dictionary with underscore-separated keys into a nested dictionary.

    Args:
        flat_body (Dict[str, Any]): A dictionary where keys are underscore-separated strings representing nested structure.

    Returns:
        Dict[str, Any]: A nested dictionary constructed from the flat dictionary.

    Raises:
        ValueError: If the input dictionary contains keys that cannot be split into parts.
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


async def get_health_risk_data(path_id: str) -> Dict[str, Any]:
    '''
    Get health risk data.

    Args:
        path_id (str): The identifier for the health risk data path.

    Returns:
        Dict[str, Any]: The JSON response from the API call containing health risk data.

    Raises:
        Exception: If the API request fails or returns an error.
    '''
    logger.debug("Making GET request to /api/v2/health/risks/{id}")

    params = {}
    data = {}

    flat_body = {}
    data = assemble_nested_body(flat_body)

    success, response = await make_api_request(
        f"/api/v2/health/risks/{path_id}", method="GET", params=params, data=data
    )

    if not success:
        logger.error(f"Request failed: {response.get('error')}")
        return {"error": response.get("error", "Request failed")}
    return response


async def update_health_risk_status(path_id: str, body_status: str = None) -> Dict[str, Any]:
    '''
    Update the status of a health risk.

    Args:
        path_id (str): The identifier for the health risk path.
        body_status (str, optional): The status to update for the health risk. Defaults to None.

    Returns:
        Dict[str, Any]: The JSON response from the API call, containing the updated health risk status.

    Raises:
        Exception: If the API request fails or returns an error.
    '''
    logger.debug("Making PUT request to /api/v2/health/risks/{id}")

    params = {}
    data = {}

    flat_body = {}
    if body_status is not None:
        flat_body["status"] = body_status
    data = assemble_nested_body(flat_body)

    success, response = await make_api_request(
        f"/api/v2/health/risks/{path_id}", method="PUT", params=params, data=data
    )

    if not success:
        logger.error(f"Request failed: {response.get('error')}")
        return {"error": response.get("error", "Request failed")}
    return response