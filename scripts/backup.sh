#!/bin/bash
docker exec db pg_dump -U $DB_USER $DB_NAME > backup.sql