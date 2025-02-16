CREATE DATABASE gamebar;

CREATE TABLE employees(
    id SERIAL NOT NULL PRIMARY KEY,
    first_name VARCHAR(30),
    last_name VARCHAR(30),
    hiring_data DATE DEFAULT '2023-01-01',
    salary NUMERIC(10, 2),
    devices_number INT
);

CREATE TABLE departments (
    id SERIAL PRIMARY KEY NOT NULL,
    name VARCHAR(30),
    code CHAR(3),
    description TEXT
);

CREATE TABLE issues(
    id SERIAL PRIMARY KEY NOT NULL,
    description VARCHAR(50),
    data DATE,
    start TIMESTAMP
);

ALTER TABLE employees
ADD COLUMN middle_name VARCHAR(30)
;

ALTER TABLE employees
ALTER COLUMN salary SET NOT NULL,
ALTER COLUMN salary SET DEFAULT 0,
ALTER COLUMN hiring_data SET NOT NULL
;

ALTER TABLE employees
ALTER COLUMN middle_name TYPE VARCHAR(35)
;

ALTER TABLE employees
ALTER COLUMN salary SET NOT NULL,
ALTER COLUMN salary SET DEFAULT 0,
ALTER COLUMN hiring_data SET NOT NULL
;

ALTER TABLE employees
ALTER COLUMN middle_name TYPE VARCHAR(50)
;

TRUNCATE TABLE issues;

DROP TABLE departments;

--Comment single line
/*
 Comment multiple lines
 */

