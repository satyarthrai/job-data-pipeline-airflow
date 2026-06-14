USE job_market_db;

-- =========================================
-- 1. Top Paying Job Titles
-- =========================================
SELECT 
    job_title,
    company_name,
    salary_max
FROM jobs
WHERE salary_max IS NOT NULL
ORDER BY salary_max DESC
LIMIT 10;


-- =========================================
-- 2. Most In-demand Skills (basic text search)
-- =========================================
SELECT 
    skills,
    COUNT(*) AS frequency
FROM jobs
WHERE skills IS NOT NULL
GROUP BY skills
ORDER BY frequency DESC
LIMIT 10;


-- =========================================
-- 3. Data Jobs Only (your filtered dataset)
-- =========================================
SELECT *
FROM jobs
WHERE 
    job_category LIKE '%Data%' 
    OR job_category LIKE '%Analyst%'
    OR job_category LIKE '%Engineer%'
    OR job_category LIKE '%Scientist%';


-- =========================================
-- 4. Source Quality Comparison
-- =========================================
SELECT 
    source,
    COUNT(*) AS total_jobs,
    AVG(salary_max) AS avg_salary
FROM jobs
GROUP BY source
ORDER BY total_jobs DESC;


-- =========================================
-- 5. Monthly Trend (if dates valid)
-- =========================================
SELECT 
    SUBSTRING(date_posted, 1, 7) AS month,
    COUNT(*) AS job_count
FROM jobs
GROUP BY month
ORDER BY month;