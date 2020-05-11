docker build -t tsmirnova/task .
docker run -v"$(pwd)"/target:/api_test/tests/report tsmirnova/task:latest
target/report.html