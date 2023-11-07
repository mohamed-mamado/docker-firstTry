# Specify the base image as Ubuntu
FROM ubuntu:latest

# Install required packages
RUN apt-get update
RUN apt-get install -y python3 python3-pip
RUN pip3 install pandas numpy seaborn matplotlib scikit-learn scipy

# Create a directory inside the container
RUN mkdir -p /home/doc-bd-a1/

# Set the working directory
WORKDIR /home/doc-bd-a1/


# Copy dataset to docker
COPY netflix_data.csv .
COPY load.py .
COPY dpre.py .
COPY eda.py .
COPY vis.py .
COPY model.py .
# Open the bash shell upon container startup
CMD ["/bin/bash"]