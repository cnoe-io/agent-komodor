"""Tools for /api/v2/realtime-monitors/config operations"""

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


async def get_api_v2_realtime_monitors_config() -> Dict[str, Any]:
    '''
    Fetches the configuration for real-time monitors from the API v2 endpoint.

    This asynchronous function makes a GET request to the /api/v2/realtime-monitors/config
    endpoint to retrieve the configuration settings for real-time monitors.

    Args:
        None

    Returns:
        Dict[str, Any]: The JSON response from the API call containing the configuration
        details for real-time monitors. If the request fails, a dictionary with an "error"
        key is returned.

    Raises:
        Exception: If the API request fails or returns an error, an exception is raised
        with the error details.
    '''
    logger.debug("Making GET request to /api/v2/realtime-monitors/config")

    params = {}
    data = {}

    flat_body = {}
    data = assemble_nested_body(flat_body)

    success, response = await make_api_request(
        "/api/v2/realtime-monitors/config", method="GET", params=params, data=data
    )

    if not success:
        logger.error(f"Request failed: {response.get('error')}")
        return {"error": response.get("error", "Request failed")}
    return response


async def post_api_v2_realtime_monitors_config(
    body_sensors: List[str],
    body_type: str,
    body_name: str = None,
    body_sinks: Dict[str, Any] = None,
    body_active: bool = None,
    body_variables: Dict[str, Any] = None,
    body_sinksOptions_notifyOn: List[str] = None,
) -> Dict[str, Any]:
    '''
    Posts a configuration for real-time monitors to the API.

    Args:
        body_sensors (List[str]): A list of sensor identifiers to be included in the configuration.
        body_type (str): The type of the monitor configuration.
        body_name (str, optional): The name of the monitor configuration. Defaults to None.
        body_sinks (Dict[str, Any], optional): A dictionary defining the sinks for the monitor configuration. Defaults to None.
        body_active (bool, optional): A flag indicating whether the monitor configuration is active. Defaults to None.
        body_variables (Dict[str, Any], optional): A dictionary of variables for the monitor configuration. Defaults to None.
        body_sinksOptions_notifyOn (List[str], optional): A list of conditions for notification options on sinks. Defaults to None.

    Returns:
        Dict[str, Any]: The JSON response from the API call.

    Raises:
        Exception: If the API request fails or returns an error.
    '''
    logger.debug("Making POST request to /api/v2/realtime-monitors/config")

    params = {}
    data = {}

    flat_body = {}
    if body_sensors is not None:
        flat_body["sensors"] = body_sensors
    if body_type is not None:
        flat_body["type"] = body_type
    if body_name is not None:
        flat_body["name"] = body_name
    if body_sinks is not None:
        flat_body["sinks"] = body_sinks
    if body_active is not None:
        flat_body["active"] = body_active
    if body_variables is not None:
        flat_body["variables"] = body_variables
    if body_sinksOptions_notifyOn is not None:
        flat_body["sinksOptions_notifyOn"] = body_sinksOptions_notifyOn
    data = assemble_nested_body(flat_body)

    success, response = await make_api_request(
        "/api/v2/realtime-monitors/config", method="POST", params=params, data=data
    )

    if not success:
        logger.error(f"Request failed: {response.get('error')}")
        return {"error": response.get("error", "Request failed")}
    return response