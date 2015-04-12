-- Sample SQL

CREATE TABLE things
    (
        name VARCHAR(20),
        base_thing VARCHAR,
        value MONEY,
        own_it BOOLEAN,
        PRIMARY KEY (name, base_thing, own_it)
    );

INSERT INTO things VALUES
    ('shoe', 'clothing', 20.00, True),
    ('lizard', 'pet', 50.00, False),
    ('soul', 'mythical', NULL, True);