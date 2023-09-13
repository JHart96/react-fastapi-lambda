# Use Python 3.9 image from the Lambda Runtime
FROM public.ecr.aws/lambda/python:3.9

# Install requirements
COPY ./app/requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

# Copy app code
COPY ./app ./app

# Create Lambda handler
CMD ["app.main.handler"]
