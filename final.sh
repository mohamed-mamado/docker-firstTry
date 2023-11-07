# Copy output files from the container to the local machine
docker cp 3eda177f76f3:/home/doc-bd-a1/netflix_data.csv /path/to/bd-a1/service-result/
docker cp 3eda177f76f3:/home/doc-bd-a1/eda-in-1.txt /path/to/bd-a1/service-result/
docker cp 3eda177f76f3:/home/doc-bd-a1/eda-in-2.txt /path/to/bd-a1/service-result/
docker cp 3eda177f76f3:/home/doc-bd-a1/eda-in-3.txt /path/to/bd-a1/service-result/
docker cp 3eda177f76f3:/home/doc-bd-a1/vis.png /path/to/bd-a1/service-result/
docker cp 3eda177f76f3:/home/doc-bd-a1/k.txt /path/to/bd-a1/service-result/
# Close the container
docker stop 3eda177f76f3