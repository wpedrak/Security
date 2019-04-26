drop table car;
create table car (
    id INTEGER PRIMARY KEY,
    name varchar(100) NOT NULL
);

drop table region;
create table region (
    id INTEGER PRIMARY KEY,
    name varchar(100) NOT NULL
);

drop table dealer;
create table dealer (
    id INTEGER PRIMARY KEY,
    account varchar(100) NOT NULL
);

drop table price;
create table price (
    id INTEGER PRIMARY KEY,
    price INTEGER NOT NULL,
    car INTEGER REFERENCES car(id),
    region INTEGER REFERENCES region(id),
    dealer INTEGER REFERENCES dealer(id)
);