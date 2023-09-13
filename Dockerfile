# Use Python 3.9 image from the Lambda Runtime
FROM public.ecr.aws/lambda/python:3.9

# Install requirements
COPY ./requirements.txt /requirements.txt
RUN pip install --no-cache-dir -r /requirements.txt

# Copy app code
COPY . .

# Create Lambda handler
CMD ["main.handler"]
