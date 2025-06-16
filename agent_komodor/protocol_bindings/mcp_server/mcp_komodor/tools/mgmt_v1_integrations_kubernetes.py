"""Tools for /mgmt/v1/integrations/kubernetes operations"""

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


async def cluster_controller_post(body_clusterName: str) -> Dict[str, Any]:
    '''
    Sends a POST request to the Kubernetes integration endpoint to manage cluster configurations.

    Args:
        body_clusterName (str): The name of the cluster to be managed.

    Returns:
        Dict[str, Any]: The JSON response from the API call, containing the result of the operation.

    Raises:
        Exception: If the API request fails or returns an error, an exception is raised with the error details.
    '''
    logger.debug("Making POST request to /mgmt/v1/integrations/kubernetes")

    params = {}
    data = {}

    flat_body = {}
    if body_clusterName is not None:
        flat_body["clusterName"] = body_clusterName
    data = assemble_nested_body(flat_body)

    success, response = await make_api_request(
        "/mgmt/v1/integrations/kubernetes", method="POST", params=params, data=data
    )

    if not success:
        logger.error(f"Request failed: {response.get('error')}")
        return {"error": response.get("error", "Request failed")}
    return response