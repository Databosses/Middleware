INSERT INTO
  LOCATION(CITY, STATE)
VALUES
("MUMBAI", "MAHARASHTRA");

INSERT INTO
  LOCATION(CITY, STATE)
VALUES
("CHENNAI", "TAMIL NADU");

INSERT INTO
  LOCATION(CITY, STATE)
VALUES
("BENGALURU", "KARNATAKA");

INSERT INTO
  LOCATION(CITY, STATE)
VALUES
("KOLKATA", "WEST BENGAL");

INSERT INTO
  LOCATION(CITY, STATE)
VALUES
("BHUBANESWAR", "ODISHA");

INSERT INTO
  LOCATION(CITY, STATE)
VALUES
("BHOPAL", "MADHYA PRADESH");

INSERT INTO
  LOCATION(CITY, STATE)
VALUES
("BIHAR", "PATNA");

INSERT INTO
  LOCATION(CITY, STATE)
VALUES
("GANDHINAGAR", "GUJURAT");

INSERT INTO
  LOCATION(CITY, STATE)
VALUES
("JAIPUR", "RAJASTHAN");

INSERT INTO
  LOCATION(CITY, STATE)
VALUES
("IMPHAL", "MANIPUR");

INSERT INTO
  EMPLOYEE(FIRSTNAME, LASTNAME, DOB, ROLE, LOC_ID, WORK_EMAIL)
VALUES
  (
    "SUCHARITA",
    "TRIPATHY",
    "1990-07-06",
    "CQE",
    2,
    "SUCHARITA.TRIPATHY@TEST.COM"
  );

INSERT INTO
  EMPLOYEE(FIRSTNAME, LASTNAME, DOB, ROLE, LOC_ID, WORK_EMAIL)
VALUES
  (
    "UJJWAL",
    "KALRA",
    "1990-07-05",
    "CQE",
    3,
    "UJJWAL.KALRA@TEST.COM"
  );

INSERT INTO
  EMPLOYEE(FIRSTNAME, LASTNAME, DOB, ROLE, LOC_ID, WORK_EMAIL)
VALUES
  (
    "AKHIL",
    "S",
    "1990-07-05",
    "PPDE",
    4,
    "AKHIL.S@TEST.COM"
  );

INSERT INTO
  EMPLOYEE(FIRSTNAME, LASTNAME, DOB, ROLE, LOC_ID, WORK_EMAIL)
VALUES
  (
    "SHRUTI",
    "KATARE",
    "1990-07-04",
    "PPDE",
    5,
    "SHRUTI.KATARE@TEST.COM"
  );

INSERT INTO
  EMPLOYEE(FIRSTNAME, LASTNAME, DOB, ROLE, LOC_ID, WORK_EMAIL)
VALUES
  (
    "ANCHAL",
    "GUPTA",
    "1990-07-03",
    "PPDE",
    6,
    "ANCHAL.GUPTA@TEST.COM"
  );

INSERT INTO
  EMPLOYEE(FIRSTNAME, LASTNAME, DOB, ROLE, LOC_ID, WORK_EMAIL)
VALUES
  (
    "MALAY",
    "ROUTERLA",
    "1990-07-02",
    "PPDE",
    7,
    "MALAY.ROUTELA@TEST.COM"
  );

UPDATE
  EMPLOYEE
SET
  MANAGER_ID = 15
WHERE
  ID IN (14, 16, 17, 18, 19);

INSERT INTO
  CONFIGURATION(NAME, CREATION_TIME, DESCRIPTION, OWNER)
VALUES
  (
    "CONFIG1",
    DATETIME('NOW'),
    "DETAILED SPECIFICATION CAN BE FOUND AT HTTP://TEST.COM",
    14
  );

INSERT INTO
  CONFIGURATION(NAME, CREATION_TIME, DESCRIPTION, OWNER)
