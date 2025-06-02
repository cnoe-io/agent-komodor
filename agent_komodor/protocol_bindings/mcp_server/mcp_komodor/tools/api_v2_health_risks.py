
"""Tools for /api/v2/health/risks operations"""

import logging
from typing import Dict, Any, List
from mcp_komodor.api.client import make_api_request

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger("mcp_tools")


async def gethealthrisks(param_pageSize: int, param_offset: int, param_impactGroupType: List[str], param_checkType: List[str] = None, param_status: List[str] = None, param_clusterName: List[str] = None, param_namespace: List[str] = None, param_shortResourceNameSearchTerm: str = None, param_shortResourceName: List[str] = None, param_impactGroupId: List[str] = None, param_severity: List[str] = None, param_komodorUid: List[str] = None, param_resourceType: List[str] = None, param_createdFromEpoch: str = None, param_createdToEpoch: str = None, param_checkCategory: List[str] = None) -> Dict[str, Any]:
    '''
    Get all the health risks.

    Args:
        param_pageSize (int): The number of results to return per page.
        param_offset (int): The offset from the start of the list of results.
        param_impactGroupType (List[str]): The types of impact groups to filter by.
        param_checkType (List[str], optional): The types of checks to filter by. Defaults to None.
        param_status (List[str], optional): The statuses to filter by. Defaults to None.
        param_clusterName (List[str], optional): The cluster names to filter by. Defaults to None.
        param_namespace (List[str], optional): The namespaces to filter by. Defaults to None.
        param_shortResourceNameSearchTerm (str, optional): A search term for short resource names. Defaults to None.
        param_shortResourceName (List[str], optional): The short resource names to filter by. Defaults to None.
        param_impactGroupId (List[str], optional): The impact group IDs to filter by. Defaults to None.
        param_severity (List[str], optional): The severities to filter by. Defaults to None.
        param_komodorUid (List[str], optional): The Komodor UIDs to filter by. Defaults to None.
        param_resourceType (List[str], optional): The resource types to filter by. Defaults to None.
        param_createdFromEpoch (str, optional): The start epoch time to filter by. Defaults to None.
        param_createdToEpoch (str, optional): The end epoch time to filter by. Defaults to None.
        param_checkCategory (List[str], optional): The check categories to filter by. Defaults to None.

    Returns:
        Dict[str, Any]: The JSON response from the API call.

    Raises:
        Exception: If the API request fails or returns an error.

    OpenAPI Specification:
        get:
          summary: Get all the health risks.
          parameters:
            - name: pageSize
              in: query
              required: true
              schema:
                type: integer
            - name: offset
              in: query
              required: true
              schema:
                type: integer
            - name: impactGroupType
              in: query
              required: true
              schema:
                type: array
                items:
                  type: string
            - name: checkType
              in: query
              schema:
                type: array
                items:
                  type: string
            - name: status
              in: query
              schema:
                type: array
                items:
                  type: string
            - name: clusterName
              in: query
              schema:
                type: array
                items:
                  type: string
            - name: namespace
              in: query
              schema:
                type: array
                items:
                  type: string
            - name: shortResourceNameSearchTerm
              in: query
              schema:
                type: string
            - name: shortResourceName
              in: query
              schema:
                type: array
                items:
                  type: string
            - name: impactGroupId
              in: query
              schema:
                type: array
                items:
                  type: string
            - name: severity
              in: query
              schema:
                type: array
                items:
                  type: string
            - name: komodorUid
              in: query
              schema:
                type: array
                items:
                  type: string
            - name: resourceType
              in: query
              schema:
                type: array
                items:
                  type: string
            - name: createdFromEpoch
              in: query
              schema:
                type: string
            - name: createdToEpoch
              in: query
              schema:
                type: string
            - name: checkCategory
              in: query
              schema:
                type: array
                items:
                  type: string
          responses:
            '200':
              description: Successful response
              content:
                application/json:
                  schema:
                    type: object
    '''
    logger.debug("Making GET request to /api/v2/health/risks")
    params = {}
    data = None
    

    
    params["pageSize"] = param_pageSize
    

    
    params["offset"] = param_offset
    

    
    params["impactGroupType"] = param_impactGroupType
    

    
    params["checkType"] = param_checkType
    

    
    params["status"] = param_status
    

    
    params["clusterName"] = param_clusterName
    

    
    params["namespace"] = param_namespace
    

    
    params["shortResourceNameSearchTerm"] = param_shortResourceNameSearchTerm
    

    
    params["shortResourceName"] = param_shortResourceName
    

    
    params["impactGroupId"] = param_impactGroupId
    

    
    params["severity"] = param_severity
    

    
    params["komodorUid"] = param_komodorUid
    

    
    params["resourceType"] = param_resourceType
    

    
    params["createdFromEpoch"] = param_createdFromEpoch
    

    
    params["createdToEpoch"] = param_createdToEpoch
    

    
    params["checkCategory"] = param_checkCategory
    


    
    data = {}

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    if not data:
        data = None
    success, response = await make_api_request(
        "/api/v2/health/risks",
        method="GET",
        params=params,
        data=data
    )
    if not success:
        logger.error(f"Request failed: {response.get('error')}")
        return {"error": response.get('error', 'Request failed')}
    return response
