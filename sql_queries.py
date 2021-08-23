# TABLE NAMES
AIRPORTS = "airports"
DEMOGRAPHICS = "demographics"
IMMIGRATIONS = "immigrations"
TEMPERATURES = "temperatures"

# DROP TABLES


def drop_table(table: str) -> str:
    """DROP query template.

    Args:
        table: name of a table to drop.
    Returns:
        DROP query.
    Raises:
    """
    return "drop table if exists {};".format(table)


drop_airports = drop_table(AIRPORTS)
drop_demographics = drop_table(DEMOGRAPHICS)
drop_immigrations = drop_table(IMMIGRATIONS)
drop_temperatures = drop_table(TEMPERATURES)

drop_table_queries = [
    drop_airports,
    drop_demographics,
    drop_immigrations,
    drop_temperatures,
]

# CREATE TABLES
create_airports = f"""
create table if not exists {AIRPORTS} (
    iata_code    varchar(3),
    name         varchar,
    type         varchar,
    coordinates  varchar,
    city         varchar,
    state_code   varchar,
    iso_country  varchar,
    iso_region   varchar,
    gps_code     varchar,
    primary key (iata_code)
);
"""
create_demographics = f"""
create table if not exists {DEMOGRAPHICS} (
    city                   varchar,
    state_code             varchar(2),
    state                  varchar,
    race                   varchar,
    count                  int,
    male_population        int,
    female_population      int,
    total_population       int,
    median_age             float,
    num_veterans           int,
    foreign_born           int,
    average_household_size float
);
"""
create_immigrations = f"""
create table if not exists {IMMIGRATIONS} (
    cicid    int,
    year     int,
    month    int,
    cit      int,
    res      int,
    iata     varchar(3),
    arrdate  int,
    mode     int,
    addr     varchar(2),
    depdate  int,
    bir      int,
    visa     int,
    count    int,
    dtadfile varchar,
    entdepa  varchar(1),
    entdepd  varchar(1),
    matflag  varchar(1),
    biryear  int,
    dtaddto  varchar,
    gender   varchar(1),
    airline  varchar,
    admnum   bigint,
    fltno    varchar,
    visatype varchar,
    primary key (cicid)
);
"""
create_temperatures = f"""
create table if not exists {TEMPERATURES} (
    timestamp                       DATE,
    average_temperature             float,
    average_temperature_uncertainty float,
    city                            varchar,
    country                         varchar,
    latitude                        varchar,
    longitude                       varchar
);
"""

create_table_queries = [
    create_airports,
    create_demographics,
    create_immigrations,
    create_temperatures,
]

# INSERT DATA
airport_insert = f"""
insert into {AIRPORTS} (
    iata_code,
    name,
    type,
    coordinates,
    city,
    state_code,
    iso_country,
    iso_region,
    gps_code
)
values (%s, %s, %s, %s, %s, %s, %s, %s, %s);"""
demographic_insert = f"""
insert into {DEMOGRAPHICS} (
    city,
    state_code,
    state,
    race,
    count,
    male_population,
    female_population,
    total_population,
    median_age,
    num_veterans,
    foreign_born,
    average_household_size
)
values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"""
immigration_insert = f"""
insert into {IMMIGRATIONS} (
    cicid,
    year,
    month,
    cit,
    res,
    iata,
    arrdate,
    mode,
    addr,
    depdate,
    bir,
    visa,
    count,
    dtadfile,
    entdepa,
    entdepd,
    matflag,
    biryear,
    dtaddto,
    gender,
    airline,
    admnum,
    fltno,
    visatype
)
values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
        %s, %s, %s, %s, %s, %s, %s);"""


temperature_insert = f"""
insert into {TEMPERATURES} (
    timestamp,
    average_temperature,
    average_temperature_uncertainty,
    city,
    country,
    latitude,
    longitude
)
values (%s, %s, %s, %s, %s, %s, %s);"""
