use fraud_detection;
select count(*) from transactions;
SET FOREIGN_KEY_CHECKS = 0;
TRUNCATE TABLE predictions;
TRUNCATE TABLE transactions;
SET FOREIGN_KEY_CHECKS = 1;
select count(*) from transactions;
