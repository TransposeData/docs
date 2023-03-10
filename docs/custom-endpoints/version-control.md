# Version Control

## Version Immutability

Endpoint versions are immutable by design.  This means that once you've created a version of an endpoint, you can't change it.  This is to ensure that you can't accidentally delete an important production endpoint.

To update an endpoint, you can instead add a new version.  To do this, go to the Playground and open a query that you wish to create a new endpoint version from.  Select the "Deploy to Endpoint" button, and select the endpoint from the 'Choose an Endpoint' dropdown.  You can then optionally give the new version a description, choose whether the version is public or private, and then deploy.

## Calling Specific Versions

View the instructions in [integrate](/custom-endpoints/integrate/#calling-specific-versions-of-an-endpoint) for how to call specific versions of an endpoint, or how to automatically select the latest version in your code.

## Deleting Versions

Query Versions can be deleted at any time from the Playground.  To do this, select the endpoint you want from the 'My Endpoints' tab in the Playground, and then select the version you want to delete from the 'Endpoint Versions' section.  Click the three dots, and selete 'Delete Version' from the dropdown.

When you delete a version, you will no longer be able to call this version from the API.  If you try to automatically infer the latest version, it will default to the next latest version that is not deleted (if one exists).  If all versions are deleted, the API will return an error 400.