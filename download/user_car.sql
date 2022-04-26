create table car_data (
	id BIGSERIAL NOT NULL PRIMARY KEY,
	make VARCHAR(100) NOT NULL,
	model VARCHAR(100) NOT NULL,
	price NUMERIC(19, 2) NOT NULL
);

create table user_data (
	id BIGSERIAL NOT NULL PRIMARY KEY,
	first_name VARCHAR(50) NOT NULL,
	last_name VARCHAR(50) NOT NULL,
	email VARCHAR(150),
	gender VARCHAR(100) NOT NULL,
	date_of_birth DATE NOT NULL,
	contry_of_birth VARCHAR(50) NOT NULL,
    car_id BIGINT REFERENCES car (id),
    UNIQUE(car_id)
);



insert into user_data (first_name, last_name, email, gender, date_of_birth, contry_of_birth) values ('Rhonda', 'Marfield', null, 'Genderqueer', '2021-03-12', 'Philippines');
insert into user_data (first_name, last_name, email, gender, date_of_birth, contry_of_birth) values ('Malva', 'Springell', 'mspringell5@zimbio.com', 'Male', '2021-04-19', 'Philippines');
insert into user_data (first_name, last_name, email, gender, date_of_birth, contry_of_birth) values ('Giulietta', 'Sarfas', 'gsarfas6@ibm.com', 'Non-binary', '2021-05-02', 'Uruguay');

insert into car_data (make, model, price) values ('GMC', '3500', '44376.30');
insert into car_data (make, model, price) values ('Land Rover', 'Defender', '31639.32');
insert into car_data (make, model, price) values ('Mercury', 'Sable', '95731.87');