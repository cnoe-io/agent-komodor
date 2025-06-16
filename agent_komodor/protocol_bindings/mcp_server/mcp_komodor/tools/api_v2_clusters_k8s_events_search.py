"""Tools for /api/v2/clusters/k8s-events/search operations"""

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


async def post_api_v2_clusters_k8s_events_search(body: str) -> Dict[str, Any]:
    '''
    Search for Kubernetes events within a cluster scope.

    This function performs a search for Kubernetes events based on the provided criteria. The maximum time range for the search is 2 days. If no time range is specified, the default is the last 24 hours. The maximum time back for the search is 7 days.

    Args:
        body (str): The request body containing search criteria for Kubernetes events.

    Returns:
        Dict[str, Any]: A dictionary containing the JSON response from the API call.

    Raises:
        Exception: If the API request fails or returns an error.
    '''
    logger.debug("Making POST request to /api/v2/clusters/k8s-events/search")

    params = {}
    data = {}

    flat_body = {}
    data = assemble_nested_body(flat_body)

    success, response = await make_api_request(
        "/api/v2/clusters/k8s-events/search", method="POST", params=params, data=data
    )

    if not success:
        logger.error(f"Request failed: {response.get('error')}")
        return {"error": response.get("error", "Request failed")}
    return response