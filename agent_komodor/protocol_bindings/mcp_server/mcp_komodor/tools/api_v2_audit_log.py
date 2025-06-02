
"""Tools for /api/v2/audit-log operations"""

import logging
from typing import Dict, Any, List
from mcp_komodor.api.client import make_api_request

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger("mcp_tools")


async def get_api_v2_audit_log(param_id: str = None, param_userIds: List[str] = None, param_actions: List[str] = None, param_categories: List[str] = None, param_operations: List[str] = None, param_entityTypes: List[str] = None, param_entityName: str = None, param_startTime: str = None, param_endTime: str = None, param_status: str = None, param_page: int = None, param_pageSize: int = None, param_sort: str = None) -> Dict[str, Any]:
    '''
    Query audit logs with filters, sort, and pagination.

    Args:
        param_id (str, optional): The unique identifier for the audit log entry. Defaults to None.
        param_userIds (List[str], optional): List of user IDs to filter the audit logs. Defaults to None.
        param_actions (List[str], optional): List of actions to filter the audit logs. Defaults to None.
        param_categories (List[str], optional): List of categories to filter the audit logs. Defaults to None.
        param_operations (List[str], optional): List of operations to filter the audit logs. Defaults to None.
        param_entityTypes (List[str], optional): List of entity types to filter the audit logs. Defaults to None.
        param_entityName (str, optional): The name of the entity to filter the audit logs. Defaults to None.
        param_startTime (str, optional): The start time for the audit log query in ISO 8601 format. Defaults to None.
        param_endTime (str, optional): The end time for the audit log query in ISO 8601 format. Defaults to None.
        param_status (str, optional): The status to filter the audit logs. Defaults to None.
        param_page (int, optional): The page number for pagination. Defaults to None.
        param_pageSize (int, optional): The number of entries per page for pagination. Defaults to None.
        param_sort (str, optional): The sort order for the audit logs. Defaults to None.

    Returns:
        Dict[str, Any]: The JSON response from the API call containing the audit logs.

    Raises:
        Exception: If the API request fails or returns an error.

    OpenAPI Specification:
        get:
          summary: Query audit logs with filters, sort, and pagination.
          parameters:
            - name: id
              in: query
              description: The unique identifier for the audit log entry.
              required: false
              schema:
                type: string
            - name: userIds
              in: query
              description: List of user IDs to filter the audit logs.
              required: false
              schema:
                type: array
                items:
                  type: string
            - name: actions
              in: query
              description: List of actions to filter the audit logs.
              required: false
              schema:
                type: array
                items:
                  type: string
            - name: categories
              in: query
              description: List of categories to filter the audit logs.
              required: false
              schema:
                type: array
                items:
                  type: string
            - name: operations
              in: query
              description: List of operations to filter the audit logs.
              required: false
              schema:
                type: array
                items:
                  type: string
            - name: entityTypes
              in: query
              description: List of entity types to filter the audit logs.
              required: false
              schema:
                type: array
                items:
                  type: string
            - name: entityName
              in: query
              description: The name of the entity to filter the audit logs.
              required: false
              schema:
                type: string
            - name: startTime
              in: query
              description: The start time for the audit log query in ISO 8601 format.
              required: false
              schema:
                type: string
            - name: endTime
              in: query
              description: The end time for the audit log query in ISO 8601 format.
              required: false
              schema:
                type: string
            - name: status
              in: query
              description: The status to filter the audit logs.
              required: false
              schema:
                type: string
            - name: page
              in: query
              description: The page number for pagination.
              required: false
              schema:
                type: integer
            - name: pageSize
              in: query
              description: The number of entries per page for pagination.
              required: false
              schema:
                type: integer
            - name: sort
              in: query
              description: The sort order for the audit logs.
              required: false
              schema:
                type: string
          responses:
            '200':
              description: Successful response containing the audit logs.
              content:
                application/json:
                  schema:
                    type: object
    '''
    logger.debug("Making GET request to /api/v2/audit-log")
    params = {}
    data = None
    

    
    params["id"] = param_id
    

    
    params["userIds"] = param_userIds
    

    
    params["actions"] = param_actions
    

    
    params["categories"] = param_categories
    

    
    params["operations"] = param_operations
    

    
    params["entityTypes"] = param_entityTypes
    

    
    params["entityName"] = param_entityName
    

    
    params["startTime"] = param_startTime
    

    
    params["endTime"] = param_endTime
    

    
    params["status"] = param_status
    

    
    params["page"] = param_page
    

    
    params["pageSize"] = param_pageSize
    

    
    params["sort"] = param_sort
    


    
    data = {}

    

    

    

    

    

    

    

    

    

    

    

    

    

    if not data:
        data = None
    success, response = await make_api_request(
        "/api/v2/audit-log",
        method="GET",
        params=params,
        data=data
    )
    if not success:
        logger.error(f"Request failed: {response.get('error')}")
        return {"error": response.get('error', 'Request failed')}
    return response
