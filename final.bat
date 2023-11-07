@echo off
:: Get the container ID
for /f "tokens=*" %%i in ('docker ps -l -q') do set container_id=%%i

:: Copy output files from the container to the local machine
docker cp "%container_id%:/home/doc-bd-a1/res_dpre.csv" service-result
docker cp "%container_id%:/home/doc-bd-a1/eda-in-1.txt" service-result
docker cp "%container_id%:/home/doc-bd-a1/eda-in-2.txt" service-result
docker cp "%container_id%:/home/doc-bd-a1/eda-in-3.txt" service-result
docker cp "%container_id%:/home/doc-bd-a1/vis.png" service-result
docker cp "%container_id%:/home/doc-bd-a1/k.txt" service-result

:: Stop the Docker container
docker container stop "%container_id%"
