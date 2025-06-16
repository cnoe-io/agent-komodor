"""Tools for /api/v2/clusters operations"""

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


async def get_api_v2_clusters(param_clusterName: List[str] = None, param_tags: List[str] = None) -> Dict[str, Any]:
    '''
    Fetch a list of all clusters, optionally filtered by name or tags.

    Args:
        param_clusterName (List[str], optional): List of cluster names to filter by. Defaults to None.
        param_tags (List[str], optional): List of tags to filter by. Defaults to None.

    Returns:
        Dict[str, Any]: The JSON response from the API call containing the list of clusters.

    Raises:
        Exception: If the API request fails or returns an error.
    '''
    logger.debug("Making GET request to /api/v2/clusters")

    params = {}
    data = {}

    if param_clusterName is not None:
        params["clusterName"] = (
            str(param_clusterName).lower() if isinstance(param_clusterName, bool) else param_clusterName
        )

    if param_tags is not None:
        params["tags"] = str(param_tags).lower() if isinstance(param_tags, bool) else param_tags

    flat_body = {}
    data = assemble_nested_body(flat_body)

    success, response = await make_api_request("/api/v2/clusters", method="GET", params=params, data=data)

    if not success:
        logger.error(f"Request failed: {response.get('error')}")
        return {"error": response.get("error", "Request failed")}
    return response