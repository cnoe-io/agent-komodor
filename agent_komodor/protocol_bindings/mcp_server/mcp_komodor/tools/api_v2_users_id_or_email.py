"""Tools for /api/v2/users/{id_or_email} operations"""

import logging
from typing import Dict, Any, List
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


async def get_api_v2_users_id_or_email(path_id_or_email: str) -> Dict[str, Any]:
    '''
    Get a User by id or email.

    Args:
        path_id_or_email (str): The user ID or email address to retrieve the user information.

    Returns:
        Dict[str, Any]: The JSON response from the API call containing user details.

    Raises:
        Exception: If the API request fails or returns an error.
    '''
    logger.debug("Making GET request to /api/v2/users/{id_or_email}")

    params = {}
    data = {}

    flat_body = {}
    data = assemble_nested_body(flat_body)

    success, response = await make_api_request(
        f"/api/v2/users/{path_id_or_email}", method="GET", params=params, data=data
    )

    if not success:
        logger.error(f"Request failed: {response.get('error')}")
        return {"error": response.get("error", "Request failed")}
    return response


async def put_api_v2_users_id_or_email(
    path_id_or_email: str,
    body_displayName: str = None,
    body_roleIds: List[str] = None,
    body_roleNames: List[str] = None,
) -> Dict[str, Any]:
    '''
    Update a User by id or email.

    Args:
        path_id_or_email (str): The user ID or email to identify the user to be updated.
        body_displayName (str, optional): The display name to update for the user. Defaults to None.
        body_roleIds (List[str], optional): A list of role IDs to assign to the user. Defaults to None.
        body_roleNames (List[str], optional): A list of role names to assign to the user. Defaults to None.

    Returns:
        Dict[str, Any]: The JSON response from the API call, containing the updated user information.

    Raises:
        Exception: If the API request fails or returns an error.
    '''
    logger.debug("Making PUT request to /api/v2/users/{id_or_email}")

    params = {}
    data = {}

    flat_body = {}
    if body_displayName is not None:
        flat_body["displayName"] = body_displayName
    if body_roleIds is not None:
        flat_body["roleIds"] = body_roleIds
    if body_roleNames is not None:
        flat_body["roleNames"] = body_roleNames
    data = assemble_nested_body(flat_body)

    success, response = await make_api_request(
        f"/api/v2/users/{path_id_or_email}", method="PUT", params=params, data=data
    )

    if not success:
        logger.error(f"Request failed: {response.get('error')}")
        return {"error": response.get("error", "Request failed")}
    return response


async def delete_api_v2_users_id_or_email(path_id_or_email: str) -> Dict[str, Any]:
    '''
    Delete a User by id or email.

    Args:
        path_id_or_email (str): The user ID or email address to identify the user to be deleted.

    Returns:
        Dict[str, Any]: The JSON response from the API call, containing the result of the delete operation.

    Raises:
        Exception: If the API request fails or returns an error, an exception is raised with the error details.
    '''
    logger.debug("Making DELETE request to /api/v2/users/{id_or_email}")

    params = {}
    data = {}

    flat_body = {}
    data = assemble_nested_body(flat_body)

    success, response = await make_api_request(
        f"/api/v2/users/{path_id_or_email}", method="DELETE", params=params, data=data
    )

    if not success:
        logger.error(f"Request failed: {response.get('error')}")
        return {"error": response.get("error", "Request failed")}
    return response