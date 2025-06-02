
"""Tools for /api/v2/realtime-monitors/config/{id} operations"""

import logging
from typing import Dict, Any, List
from mcp_komodor.api.client import make_api_request

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger("mcp_tools")


async def get_api_v2_realtime_monitors_config_id(path_id: str) -> Dict[str, Any]:
    '''
    Fetches the configuration for a specific realtime monitor by its ID.

    Args:
        path_id (str): The ID of the realtime monitor configuration to retrieve.

    Returns:
        Dict[str, Any]: The JSON response containing the configuration details.

    Raises:
        Exception: If the API request fails or returns an error.

    OpenAPI Specification:
        get:
          summary: Retrieve realtime monitor configuration by ID
          operationId: getApiV2RealtimeMonitorsConfigId
          parameters:
            - name: path_id
              in: path
              required: true
              description: The ID of the realtime monitor configuration
              schema:
                type: string
          responses:
            '200':
              description: Successful response with configuration details
              content:
                application/json:
                  schema:
                    type: object
                    additionalProperties: true
            '404':
              description: Configuration not found
            '500':
              description: Internal server error
    '''
    logger.debug("Making GET request to /api/v2/realtime-monitors/config/{id}")
    params = {}
    data = None
    

    


    
    data = {}

    

    if not data:
        data = None
    success, response = await make_api_request(
        f"/api/v2/realtime-monitors/config/{path_id}",
        method="GET",
        params=params,
        data=data
    )
    if not success:
        logger.error(f"Request failed: {response.get('error')}")
        return {"error": response.get('error', 'Request failed')}
    return response


async def put_api_v2_realtime_monitors_config_id(path_id: str, body_sensors: List[str], body_type: str, body_name: str = None, body_sinks: Dict[str, Any] = None, body_active: bool = None, body_variables: Dict[str, Any] = None, body_sinksOptions: Dict[str, Any] = None) -> Dict[str, Any]:
    '''
    Updates the configuration of a real-time monitor by its ID.

    Args:
        path_id (str): The ID of the monitor configuration to update.
        body_sensors (List[str]): List of sensor identifiers to be included in the monitor.
        body_type (str): The type of the monitor configuration.
        body_name (str, optional): The name of the monitor configuration. Defaults to None.
        body_sinks (Dict[str, Any], optional): Configuration for data sinks. Defaults to None.
        body_active (bool, optional): Indicates if the monitor is active. Defaults to None.
        body_variables (Dict[str, Any], optional): Variables associated with the monitor. Defaults to None.
        body_sinksOptions (Dict[str, Any], optional): Options for the data sinks. Defaults to None.

    Returns:
        Dict[str, Any]: The JSON response from the API call.

    Raises:
        Exception: If the API request fails or returns an error.

    OpenAPI Specification:
        put:
          summary: Updates the configuration of a real-time monitor by its ID.
          operationId: putApiV2RealtimeMonitorsConfigId
          parameters:
            - name: path_id
              in: path
              required: true
              schema:
                type: string
          requestBody:
            required: true
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
    '''
    logger.debug("Making PUT request to /api/v2/realtime-monitors/config/{id}")
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
        f"/api/v2/realtime-monitors/config/{path_id}",
        method="PUT",
        params=params,
        data=data
    )
    if not success:
        logger.error(f"Request failed: {response.get('error')}")
        return {"error": response.get('error', 'Request failed')}
    return response


async def delete_api_v2_realtime_monitors_config_id(path_id: str) -> Dict[str, Any]:
    '''
    Deletes a real-time monitor configuration by its ID.

    Args:
        path_id (str): The ID of the real-time monitor configuration to delete.

    Returns:
        Dict[str, Any]: The JSON response from the API call, which includes the status of the deletion.

    Raises:
        Exception: If the API request fails or returns an error.

    OpenAPI Specification:
        delete:
          summary: Deletes a real-time monitor configuration by ID.
          operationId: deleteApiV2RealtimeMonitorsConfigId
          parameters:
            - name: path_id
              in: path
              required: true
              description: The ID of the real-time monitor configuration.
              schema:
                type: string
          responses:
            '200':
              description: Successful deletion of the configuration.
              content:
                application/json:
                  schema:
                    type: object
                    properties:
                      status:
                        type: string
                        example: "success"
            '404':
              description: Configuration not found.
              content:
                application/json:
                  schema:
                    type: object
                    properties:
                      error:
                        type: string
                        example: "Configuration not found"
            '500':
              description: Internal server error.
              content:
                application/json:
                  schema:
                    type: object
                    properties:
                      error:
                        type: string
                        example: "Internal server error"
    '''
    logger.debug("Making DELETE request to /api/v2/realtime-monitors/config/{id}")
    params = {}
    data = None
    

    


    
    data = {}

    

    if not data:
        data = None
    success, response = await make_api_request(
        f"/api/v2/realtime-monitors/config/{path_id}",
        method="DELETE",
        params=params,
        data=data
    )
    if not success:
        logger.error(f"Request failed: {response.get('error')}")
        return {"error": response.get('error', 'Request failed')}
    return response
