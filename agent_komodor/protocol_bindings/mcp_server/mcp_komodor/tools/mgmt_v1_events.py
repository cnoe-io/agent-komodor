"""Tools for /mgmt/v1/events operations"""

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


async def events_controller_create_custom_event(
    body_eventType: str,
    body_summary: str,
    body_scope_clusters: List[str] = None,
    body_scope_servicesNames: List[str] = None,
    body_scope_namespaces: List[str] = None,
    body_severity: str = None,
    body_details: Dict[str, Any] = None,
) -> Dict[str, Any]:
    '''
    Creates a custom event in the events controller.

    Args:
        body_eventType (str): The type of event you'd like to create, limited to 30 characters.
        body_summary (str): Description of the event.
        body_scope_clusters (List[str], optional): List of cluster identifiers. Defaults to None.
        body_scope_servicesNames (List[str], optional): List of service names. Defaults to None.
        body_scope_namespaces (List[str], optional): List of namespaces. Defaults to None.
        body_severity (str, optional): Severity level of the event. Defaults to 'information'.
        body_details (Dict[str, Any], optional): Additional key-value pairs for extra event details. Defaults to None.

    Returns:
        Dict[str, Any]: The JSON response from the API call.

    Raises:
        Exception: If the API request fails or returns an error.
    '''
    logger.debug("Making POST request to /mgmt/v1/events")

    params = {}
    data = {}

    flat_body = {}
    if body_eventType is not None:
        flat_body["eventType"] = body_eventType
    if body_summary is not None:
        flat_body["summary"] = body_summary
    if body_scope_clusters is not None:
        flat_body["scope_clusters"] = body_scope_clusters
    if body_scope_servicesNames is not None:
        flat_body["scope_servicesNames"] = body_scope_servicesNames
    if body_scope_namespaces is not None:
        flat_body["scope_namespaces"] = body_scope_namespaces
    if body_severity is not None:
        flat_body["severity"] = body_severity
    if body_details is not None:
        flat_body["details"] = body_details
    data = assemble_nested_body(flat_body)

    success, response = await make_api_request("/mgmt/v1/events", method="POST", params=params, data=data)

    if not success:
        logger.error(f"Request failed: {response.get('error')}")
        return {"error": response.get("error", "Request failed")}
    return response