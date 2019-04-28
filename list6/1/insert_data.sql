INSERT INTO car(id, name) VALUES
(1, 'Maluch'),
(2, 'Polonez'),
(3, 'Golf');

INSERT INTO region(id, name) VALUES
(1, 'EMEA'),
(2, 'USA'),
(3, 'China');

INSERT INTO dealer(id, account) VALUES
(1, 'Kamil'),
(2, 'Marek');

INSERT INTO region_price(id, car, region, price) VALUES
(1, 1, 1, 1000),
(2, 1, 2, 900),
(3, 1, 3, 300),
(4, 2, 1, 2000),
(5, 2, 2, 2100),
(6, 2, 3, 1000),
(7, 3, 1, 9900),
(8, 3, 2, 12500),
(9, 3, 3, 13000);

INSERT INTO price(id, car, region, dealer, price) VALUES
(1, 1, 1, 1, 500),
(2, 1, 1, 2, 500);

INSERT INTO price(id, car, region, dealer, price) VALUES
(3, 2, 1, 1, 2000);