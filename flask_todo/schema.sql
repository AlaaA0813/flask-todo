DROP TABLE IF EXISTS task_list;

CREATE TABLE task_list (
  id bigserial PRIMARY KEY,
  task varchar(250) NOT NULL,
  timestamp_of_task timestamp NOT NULL,
  completed boolean NOT NULL,
);
