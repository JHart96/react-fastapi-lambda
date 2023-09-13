# FastAPI + Lambda + Serverless + Docker

This is a simple example of how to deploy a FastAPI application to AWS Lambda using `serverless` and Docker images. The benefit of this approach is that unlike .zip files which have a 50mb compressed limit on Lambda, the size limit is 10gb when using images. 

## Run locally

To run the FastAPI locally, use the standard FastAPI command:

```bash
uvicorn main:app --reload
```

### React app dev

FastAPI only serves pre-built frontends, so when developing the React app you'll need to run the FastAPI backend and React app frontend on separate local servers. To run the FastAPI backend you can use the command above, but to run the React app frontend you'll need to run `npm start` inside `frontend` and be sure to navigate to the right port on localhost (the node one, not the one hosted by FastAPI).

## Deploy

Make sure the latest React app has been compiled. To do so, `cd` into `frontend` and run:

```bash
npm build
```

Now to deploy the full app to AWS Lambda, run:

```bash
serverless deploy
```

This will return a URL that can be used to access the function.

### Domain

Through route 53 I think we can set up domains using this: https://www.serverless.com/plugins/serverless-domain-manager.