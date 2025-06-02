
"""Tools for /mgmt/v1/monitors/config/{id} operations"""

import logging
from typing import Dict, Any, List
from mcp_komodor.api.client import make_api_request

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger("mcp_tools")


async def monitorscontrollerv1_get(path_id: str) -> Dict[str, Any]:
    '''
    Deprecated: Use `/api/v2/realtime-monitors/config` instead.

    Args:
        path_id (str): The identifier for the monitor configuration.

    Returns:
        Dict[str, Any]: The JSON response from the API call.

    Raises:
        Exception: If the API request fails or returns an error.

    OpenAPI Specification:
      get:
        summary: Retrieve monitor configuration by ID
        description: |
          This API is deprecated. Please use `/api/v2/realtime-monitors/config` API instead for new implementations and better validation and error handling.
        parameters:
          - name: path_id
            in: path
            required: true
            description: The identifier for the monitor configuration.
            schema:
              type: string
        responses:
          '200':
            description: Successful response with monitor configuration details.
            content:
              application/json:
                schema:
                  type: object
                  additionalProperties: true
          '4XX':
            description: Client error response.
            content:
              application/json:
                schema:
                  type: object
                  properties:
                    error:
                      type: string
          '5XX':
            description: Server error response.
            content:
              application/json:
                schema:
                  type: object
                  properties:
                    error:
                      type: string
    '''
    logger.debug("Making GET request to /mgmt/v1/monitors/config/{id}")
    params = {}
    data = None
    

    


    
    data = {}

    

    if not data:
        data = None
    success, response = await make_api_request(
        "/mgmt/v1/monitors/config/{path_id}",
        method="GET",
        params=params,
        data=data
    )
    if not success:
        logger.error(f"Request failed: {response.get('error')}")
        return {"error": response.get('error', 'Request failed')}
    return response


async def monitorscontrollerv1_put(path_id: str, body_name: str, body_type: str, body_active: bool, body_sensors: List[str], body_isDeleted: bool, body_variables: Dict[str, Any] = None, body_sinks: str = None, body_sinksOptions: Dict[str, Any] = None) -> Dict[str, Any]:
    '''
    Deprecated: Use `/api/v2/realtime-monitors/config` instead.

    Args:
        path_id (str): The identifier for the monitor configuration path.
        body_name (str): The name of the monitor.
        body_type (str): The type of the monitor.
        body_active (bool): Indicates if the monitor is active.
        body_sensors (List[str]): List of sensors associated with the monitor.
        body_isDeleted (bool): Flag indicating if the monitor is marked as deleted.
        body_variables (Dict[str, Any], optional): Variables associated with the monitor. Defaults to None.
        body_sinks (str, optional): Sinks associated with the monitor. Defaults to None.
        body_sinksOptions (Dict[str, Any], optional): Options for the sinks associated with the monitor. Defaults to None.

    Returns:
        Dict[str, Any]: The JSON response from the API call.

    Raises:
        Exception: If the API request fails or returns an error.

    OpenAPI Specification:
        paths:
          /mgmt/v1/monitors/config/{path_id}:
            put:
              summary: Update monitor configuration
              deprecated: true
              parameters:
                - name: path_id
                  in: path
                  required: true
                  schema:
                    type: string
              requestBody:
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
                  description: Successful response
                  content:
                    application/json:
                      schema:
                        type: object
                        additionalProperties: true
                '400':
                  description: Bad request
                '404':
                  description: Not found
                '500':
                  description: Internal server error
    '''
    logger.debug("Making PUT request to /mgmt/v1/monitors/config/{id}")
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
        "/mgmt/v1/monitors/config/{path_id}",
        method="PUT",
        params=params,
        data=data
    )
    if not success:
        logger.error(f"Request failed: {response.get('error')}")
        return {"error": response.get('error', 'Request failed')}
    return response


async def monitorscontrollerv1_delete(path_id: str) -> Dict[str, Any]:
    '''
    Deletes a monitor configuration by its path ID.

    This function is deprecated. Please use `/api/v2/realtime-monitors/config` API instead for new implementations and better validation and error handling.

    Args:
        path_id (str): The unique identifier for the monitor configuration to be deleted.

    Returns:
        Dict[str, Any]: The JSON response from the API call, which may include an error message if the request fails.

    Raises:
        Exception: If the API request fails or returns an error.

    OpenAPI Specification:
      delete:
        summary: Delete a monitor configuration
        description: This API is deprecated. Use `/api/v2/realtime-monitors/config` instead.
        parameters:
          - name: path_id
            in: path
            required: true
            description: The unique identifier for the monitor configuration
            schema:
              type: string
        responses:
          '200':
            description: Successful deletion of the monitor configuration
            content:
              application/json:
                schema:
                  type: object
                  additionalProperties: true
          '400':
            description: Bad request due to invalid path_id
          '404':
            description: Monitor configuration not found
          '500':
            description: Internal server error
    '''
    logger.debug("Making DELETE request to /mgmt/v1/monitors/config/{id}")
    params = {}
    data = None
    

    


    
    data = {}

    

    if not data:
        data = None
    success, response = await make_api_request(
        "/mgmt/v1/monitors/config/{path_id}",
        method="DELETE",
        params=params,
        data=data
    )
    if not success:
        logger.error(f"Request failed: {response.get('error')}")
        return {"error": response.get('error', 'Request failed')}
    return response
