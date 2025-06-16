"""Tools for /api/v2/service/yaml operations"""

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


async def get_api_v2_service_yaml(
    param_cluster: str, param_namespace: str, param_kind: str, param_name: str
) -> Dict[str, Any]:
    '''
    Get the YAML for a service.

    Args:
        param_cluster (str): The cluster identifier.
        param_namespace (str): The namespace of the service.
        param_kind (str): The kind of the service.
        param_name (str): The service name.

    Returns:
        Dict[str, Any]: The JSON response from the API call.

    Raises:
        Exception: If the API request fails or returns an error.
    '''
    logger.debug("Making GET request to /api/v2/service/yaml")

    params = {}
    data = {}

    if param_cluster is not None:
        params["cluster"] = str(param_cluster).lower() if isinstance(param_cluster, bool) else param_cluster

    if param_namespace is not None:
        params["namespace"] = str(param_namespace).lower() if isinstance(param_namespace, bool) else param_namespace

    if param_kind is not None:
        params["kind"] = str(param_kind).lower() if isinstance(param_kind, bool) else param_kind

    if param_name is not None:
        params["name"] = str(param_name).lower() if isinstance(param_name, bool) else param_name

    flat_body = {}
    data = assemble_nested_body(flat_body)

    success, response = await make_api_request("/api/v2/service/yaml", method="GET", params=params, data=data)

    if not success:
        logger.error(f"Request failed: {response.get('error')}")
        return {"error": response.get("error", "Request failed")}
    return response