DROP TABLE IF EXISTS hatecrimes;
DROP TABLE IF EXISTS ustates;
DROP TABLE IF EXISTS gun_violence;

CREATE TABLE IF NOT EXISTS ustates(
state_id VARCHAR(2) PRIMARY KEY,
state_name VARCHAR(30) UNIQUE
);

--

CREATE TABLE IF NOT EXISTS hatecrimes(
incident_id INTEGER,
hyear	INTEGER,
state_id CHAR(2) REFERENCES ustates(state_id),
state_name VARCHAR(30),
offender_count INTEGER,
offender_race VARCHAR(30),
victim_count INTEGER,
offense_type VARCHAR(255),
bias_desc VARCHAR(255),
PRIMARY KEY (incident_id, state_id)
);

--

CREATE TABLE IF NOT EXISTS gun_violence(
incident_id INTEGER PRIMARY KEY,
incident_date DATE,
state_name VARCHAR(30) REFERENCES ustates(state_name),
city VARCHAR(30),
n_killed INTEGER,
n_injured INTEGER,
n_guns INTEGER
);