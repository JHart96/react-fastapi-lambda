# FastAPI + Lambda + Serverless + Docker

This is a simple example of how to deploy a FastAPI application to AWS Lambda using `serverless` and Docker images. The benefit of this approach is that unlike .zip files which have a 50mb compressed limit on Lambda, the size limit is 10gb when using images. 

## Run locally

To run locally as a dev server, use the standard FastAPI command:

```bash
uvicorn app.main:app --reload
```

## Deploy

To deploy to AWS Lambda, run:

```
serverless deploy
```

This will return a URL that can be used to access the function.

### Domain

Through route 53 I think we can set up domains using this: https://www.serverless.com/plugins/serverless-domain-manager.