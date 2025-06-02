
"""Tools for /mgmt/v1/rbac/actions/{id} operations"""

import logging
from typing import Dict, Any, List
from mcp_komodor.api.client import make_api_request

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger("mcp_tools")


async def actionscontrollerv1_delete(path_id: str) -> Dict[str, Any]:
    '''
    Deletes an action controller resource identified by the given path_id.

    Args:
        path_id (str): The identifier of the action controller resource to be deleted.

    Returns:
        Dict[str, Any]: The JSON response from the API call, containing the result of the delete operation.

    Raises:
        Exception: If the API request fails or returns an error.

    OpenAPI Specification:
        delete:
          summary: Deletes an action controller resource.
          operationId: actionscontrollerv1_delete
          parameters:
            - name: path_id
              in: path
              required: true
              description: The identifier of the action controller resource.
              schema:
                type: string
          responses:
            '200':
              description: Successfully deleted the resource.
              content:
                application/json:
                  schema:
                    type: object
                    additionalProperties: true
            '400':
              description: Bad request due to invalid path_id.
            '404':
              description: Resource not found.
            '500':
              description: Internal server error.
    '''
    logger.debug("Making DELETE request to /mgmt/v1/rbac/actions/{id}")
    params = {}
    data = None
    

    


    
    data = {}

    

    if not data:
        data = None
    success, response = await make_api_request(
        f"/mgmt/v1/rbac/actions/{path_id}",
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
    Updates an action in the RBAC system with the specified description and Kubernetes ruleset.

    Args:
        path_id (str): The unique identifier for the action to be updated.
        body_description (str): The new description for the action.
        body_k8sRuleset (List[str]): A list of Kubernetes rulesets to associate with the action.

    Returns:
        Dict[str, Any]: The JSON response from the API call, containing the updated action details.

    Raises:
        Exception: If the API request fails or returns an error.

    OpenAPI Specification:
      put:
        summary: Update an action in the RBAC system.
        parameters:
          - name: path_id
            in: path
            required: true
            description: The unique identifier for the action to be updated.
            schema:
              type: string
        requestBody:
          required: true
          content:
            application/json:
              schema:
                type: object
                properties:
                  description:
                    type: string
                    description: The new description for the action.
                  k8sRuleset:
                    type: array
                    items:
                      type: string
                    description: A list of Kubernetes rulesets to associate with the action.
        responses:
          '200':
            description: Successfully updated the action.
            content:
              application/json:
                schema:
                  type: object
                  additionalProperties: true
          '400':
            description: Bad request due to invalid input.
          '404':
            description: Action not found.
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
        f"/mgmt/v1/rbac/actions/{path_id}",
        method="PUT",
        params=params,
        data=data
    )
    if not success:
        logger.error(f"Request failed: {response.get('error')}")
        return {"error": response.get('error', 'Request failed')}
    return response
