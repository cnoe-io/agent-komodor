"""Tools for /api/v2/users/effective-permissions operations"""

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
        ValueError: If the input dictionary contains keys that cannot be split into valid parts.
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


async def get_api_v2_users_effective_permissions(param_id: str = None, param_email: str = None) -> Dict[str, Any]:
    '''
    Get User's Effective Permissions.

    This function retrieves a user's effective permissions using either their user ID or email address.

    Args:
        param_id (str, optional): The user ID to query. Defaults to None.
        param_email (str, optional): The email address to query. Defaults to None.

    Returns:
        Dict[str, Any]: The JSON response from the API call containing the user's effective permissions.

    Raises:
        Exception: If the API request fails or returns an error.
    '''
    logger.debug("Making GET request to /api/v2/users/effective-permissions")

    params = {}
    data = {}

    if param_id is not None:
        params["id"] = str(param_id).lower() if isinstance(param_id, bool) else param_id

    if param_email is not None:
        params["email"] = str(param_email).lower() if isinstance(param_email, bool) else param_email

    flat_body = {}
    data = assemble_nested_body(flat_body)

    success, response = await make_api_request(
        "/api/v2/users/effective-permissions", method="GET", params=params, data=data
    )

    if not success:
        logger.error(f"Request failed: {response.get('error')}")
        return {"error": response.get("error", "Request failed")}
    return response