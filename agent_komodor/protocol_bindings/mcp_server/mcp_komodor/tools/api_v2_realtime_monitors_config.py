
"""Tools for /api/v2/realtime-monitors/config operations"""

import logging
from typing import Dict, Any, List
from mcp_komodor.api.client import make_api_request

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger("mcp_tools")


async def get_api_v2_realtime_monitors_config() -> Dict[str, Any]:
    '''
    Fetches the configuration for real-time monitors from the API v2 endpoint.

    Args:
        None

    Returns:
        Dict[str, Any]: The JSON response from the API call containing the configuration details.

    Raises:
        Exception: If the API request fails or returns an error.

    OpenAPI Specification:
        get:
          summary: Retrieve real-time monitors configuration
          operationId: getApiV2RealtimeMonitorsConfig
          responses:
            '200':
              description: Successful response with configuration details
              content:
                application/json:
                  schema:
                    type: object
                    additionalProperties: true
            '400':
              description: Bad request
            '401':
              description: Unauthorized
            '500':
              description: Internal server error
    '''
    logger.debug("Making GET request to /api/v2/realtime-monitors/config")
    params = {}
    data = None
    


    
    data = {}

    if not data:
        data = None
    success, response = await make_api_request(
        "/api/v2/realtime-monitors/config",
        method="GET",
        params=params,
        data=data
    )
    if not success:
        logger.error(f"Request failed: {response.get('error')}")
        return {"error": response.get('error', 'Request failed')}
    return response


async def post_api_v2_realtime_monitors_config(body_sensors: List[str], body_type: str, body_name: str = None, body_sinks: Dict[str, Any] = None, body_active: bool = None, body_variables: Dict[str, Any] = None, body_sinksOptions: Dict[str, Any] = None) -> Dict[str, Any]:
    '''
    Posts a configuration for real-time monitors to the API.

    Args:
        body_sensors (List[str]): A list of sensor identifiers.
        body_type (str): The type of the monitor configuration.
        body_name (str, optional): The name of the monitor configuration. Defaults to None.
        body_sinks (Dict[str, Any], optional): The sinks configuration. Defaults to None.
        body_active (bool, optional): Indicates if the monitor is active. Defaults to None.
        body_variables (Dict[str, Any], optional): Variables associated with the monitor. Defaults to None.
        body_sinksOptions (Dict[str, Any], optional): Options for the sinks. Defaults to None.

    Returns:
        Dict[str, Any]: The JSON response from the API call.

    Raises:
        Exception: If the API request fails or returns an error.

    OpenAPI Specification:
        post:
          summary: Posts a configuration for real-time monitors.
          operationId: postApiV2RealtimeMonitorsConfig
          requestBody:
            content:
              application/json:
                schema:
                  type: object
                  properties:
                    sensors:
                      type: array
                      items:
                        type: string
                    type:
                      type: string
                    name:
                      type: string
                    sinks:
                      type: object
                    active:
                      type: boolean
                    variables:
                      type: object
                    sinksOptions:
                      type: object
          responses:
            '200':
              description: Successful response
              content:
                application/json:
                  schema:
                    type: object
            '400':
              description: Bad request
            '500':
              description: Internal server error
    '''
    logger.debug("Making POST request to /api/v2/realtime-monitors/config")
    params = {}
    data = None
    

    

    

    

    

    

    

    


    
    data = {}

    
    data["sensors"] = body_sensors
    

    
    data["type"] = body_type
    

    
    data["name"] = body_name
    

    
    data["sinks"] = body_sinks
    

    
    data["active"] = body_active
    

    
    data["variables"] = body_variables
    

    
    data["sinksOptions"] = body_sinksOptions
    

    if not data:
        data = None
    success, response = await make_api_request(
        "/api/v2/realtime-monitors/config",
        method="POST",
        params=params,
        data=data
    )
    if not success:
        logger.error(f"Request failed: {response.get('error')}")
        return {"error": response.get('error', 'Request failed')}
    return response
