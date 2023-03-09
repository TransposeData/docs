# Version Control

- Endpoint versions are immutable (this is so you can't accidentally delete an important production endpoint)
- To create a new version of an endpoint, you can either:
  - Create a new endpoint from scratch
  - Create a new version in an existing endpoint
  - Instructions on how to call specific version or latest version
  - Behaviour on deletion (calling latest will fallback to older version, calling specific version will return 404?  test this)