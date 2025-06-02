
"""Tools for /mgmt/v1/monitors/config operations"""

import logging
from typing import Dict, Any, List
from mcp_komodor.api.client import make_api_request

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger("mcp_tools")


async def monitorscontrollerv1_getall() -> Dict[str, Any]:
    '''
    Fetches all monitor configurations from the deprecated API endpoint.

    This function makes an asynchronous GET request to the `/mgmt/v1/monitors/config` endpoint to retrieve monitor configurations. Note that this API is deprecated, and it is recommended to use `/api/v2/realtime-monitors/config` for new implementations.

    Args:

    Returns:
        Dict[str, Any]: The JSON response from the API call containing monitor configurations.

    Raises:
        Exception: If the API request fails or returns an error.

    OpenAPI Specification:
      deprecated: true
      summary: Retrieve all monitor configurations from the deprecated endpoint.
      responses:
        '200':
          description: Successful response containing monitor configurations.
          content:
            application/json:
              schema:
                type: object
                additionalProperties: true
        '400':
          description: Bad request due to invalid parameters.
        '500':
          description: Internal server error.
    '''
    logger.debug("Making GET request to /mgmt/v1/monitors/config")
    params = {}
    data = None
    


    
    data = {}

    if not data:
        data = None
    success, response = await make_api_request(
        "/mgmt/v1/monitors/config",
        method="GET",
        params=params,
        data=data
    )
    if not success:
        logger.error(f"Request failed: {response.get('error')}")
        return {"error": response.get('error', 'Request failed')}
    return response


async def monitorscontrollerv1_post(body_name: str, body_type: str, body_active: bool, body_sensors: List[str], body_isDeleted: bool, body_variables: Dict[str, Any] = None, body_sinks: str = None, body_sinksOptions: Dict[str, Any] = None) -> Dict[str, Any]:
    '''
    Deprecated: Use `/api/v2/realtime-monitors/config` instead.

    Args:
        body_name (str): The name of the monitor.
        body_type (str): The type of the monitor.
        body_active (bool): Indicates if the monitor is active.
        body_sensors (List[str]): List of sensors associated with the monitor.
        body_isDeleted (bool): Indicates if the monitor is marked as deleted.
        body_variables (Dict[str, Any], optional): Variables associated with the monitor. Defaults to None.
        body_sinks (str, optional): Sinks associated with the monitor. Defaults to None.
        body_sinksOptions (Dict[str, Any], optional): Options for the sinks associated with the monitor. Defaults to None.

    Returns:
        Dict[str, Any]: The JSON response from the API call.

    Raises:
        Exception: If the API request fails or returns an error.

    OpenAPI Specification:
        deprecated: true
        description: This API is deprecated. Please use `/api/v2/realtime-monitors/config` API instead for new implementations and better validation and error handling.
        parameters:
          - name: body_name
            in: body
            required: true
            type: string
            description: The name of the monitor.
          - name: body_type
            in: body
            required: true
            type: string
            description: The type of the monitor.
          - name: body_active
            in: body
            required: true
            type: boolean
            description: Indicates if the monitor is active.
          - name: body_sensors
            in: body
            required: true
            type: array
            items:
              type: string
            description: List of sensors associated with the monitor.
          - name: body_isDeleted
            in: body
            required: true
            type: boolean
            description: Indicates if the monitor is marked as deleted.
          - name: body_variables
            in: body
            required: false
            type: object
            description: Variables associated with the monitor.
          - name: body_sinks
            in: body
            required: false
            type: string
            description: Sinks associated with the monitor.
          - name: body_sinksOptions
            in: body
            required: false
            type: object
            description: Options for the sinks associated with the monitor.
        responses:
          200:
            description: Successful response
            schema:
              type: object
          default:
            description: Error response
            schema:
              type: object
    '''
    logger.debug("Making POST request to /mgmt/v1/monitors/config")
    params = {}
    data = None
    

    

    

    

    

    

    

    

    


    
    data = {}

    
    data["name"] = body_name
    

    
    data["type"] = body_type
    

    
    data["active"] = body_active
    

    
    data["sensors"] = body_sensors
    

    
    data["isDeleted"] = body_isDeleted
    

    
    data["variables"] = body_variables
    

    
    data["sinks"] = body_sinks
    

    
    data["sinksOptions"] = body_sinksOptions
    

    if not data:
        data = None
    success, response = await make_api_request(
        "/mgmt/v1/monitors/config",
        method="POST",
        params=params,
        data=data
    )
    if not success:
        logger.error(f"Request failed: {response.get('error')}")
        return {"error": response.get('error', 'Request failed')}
    return response
