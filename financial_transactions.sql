CREATE TABLE financial_transactions (
    transaction_id UUID PRIMARY KEY,
    product_id VARCHAR(50),
    product_name VARCHAR(50),
    product_category VARCHAR(50),
    product_price NUMERIC,
    product_quantity INTEGER,
    product_brand VARCHAR(50),
    currency VARCHAR(3),
    customer_id VARCHAR(50),
    transaction_date TIMESTAMP,
    payment_method VARCHAR(20),
    total_amount NUMERIC
);
