drop table car;
create table car (
    id SERIAL PRIMARY KEY,
    name varchar(100) NOT NULL
);

drop table region;
create table region (
    id SERIAL PRIMARY KEY,
    name varchar(100) NOT NULL
);

drop table dealer;
create table dealer (
    id SERIAL PRIMARY KEY,
    account varchar(100) NOT NULL
);

drop table region_price;
create table region_price (
    id SERIAL PRIMARY KEY,
    price INTEGER NOT NULL,
    car INTEGER REFERENCES car ON DELETE CASCADE,
    region INTEGER REFERENCES region ON DELETE CASCADE
);

drop table price;
create table price (
    id SERIAL PRIMARY KEY,
    price INTEGER NOT NULL,
    car INTEGER REFERENCES car ON DELETE CASCADE,
    region INTEGER REFERENCES region ON DELETE CASCADE,
    dealer INTEGER REFERENCES dealer ON DELETE CASCADE
);

DROP FUNCTION ensure_lower_price;
CREATE FUNCTION ensure_lower_price() RETURNS trigger AS $$
DECLARE
    price_in_region INTEGER;
BEGIN
    SELECT INTO price_in_region pr.price 
    FROM region_price
    WHERE car = NEW.car
    AND   region = NEW.region;


    IF NEW.price >= price_in_region THEN
        RAISE EXCEPTION 'Price can not be worst than price in region';
    END IF;
  RETURN NEW;
END
$$ LANGUAGE 'plpgsql';

DROP TRIGGER ensure_lower_price on price;
CREATE TRIGGER ensure_lower_price BEFORE INSERT OR UPDATE ON price
    FOR EACH ROW EXECUTE PROCEDURE ensure_lower_price();
