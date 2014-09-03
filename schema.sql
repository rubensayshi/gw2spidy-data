DROP TABLE IF EXISTS item;
CREATE TABLE item (
  data_id INT(11) NOT NULL,
  name VARCHAR(255) NOT NULL,
  type_id INT(11) NOT NULL,
  sub_type_id INT(11) NOT NULL DEFAULT 0,
  max_offer_unit_price INT(11) NOT NULL,
  min_sale_unit_price INT(11) NOT NULL,

  PRIMARY KEY (`data_id`)
);