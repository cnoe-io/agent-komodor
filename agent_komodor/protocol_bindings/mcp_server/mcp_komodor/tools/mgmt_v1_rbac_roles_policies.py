
"""Tools for /mgmt/v1/rbac/roles/policies operations"""

import logging
from typing import Dict, Any
from mcp_komodor.api.client import make_api_request

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger("mcp_tools")


async def rbacrolepoliciescontrollerv1_post(body_roleId: str, body_policyId: str) -> Dict[str, Any]:
    '''
    Creates a new RBAC role policy association by making a POST request to the specified endpoint.

    Args:
        body_roleId (str): The ID of the role to associate with the policy.
        body_policyId (str): The ID of the policy to associate with the role.

    Returns:
        Dict[str, Any]: The JSON response from the API call, containing the result of the role-policy association.

    Raises:
        Exception: If the API request fails or returns an error.

    OpenAPI Specification:
        post:
          summary: Create a new RBAC role policy association.
          operationId: rbacrolepoliciescontrollerv1_post
          requestBody:
            required: true
            content:
              application/json:
                schema:
                  type: object
                  properties:
                    roleId:
                      type: string
                      description: The ID of the role.
                    policyId:
                      type: string
                      description: The ID of the policy.
          responses:
            '200':
              description: Successful operation
              content:
                application/json:
                  schema:
                    type: object
                    properties:
                      success:
                        type: boolean
                        description: Indicates if the operation was successful.
                      data:
                        type: object
                        description: Contains the details of the role-policy association.
            '400':
              description: Bad Request
            '500':
              description: Internal Server Error
    '''
    logger.debug("Making POST request to /mgmt/v1/rbac/roles/policies")
    params = {}
    data = None
    

    

    


    
    data = {}

    
    data["roleId"] = body_roleId
    

    
    data["policyId"] = body_policyId
    

    if not data:
        data = None
    success, response = await make_api_request(
        "/mgmt/v1/rbac/roles/policies",
        method="POST",
        params=params,
        data=data
    )
    if not success:
        logger.error(f"Request failed: {response.get('error')}")
        return {"error": response.get('error', 'Request failed')}
    return response


async def rbacrolepoliciescontrollerv1_delete(body_roleId: str, body_policyId: str) -> Dict[str, Any]:
    '''
    Deletes a policy from a role in the RBAC system.

    Args:
        body_roleId (str): The ID of the role from which the policy will be deleted.
        body_policyId (str): The ID of the policy to be deleted from the role.

    Returns:
        Dict[str, Any]: The JSON response from the API call, indicating success or failure.

    Raises:
        Exception: If the API request fails or returns an error.

    OpenAPI Specification:
        delete:
          summary: Deletes a policy from a role in the RBAC system.
          operationId: rbacrolepoliciescontrollerv1_delete
          parameters:
            - name: body_roleId
              in: query
              required: true
              description: The ID of the role.
              schema:
                type: string
            - name: body_policyId
              in: query
              required: true
              description: The ID of the policy.
              schema:
                type: string
          responses:
            '200':
              description: Policy successfully deleted from the role.
              content:
                application/json:
                  schema:
                    type: object
                    properties:
                      success:
                        type: boolean
                      message:
                        type: string
            '400':
              description: Bad request, invalid role or policy ID.
              content:
                application/json:
                  schema:
                    type: object
                    properties:
                      error:
                        type: string
            '404':
              description: Role or policy not found.
              content:
                application/json:
                  schema:
                    type: object
                    properties:
                      error:
                        type: string
            '500':
              description: Internal server error.
              content:
                application/json:
                  schema:
                    type: object
                    properties:
                      error:
                        type: string
    '''
    logger.debug("Making DELETE request to /mgmt/v1/rbac/roles/policies")
    params = {}
    data = None
    

    

    


    
    data = {}

    
    data["roleId"] = body_roleId
    

    
    data["policyId"] = body_policyId
    

    if not data:
        data = None
    success, response = await make_api_request(
        "/mgmt/v1/rbac/roles/policies",
        method="DELETE",
        params=params,
        data=data
    )
    if not success:
        logger.error(f"Request failed: {response.get('error')}")
        return {"error": response.get('error', 'Request failed')}
    return response
