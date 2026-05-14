# FastAPI Practice

FastAPI is a modern, high-performance Python web framework for building APIs with automatic OpenAPI schema generation, validation, and interactive docs.

## Session Focus

Every question and task in this session is directed toward solving the issue below. If a question appears unrelated to this problem, remind the user of this focus.

## Current Issue

FastAPI generates OpenAPI schema entries for the responses a route explicitly declares, but does not automatically document the 404 response that the framework returns when a path does not match. Add a way to configure FastAPI to automatically include standard error responses in the OpenAPI schema for every route.
