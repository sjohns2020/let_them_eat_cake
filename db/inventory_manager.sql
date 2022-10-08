DROP TABLE IF EXISTS cakes;
DROP TABLE IF EXISTS bakers;

CREATE TABLE bakers (
  id SERIAL PRIMARY KEY,
  full_name VARCHAR(255),
  favourite_quote VARCHAR(255),
  length_of_service INT,
  salary FLOAT
);

CREATE TABLE cakes (
  id SERIAL PRIMARY KEY,
  full_name VARCHAR(255),
  qty_on_hand INT,
  manufacture_cost INT,
  selling_price FLOAT,
  baker_id INT NOT NULL REFERENCES bakers(id),
  category VARCHAR(255),
  vegetarian BOOLEAN,
  daily_sales_forecast INT,
  par_level INT
);


