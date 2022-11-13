-- DROP TABLE IF EXISTS inventory;
DROP TABLE IF EXISTS cakes;
DROP TABLE IF EXISTS bakers;

CREATE TABLE bakers (
  id SERIAL PRIMARY KEY,
  full_name VARCHAR(255),
  favourite_quote VARCHAR(255),
  length_of_service INT,
  salary INT
);

CREATE TABLE cakes (
  id SERIAL PRIMARY KEY,
  full_name VARCHAR(255),
  qty_on_hand INT,
  manufacture_cost FLOAT,
  selling_price FLOAT,
  baker_id INT NOT NULL REFERENCES bakers(id) ON DELETE CASCADE,
  category VARCHAR(255),
  vegetarian BOOLEAN,
  daily_sales_forecast INT,
  par_level INT
);

-- CREATE TABLE inventory (
--     id SERIAL PRIMARY KEY
--     full_name VARCHAR(255),
--     available_funds FLOAT,
--     baker_id INT NOT NULL REFERENCES bakers(id) ON DELETE CASCADE,
--     cake_id INT NOT NULL REFERENCES cakes(id) ON DELETE CASCADE,
-- )


