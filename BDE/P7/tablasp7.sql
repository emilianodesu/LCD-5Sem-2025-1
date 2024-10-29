--create flights table
CREATE TABLE IF NOT EXISTS vuelos_equipo5 (
    year character varying,
    month character varying,
    day character varying,
    day_of_week character varying,
    airline character varying,
    flight_number character varying,
    tail_number character varying,
    origin_airport character varying,
    destination_airport character varying,
    scheduled_departure character varying,
    departure_time character varying,
    departure_delay smallint,
    taxi_out smallint,
    wheels_off character varying,
    scheduled_time smallint,
    elapsed_time smallint,
    air_time smallint,
    distance smallint,
    wheels_on character varying,
    taxi_in smallint,
    scheduled_arrival character varying,
    arrival_time character varying,
    arrivale_delay smallint,
    diverted character varying,
    cancelled character varying,
    cancellation_reason character varying,
    air_system_delay smallint,
    security_delay smallint,
    airline_delay smallint,
    late_aircraft_delay smallint,
    weather_delay smallint,
    date character varying
);

--create airlines table
CREATE TABLE IF NOT EXISTS aerolineas_equipo5 (
    code_airline character varying,
    airline character varying
);

--create airports table
CREATE TABLE IF NOT EXISTS aeropuertos_equipo5 (
    iata_code character varying,
    airport character varying,
    city character varying,
    state character varying,
    country character varying,
    latitude double precision,
    longitude double precision
);
