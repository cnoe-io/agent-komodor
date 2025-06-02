
"""Tools for /mgmt/v1/rbac/actions/{id} operations"""

import logging
from typing import Dict, Any, List
from mcp_komodor.api.client import make_api_request

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger("mcp_tools")


async def actionscontrollerv1_delete(path_id: str) -> Dict[str, Any]:
    '''
    Deletes an action by its ID.

    Args:
        path_id (str): The ID of the action to be deleted.

    Returns:
        Dict[str, Any]: The JSON response from the API call.

    Raises:
        Exception: If the API request fails or returns an error.

    OpenAPI Specification:
      delete:
        summary: Delete an action by ID
        operationId: actionscontrollerv1_delete
        parameters:
          - name: path_id
            in: path
            required: true
            description: The ID of the action to be deleted
            schema:
              type: string
        responses:
          '200':
            description: Action successfully deleted
            content:
              application/json:
                schema:
                  type: object
                  additionalProperties: true
          '400':
            description: Bad request
          '404':
            description: Action not found
          '500':
            description: Internal server error
    '''
    logger.debug("Making DELETE request to /mgmt/v1/rbac/actions/{id}")
    params = {}
    data = None
    

    


    
    data = {}

    

    if not data:
        data = None
    success, response = await make_api_request(
        "/mgmt/v1/rbac/actions/{path_id}",
        method="DELETE",
        params=params,
        data=data
    )
    if not success:
        logger.error(f"Request failed: {response.get('error')}")
        return {"error": response.get('error', 'Request failed')}
    return response


async def actionscontrollerv1_update(path_id: str, body_description: str, body_k8sRuleset: List[str]) -> Dict[str, Any]:
    '''
    Updates an action controller with the specified ID using the provided description and Kubernetes ruleset.

    Args:
        path_id (str): The ID of the action controller to update.
        body_description (str): The description to update for the action controller.
        body_k8sRuleset (List[str]): The Kubernetes ruleset to update for the action controller.

    Returns:
        Dict[str, Any]: The JSON response from the API call, containing the updated action controller details.

    Raises:
        Exception: If the API request fails or returns an error.

    OpenAPI Specification:
        paths:
          /mgmt/v1/rbac/actions/{id}:
            put:
              summary: Update an action controller
              parameters:
                - name: path_id
                  in: path
                  required: true
                  schema:
                    type: string
                  description: The ID of the action controller to update.
              requestBody:
                required: true
                content:
                  application/json:
                    schema:
                      type: object
                      properties:
                        description:
                          type: string
                          description: The description to update for the action controller.
                        k8sRuleset:
                          type: array
                          items:
                            type: string
                          description: The Kubernetes ruleset to update for the action controller.
              responses:
                '200':
                  description: Successful update of the action controller.
                  content:
                    application/json:
                      schema:
                        type: object
                        additionalProperties: true
                '400':
                  description: Bad request due to invalid input.
                '404':
                  description: Action controller not found.
                '500':
                  description: Internal server error.
    '''
    logger.debug("Making PUT request to /mgmt/v1/rbac/actions/{id}")
    params = {}
    data = None
    

    

    

    


    
    data = {}

    

    
    data["description"] = body_description
    

    
    data["k8sRuleset"] = body_k8sRuleset
    

    if not data:
        data = None
    success, response = await make_api_request(
        "/mgmt/v1/rbac/actions/{path_id}",
        method="PUT",
        params=params,
        data=data
    )
    if not success:
        logger.error(f"Request failed: {response.get('error')}")
        return {"error": response.get('error', 'Request failed')}
    return response
