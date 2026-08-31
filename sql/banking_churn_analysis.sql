-- 1. Executive Portfolio KPIs
SELECT 
    COUNT(customer_id) AS total_customers,
    SUM(churn) AS total_churned_customers,
    ROUND(AVG(churn) * 100, 2) AS churn_rate_pct,
    ROUND(SUM(CASE WHEN churn = 1 THEN balance ELSE 0 END), 2) AS total_capital_lost_usd
FROM `banking-churn-project.banking_analytics.bank_churn`;

-- 2. Regional Risk Breakdown
SELECT 
    country,
    COUNT(customer_id) AS total_customers,
    SUM(churn) AS churned_customers,
    ROUND(AVG(churn) * 100, 2) AS churn_rate_pct,
    ROUND(AVG(balance), 2) AS avg_balance
FROM `banking-churn-project.banking_analytics.bank_churn`
GROUP BY country
ORDER BY churn_rate_pct DESC;

-- 3. Age Bracket & High-Value Capital Leakage
SELECT 
    CASE 
        WHEN age BETWEEN 18 AND 30 THEN '18-30 (Young Adult)'
        WHEN age BETWEEN 31 AND 45 THEN '31-45 (Mid Career)'
        WHEN age BETWEEN 46 AND 60 THEN '46-60 (Pre-Retirement)'
        ELSE '61+ (Retiree)'
    END AS age_bracket,
    COUNT(customer_id) AS total_customers,
    SUM(churn) AS churned_customers,
    ROUND(AVG(churn) * 100, 2) AS churn_rate_pct,
    ROUND(SUM(CASE WHEN churn = 1 THEN balance ELSE 0 END), 2) AS lost_balance
FROM `banking-churn-project.banking_analytics.bank_churn`
GROUP BY age_bracket
ORDER BY churn_rate_pct DESC;

-- 4. Product Holding & Engagement Risk
SELECT 
    products_number,
    active_member,
    COUNT(customer_id) AS total_customers,
    SUM(churn) AS churned_customers,
    ROUND(AVG(churn) * 100, 2) AS churn_rate_pct
FROM `banking-churn-project.banking_analytics.bank_churn`
GROUP BY products_number, active_member
ORDER BY products_number, active_member;