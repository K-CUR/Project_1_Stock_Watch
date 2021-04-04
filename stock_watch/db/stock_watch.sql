DROP TABLE fabrics;
DROP TABLE manufacturers;

CREATE TABLE manufacturers (
    id SERIAL PRIMARY KEY,
    manufacturer_name VARCHAR(255),
    sales_contact VARCHAR(255),
    active BOOlEAN
);

CREATE TABLE fabrics (
    id SERIAL PRIMARY KEY,
    manufacturer_id INT REFERENCES manufacturers(id) ON DELETE CASCADE,
    design_ref VARCHAR(255),
    main_colour VARCHAR(255),
    style VARCHAR(255),
    stock_price DECIMAL(5,2),
    sale_price DECIMAL(5,2),
    quantity INT
);