VALUES
  (
    "CONFIG2",
    DATETIME('NOW'),
    "DETAILED SPECIFICATION CAN BE FOUND AT HTTP://TEST1.COM",
    14
  );

INSERT INTO
  CONFIGURATION(NAME, CREATION_TIME, DESCRIPTION, OWNER)
VALUES
  (
    "CONFIG3",
    DATETIME('NOW'),
    "DETAILED SPECIFICATION CAN BE FOUND AT HTTP://TEST2.COM",
    14
  );

INSERT INTO
  LOT(
    NAME,
    MATERIAL_TYPE,
    HEIGHT,
    DIAMETER,
    CONFIGURATION,
    LOC_ID
  )
VALUES
("TEST-LOT-1", "METAL", 20.6, 7.3, 1, 2);

INSERT INTO
  LOT(
    NAME,
    MATERIAL_TYPE,
    HEIGHT,
    DIAMETER,
    CONFIGURATION,
    LOC_ID
  )
VALUES
("TEST-LOT-2", "GLASS", 28.45, 8.38, 2, 2);

INSERT INTO
  LOT(
    NAME,
    MATERIAL_TYPE,
    HEIGHT,
    DIAMETER,
    CONFIGURATION,
    LOC_ID
  )
VALUES
("TEST-LOT-3", "PLASTIC", 30, 7.3, 3, 2);

INSERT INTO
  PART(TEST_START_TIME, TEST_END_TIME, BUCKET, LOT)
VALUES
("2021-10-25 02:34:56", "2021-10-25 04:50:50", 0, 1);

INSERT INTO
  PART(TEST_START_TIME, TEST_END_TIME, BUCKET, LOT)
VALUES
("2021-10-26 02:34:56", "2021-10-26 04:50:50", 0, 1);

INSERT INTO
  PART(TEST_START_TIME, TEST_END_TIME, BUCKET, LOT)
VALUES
("2021-10-27 02:34:56", "2021-10-27 04:50:50", 0, 1);

INSERT INTO
  PART(TEST_START_TIME, TEST_END_TIME, BUCKET, LOT)
VALUES
("2021-10-27 02:34:56", "2021-10-27 04:50:50", 0, 1);

INSERT INTO
  PART(TEST_START_TIME, TEST_END_TIME, BUCKET, LOT)
VALUES
("2021-10-27 01:34:56", "2021-10-27 03:50:50", 0, 1);

INSERT INTO
  DEFECT(TYPE)
VALUES
("SCRATCH");

INSERT INTO
  DEFECT(TYPE)
VALUES
("HOLE");

INSERT INTO
  DEFECT(TYPE)
VALUES
("DIM_ERR");

INSERT INTO
  DEFECT_HOLE(DEFECT_ID, DIAMETER, CIRCULAR_RATIO)
VALUES
(2, 0.2, 0.9);

INSERT INTO
  DEFECT_SCRATCH(DEFECT_ID, DEPTH, ASPECT_RATIO)
VALUES
(1, 0.01, "16:9");

INSERT INTO
  DEFECT_DIMENSION_ERROR(DEFECT_ID, ACTUAL_DIAMETER, ACTUAL_HEIGHT)
VALUES
(3, 30.9, 7.4);

INSERT INTO
  PART_DEFECT(PART_ID, DEFECT_ID, DEFECT_COUNT, SEVERITY)
VALUES
(1, 1, 2, "LOW");

INSERT INTO
  PART_DEFECT(PART_ID, DEFECT_ID, DEFECT_COUNT, SEVERITY)
VALUES
(2, 1, 3, "HIGH");

INSERT INTO
  PART_DEFECT(PART_ID, DEFECT_ID, DEFECT_COUNT, SEVERITY)
VALUES
(3, 2, 1, "HIGH");

INSERT INTO
  PART_DEFECT(PART_ID, DEFECT_ID, DEFECT_COUNT, SEVERITY)
VALUES
(4, 3, 1, "HIGH");