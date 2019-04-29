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

DROP TRIGGER ensure_lower_price on price;
DROP FUNCTION ensure_lower_price;

CREATE FUNCTION ensure_lower_price() RETURNS trigger AS $$
DECLARE
    price_in_region INTEGER;
BEGIN
    SELECT rp.price INTO price_in_region
    FROM region_price as rp
    WHERE rp.car = NEW.car
    AND   rp.region = NEW.region;

    -- RAISE EXCEPTION '%, %', ;

    IF NEW.price >= price_in_region THEN
        RAISE EXCEPTION 'Price can not be worst than price in region';
    END IF;
  RETURN NEW;
END
$$ LANGUAGE 'plpgsql';

CREATE TRIGGER ensure_lower_price BEFORE INSERT OR UPDATE ON price
    FOR EACH ROW EXECUTE PROCEDURE ensure_lower_price();

DROP FUNCTION dealer_by_id;
CREATE FUNCTION dealer_by_id(integer) RETURNS text AS $$
DECLARE
    result text;
BEGIN
    SELECT account into result
    FROM dealer
    WHERE id = $1;

    RETURN result;
END
$$ LANGUAGE 'plpgsql';

ALTER TABLE price ENABLE ROW LEVEL SECURITY;
DROP POLICY price_policy ON price;
CREATE POLICY price_policy ON price USING (dealer_by_id(dealer) = current_user);
