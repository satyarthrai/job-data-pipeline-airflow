CREATE DATABASE IF NOT EXISTS job_market_db;
USE job_market_db;

DROP TABLE IF EXISTS jobs;

CREATE TABLE jobs (
    id INT AUTO_INCREMENT PRIMARY KEY,

    job_id VARCHAR(255),
    source VARCHAR(100),
    job_title VARCHAR(255),
    job_category VARCHAR(100),
    company_name VARCHAR(255),

    location VARCHAR(255),

    date_posted VARCHAR(100),
    load_date VARCHAR(100),

    salary_min FLOAT,
    salary_max FLOAT,

    skills TEXT,
    description LONGTEXT,

    job_url TEXT
);