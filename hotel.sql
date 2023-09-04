
use hotel;
CREATE TABLE reservations (
  id INT AUTO_INCREMENT PRIMARY KEY,
  first_name VARCHAR(50),
  last_name VARCHAR(50),
  contact_number VARCHAR(10),
  address VARCHAR(255),
  check_in_date DATE,
  check_out_date DATE,
  room_type ENUM('Single Bed', 'Double Bed','Three Bed','Four Bed'),
  num_of_people ENUM('1', '2','3','4','5','6','7','8','9','10'),
  room_number int references rooms(room_number),
  wifi ENUM('Yes', 'No') references rooms(wifi),
  ac ENUM('Yes', 'No') references rooms(ac),
  payment enum('Card', 'Cash')
);
CREATE TABLE rooms (
  room_number int NOT NULL PRIMARY KEY,
  room_type ENUM('Single Bed', 'Double Bed','Three Bed','Four Bed'),
  room_price int,
  wifi ENUM('Yes', 'No'),
  ac ENUM('Yes', 'No'),
  check_in_date DATE references reservations(check_in_date),
  check_out_date DATE references reservations(check_out_date)
);
