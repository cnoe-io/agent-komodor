"""Tools for /api/v2/rbac/policies/{id_or_name} operations"""

import logging
from typing import Dict, Any, List
from mcp_komodor.api.client import make_api_request


def assemble_nested_body(flat_body: Dict[str, Any]) -> Dict[str, Any]:
    '''
    Convert a flat dictionary with underscore-separated keys into a nested dictionary.

    Args:
        flat_body (Dict[str, Any]): A dictionary where keys are underscore-separated strings representing nested paths.

    Returns:
        Dict[str, Any]: A nested dictionary constructed from the flat dictionary, where each underscore in the keys represents a level of nesting.

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


async def get_api_v2_rbac_policies_id_or_name(path_id_or_name: str) -> Dict[str, Any]:
    '''
    Get Policy by ID or Name.

    Args:
        path_id_or_name (str): The policy ID or name to retrieve.

    Returns:
        Dict[str, Any]: The JSON response from the API call containing the policy details.

    Raises:
        Exception: If the API request fails or returns an error.
    '''
    logger.debug("Making GET request to /api/v2/rbac/policies/{id_or_name}")

    params = {}
    data = {}

    flat_body = {}
    data = assemble_nested_body(flat_body)

    success, response = await make_api_request(
        f"/api/v2/rbac/policies/{path_id_or_name}", method="GET", params=params, data=data
    )

    if not success:
        logger.error(f"Request failed: {response.get('error')}")
        return {"error": response.get("error", "Request failed")}
    return response


async def put_api_v2_rbac_policies_id_or_name(
    path_id_or_name: str, body_name: str = None, body_statements: List[str] = None
) -> Dict[str, Any]:
    '''
    Update Policy by Id or Name.

    This function makes an asynchronous PUT request to update a policy identified by its ID or name.
    It sends the updated policy name and statements as part of the request body.

    Args:
        path_id_or_name (str): The ID or name of the policy to be updated.
        body_name (str, optional): The new name for the policy. Defaults to None.
        body_statements (List[str], optional): A list of statements to update the policy with. Defaults to None.

    Returns:
        Dict[str, Any]: The JSON response from the API call, which includes the updated policy details or an error message.

    Raises:
        Exception: If the API request fails or returns an error, an exception is raised with the error details.
    '''
    logger.debug("Making PUT request to /api/v2/rbac/policies/{id_or_name}")

    params = {}
    data = {}

    flat_body = {}
    if body_name is not None:
        flat_body["name"] = body_name
    if body_statements is not None:
        flat_body["statements"] = body_statements
    data = assemble_nested_body(flat_body)

    success, response = await make_api_request(
        f"/api/v2/rbac/policies/{path_id_or_name}", method="PUT", params=params, data=data
    )

    if not success:
        logger.error(f"Request failed: {response.get('error')}")
        return {"error": response.get("error", "Request failed")}
    return response


async def delete_api_v2_rbac_policies_id_or_name(path_id_or_name: str) -> Dict[str, Any]:
    '''
    Delete a policy by its ID or name.

    Args:
        path_id_or_name (str): The ID or name of the policy to be deleted.

    Returns:
        Dict[str, Any]: The JSON response from the API call, containing the result of the delete operation.

    Raises:
        Exception: If the API request fails or returns an error.
    '''
    logger.debug("Making DELETE request to /api/v2/rbac/policies/{id_or_name}")

    params = {}
    data = {}

    flat_body = {}
    data = assemble_nested_body(flat_body)

    success, response = await make_api_request(
        f"/api/v2/rbac/policies/{path_id_or_name}", method="DELETE", params=params, data=data
    )

    if not success:
        logger.error(f"Request failed: {response.get('error')}")
        return {"error": response.get("error", "Request failed")}
    return response