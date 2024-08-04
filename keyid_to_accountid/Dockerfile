# Use the official Ubuntu base image
FROM ubuntu:22.04

# Create a directory
RUN mkdir -p /app

# Set the working directory
WORKDIR /app

# Copy the Lambda function code to the working directory
COPY main.py .
COPY requirements.txt .

# Install necessary system dependencies
RUN apt-get update && \
    apt-get install -y python3 python3-pip git

# Install any additional Python dependencies your Lambda function requires
#RUN pip3 install requests
RUN python3 -m pip install -r requirements.txt

# Install any additional Python dependencies your Lambda function requires
#RUN pip3 install boto3

# Install AWS Lambda Python runtime interface client
# RUN pip3 install awslambdaric

# Install golang
#WORKDIR /usr/local
#COPY go1.22.3.linux-amd64.tar.gz /usr/local/go1.22.3.linux-amd64.tar.gz
#RUN rm -rf /usr/local/go
#RUN tar -C /usr/local -xzf go1.22.3.linux-amd64.tar.gz

# Add /usr/local/go/bin to the PATH environment variable.
#RUN export PATH=$PATH:/usr/local/go/bin

# Install App
# RUN /usr/local/go/bin/go install -v github.com/projectdiscovery/nuclei/v3/cmd/nuclei@latest
#WORKDIR /root
#RUN git clone https://github.com/projectdiscovery/nuclei.git;
#WORKDIR /root/nuclei/cmd/nuclei
# RUN cd nuclei/cmd/nuclei
#RUN /usr/local/go/bin/go build
#RUN mv nuclei /usr/local/bin/
#RUN nuclei -version

# Set the working directory
#WORKDIR /root
#RUN git clone https://github.com/projectdiscovery/nuclei-templates.git
#RUN mkdir -p /root/.config/nuclei/
#RUN cp /root/nuclei-templates/.nuclei-ignore /root/.config/nuclei/.nuclei-ignore

# WORKDIR /root

# Set the entry point for the Lambda function
# CMD ["python3", "-m", "awslambdaric", "lambda_function.handler"]
# CMD ["python3", "/app/lambda_function.py"]
# ENTRYPOINT ["mesop", "--port", "8080", "/app/main.py"]
ENTRYPOINT ["mesop", "--prod", "--port", "8080", "/app/main.py"]
CMD []