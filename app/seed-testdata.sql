-- Reset auto-increment counters
DELETE FROM sqlite_sequence WHERE name IN ('account', 'position', 'user');

-- Delete existing data from tables
DELETE FROM position;
DELETE FROM account;
DELETE FROM user;

-- Insert new data
INSERT INTO user (username, password)
VALUES ('admin', 'scrypt:32768:8:1$ONXNt5bCp1BvMRTw$b5acb16088edbc80b8a81ad6812ef1789022304cf6a6af5b5a0d915f1696aff63d466277848807bd85e62198f927cadce9f02ddf0d20eadda029183231128323');

INSERT INTO account (title, user_id) 
VALUES ('Privatkonto', 1), 
       ('Sparkonto', 1), 
       ('Familienkonto', 1);

INSERT INTO position (text, amount_rappen, account_id, category_id)
VALUES   ('Payment from Client A', 750, 1, 1),
         ('Grocery Store Purchase', 1250, 2, 2),
         ('Internet Bill Payment', 1750, 3, 3),
         ('Coffee Shop Expense', 2250, 1, 4),
         ('Gas Station Refuel', 2750, 2, 5),
         ('Dinner with Friends', 3250, 3, 6),
         ('Salary Deposit', 3750, 1, 1),
         ('Online Shopping', 4250, 2, 2),
         ('Electricity Bill Payment', 4750, 3, 3),
         ('Lunch Expense', 5250, 1, 4),
         ('Weekend Getaway Expense', 5750, 2, 5),
         ('Bookstore Purchase', 6250, 3, 6),
         ('Rent Payment', 6750, 1, 1),
         ('Gym Membership Renewal', 7250, 2, 2),
         ('Medical Checkup Fee', 7750, 3, 3),
         ('Transportation Expense', 8250, 1, 4),
         ('Home Appliance Purchase', 8750, 2, 5),
         ('Charity Donation', 9250, 3, 6),
         ('Insurance Premium Payment', 9750, 1, 1),
         ('Car Maintenance Expense', 10250, 2, 2),
         ('School Supplies Purchase', 10750, 3, 3),
         ('Clothing Store Purchase', 11250, 1, 4),
         ('Movie Night Expense', 11750, 2, 5),
         ('Credit Card Payment', 12250, 3, 6),
         ('Utility Bill Payment', 12750, 1, 1),
         ('Home Renovation Expense', 13250, 2, 2),
         ('Restaurant Dinner', 13750, 3, 3),
         ('Vacation Expense', 14250, 1, 4),
         ('Tech Gadgets Purchase', 14750, 2, 5),
         ('Hobby Supplies Purchase', 15250, 3, 6),
         ('Tax Payment', 15750, 1, 1),
         ('Health Insurance Premium', 16250, 2, 2),
         ('Home Decor Purchase', 16750, 3, 3),
         ('Coffee Machine Upgrade', 17250, 1, 4),
         ('Online Course Subscription', 17750, 2, 5),
         ('Birthday Gift Purchase', 18250, 3, 6),
         ('Car Insurance Renewal', 18750, 1, 1),
         ('Fitness Class Fee', 19250, 2, 2),
         ('Music Concert Ticket', 19750, 3, 3),
         ('Home Office Setup', 20250, 1, 4);