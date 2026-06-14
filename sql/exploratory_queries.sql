USE job_market_db;

-- =========================================
-- 1. Total Jobs
-- =========================================
SELECT COUNT(*) AS total_jobs FROM jobs;


-- =========================================
-- 2. Jobs by Source
-- =========================================
SELECT 
    source,
    COUNT(*) AS total_jobs
FROM jobs
GROUP BY source
ORDER BY total_jobs DESC;


-- =========================================
-- 3. Jobs by Category
-- =========================================
SELECT 
    job_category,
    COUNT(*) AS total_jobs
FROM jobs
GROUP BY job_category
ORDER BY total_jobs DESC;


-- =========================================
-- 4. Top Companies Hiring
-- =========================================
SELECT 
    company_name,
    COUNT(*) AS total_jobs 
FROM jobs
GROUP BY company_name
ORDER BY total_jobs DESC
LIMIT 10;


-- =========================================
-- 5. Remote vs Onsite
-- =========================================
SELECT 
    CASE 
        WHEN LOWER(location) LIKE '%remote%' THEN 'Remote'
        ELSE 'Onsite/Hybrid'
    END AS work_type,
    COUNT(*) AS total_jobs
FROM jobs
GROUP BY work_type;


-- =========================================
-- 6. Salary Insights (Basic)
-- =========================================
SELECT 
    job_category,
    AVG(salary_min) AS avg_min_salary,
    AVG(salary_max) AS avg_max_salary
FROM jobs
WHERE salary_min IS NOT NULL
GROUP BY job_category
ORDER BY avg_max_salary DESC;