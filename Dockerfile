# Use an official PostgreSQL image as a base image
FROM postgres:latest

# Set environment variables
ENV POSTGRES_DB=demo6
ENV POSTGRES_USER=posgress
ENV POSTGRES_PASSWORD=123456

# Expose the PostgreSQL port
EXPOSE 5432

# Copy the initialization script to the container
COPY init.sql /docker-entrypoint-initdb.d/

# The init.sql script will be executed during the database initialization
# Customize the script according to your needs (e.g., create user, grant permissions)
