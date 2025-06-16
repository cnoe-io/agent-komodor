"""Tools for /api/v2/rbac/roles/{id_or_name} operations"""

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


async def get_api_v2_rbac_roles_id_or_name(path_id_or_name: str) -> Dict[str, Any]:
    '''
    Get Role by ID or Name.

    Args:
        path_id_or_name (str): The role ID or name to retrieve.

    Returns:
        Dict[str, Any]: The JSON response from the API call containing role details.

    Raises:
        Exception: If the API request fails or returns an error.
    '''
    logger.debug("Making GET request to /api/v2/rbac/roles/{id_or_name}")

    params = {}
    data = {}

    flat_body = {}
    data = assemble_nested_body(flat_body)

    success, response = await make_api_request(
        f"/api/v2/rbac/roles/{path_id_or_name}", method="GET", params=params, data=data
    )

    if not success:
        logger.error(f"Request failed: {response.get('error')}")
        return {"error": response.get("error", "Request failed")}
    return response


async def put_api_v2_rbac_roles_id_or_name(
    path_id_or_name: str,
    body_name: str = None,
    body_isDefault: bool = None,
    body_policyIds: List[str] = None,
    body_policyNames: List[str] = None,
) -> Dict[str, Any]:
    '''
    Update a role by its ID or name.

    Args:
        path_id_or_name (str): The ID or name of the role to update.
        body_name (str, optional): The new name for the role. Defaults to None.
        body_isDefault (bool, optional): Indicates if the role is default. Defaults to None.
        body_policyIds (List[str], optional): List of policy IDs associated with the role. Defaults to None.
        body_policyNames (List[str], optional): List of policy names associated with the role. Defaults to None.

    Returns:
        Dict[str, Any]: The JSON response from the API call, containing the updated role information.

    Raises:
        Exception: If the API request fails or returns an error.
    '''
    logger.debug("Making PUT request to /api/v2/rbac/roles/{id_or_name}")

    params = {}
    data = {}

    flat_body = {}
    if body_name is not None:
        flat_body["name"] = body_name
    if body_isDefault is not None:
        flat_body["isDefault"] = body_isDefault
    if body_policyIds is not None:
        flat_body["policyIds"] = body_policyIds
    if body_policyNames is not None:
        flat_body["policyNames"] = body_policyNames
    data = assemble_nested_body(flat_body)

    success, response = await make_api_request(
        f"/api/v2/rbac/roles/{path_id_or_name}", method="PUT", params=params, data=data
    )

    if not success:
        logger.error(f"Request failed: {response.get('error')}")
        return {"error": response.get("error", "Request failed")}
    return response


async def delete_api_v2_rbac_roles_id_or_name(path_id_or_name: str) -> Dict[str, Any]:
    '''
    Delete a role by its ID or name.

    This function sends an asynchronous DELETE request to the API to remove a role specified by its ID or name.

    Args:
        path_id_or_name (str): The ID or name of the role to be deleted.

    Returns:
        Dict[str, Any]: The JSON response from the API call, which includes the result of the deletion operation.

    Raises:
        Exception: If the API request fails or returns an error, an exception is raised with the error details.
    '''
    logger.debug("Making DELETE request to /api/v2/rbac/roles/{id_or_name}")

    params = {}
    data = {}

    flat_body = {}
    data = assemble_nested_body(flat_body)

    success, response = await make_api_request(
        f"/api/v2/rbac/roles/{path_id_or_name}", method="DELETE", params=params, data=data
    )

    if not success:
        logger.error(f"Request failed: {response.get('error')}")
        return {"error": response.get("error", "Request failed")}
    return response