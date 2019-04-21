-- it seems that it is not really perfect
-- https://www.postgresql.org/docs/current/encryption-options.html

CREATE EXTENSION IF NOT EXISTS pgcrypto;

-- column level encryption (simply crypto functions)

CREATE TABLE secret_card(
    own varchar(255),
    num varchar(255)
    );

insert into secret_card (own, num) values
('ala',PGP_SYM_ENCRYPT('11111','AES_KEY')),
('marek',PGP_SYM_ENCRYPT('22222','AES_KEY')),
('ola',PGP_SYM_ENCRYPT('33333','AES_KEY'));

select * from secret_card;

select own,pgp_sym_decrypt(num::bytea,'AES_KEY') as num from secret_card;

-- no key management included