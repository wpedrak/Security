CREATE USER Kamil WITH PASSWORD 'alamakota';
GRANT ALL PRIVILEGES ON DATABASE postgres TO "Kamil";
GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO "Kamil";