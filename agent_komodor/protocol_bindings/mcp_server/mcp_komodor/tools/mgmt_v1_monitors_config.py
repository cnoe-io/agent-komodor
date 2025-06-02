
"""Tools for /mgmt/v1/monitors/config operations"""

import logging
from typing import Dict, Any, List
from mcp_komodor.api.client import make_api_request

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger("mcp_tools")


async def monitorscontrollerv1_getall() -> Dict[str, Any]:
    '''
    Fetches all monitor configurations.

    This function is deprecated. Please use `/api/v2/realtime-monitors/config` for new implementations and better validation and error handling.

    Returns:
        Dict[str, Any]: The JSON response from the API call.

    Raises:
        Exception: If the API request fails or returns an error.

    OpenAPI Specification:
      deprecated: true
      summary: Fetch all monitor configurations
      description: |
        This API is deprecated. Please use `/api/v2/realtime-monitors/config` API instead for new implementations and better validation and error handling.
      responses:
        '200':
          description: Successful response with monitor configurations
          content:
            application/json:
              schema:
                type: object
                additionalProperties: true
        '4XX':
          description: Client error
        '5XX':
          description: Server error
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

    This function makes a POST request to the deprecated `/mgmt/v1/monitors/config` endpoint. It is recommended to use the `/api/v2/realtime-monitors/config` endpoint for new implementations, which offers better validation and error handling.

    Args:
        body_name (str): The name of the monitor.
        body_type (str): The type of the monitor.
        body_active (bool): Indicates if the monitor is active.
        body_sensors (List[str]): A list of sensors associated with the monitor.
        body_isDeleted (bool): Indicates if the monitor is marked as deleted.
        body_variables (Dict[str, Any], optional): Additional variables for the monitor. Defaults to None.
        body_sinks (str, optional): The sinks associated with the monitor. Defaults to None.
        body_sinksOptions (Dict[str, Any], optional): Options for the sinks. Defaults to None.

    Returns:
        Dict[str, Any]: The JSON response from the API call.

    Raises:
        Exception: If the API request fails or returns an error.

    OpenAPI Specification:
        deprecated: true
        summary: "Create or update a monitor configuration."
        description: "This API is deprecated. Please use `/api/v2/realtime-monitors/config` API instead for new implementations and better validation and error handling."
        requestBody:
            required: true
            content:
                application/json:
                    schema:
                        type: object
                        properties:
                            name:
                                type: string
                            type:
                                type: string
                            active:
                                type: boolean
                            sensors:
                                type: array
                                items:
                                    type: string
                            isDeleted:
                                type: boolean
                            variables:
                                type: object
                                additionalProperties: true
                            sinks:
                                type: string
                            sinksOptions:
                                type: object
                                additionalProperties: true
        responses:
            '200':
                description: "Successful response"
                content:
                    application/json:
                        schema:
                            type: object
                            additionalProperties: true
            '400':
                description: "Bad request"
            '500':
                description: "Internal server error"
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
