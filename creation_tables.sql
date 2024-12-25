

-- object: public.jump | type: TABLE --
DROP TABLE IF EXISTS public.jump CASCADE;
CREATE TABLE public.jump (
	id_jump smallint NOT NULL GENERATED ALWAYS AS IDENTITY ,
	jump_number smallint,
	jump_date date,
	id_jump_type smallint,
	id_altitude smallint,
	id_location smallint,
	id_aircraft smallint,
	id_parachute smallint,
	CONSTRAINT jump_pk PRIMARY KEY (id_jump)
);
-- ddl-end --
ALTER TABLE public.jump OWNER TO benjaminbatignani;
-- ddl-end --

-- object: public.parachute | type: TABLE --
DROP TABLE IF EXISTS public.parachute CASCADE;
CREATE TABLE public.parachute (
	id_parachute smallint NOT NULL GENERATED ALWAYS AS IDENTITY ,
	harness_manufacturer varchar(50),
	harness_name varchar(50),
	harness_serial_number varchar(40),
	harness_dom date,
	main_canopy_manufacturer varchar(50),
	main_canopy_name varchar(50),
	main_canopy_size smallint,
	main_canopy_serial_number varchar(40),
	main_canopy_dom date,
	reserve_canopy_manufacturer varchar(50),
	reserve_canopy_name varchar(50),
	reserve_canopy_size smallint,
	reserve_canopy_serial_number varchar(40),
	reserve_canopy_dom date,
	aad_manufacturer varchar(50),
	aad_name varchar(50),
	aad_serial_number varchar(40),
	aad_dom date,
	CONSTRAINT parachute_pk PRIMARY KEY (id_parachute)
);
-- ddl-end --
ALTER TABLE public.parachute OWNER TO benjaminbatignani;
-- ddl-end --

-- object: parachute_fk | type: CONSTRAINT --
ALTER TABLE public.jump DROP CONSTRAINT IF EXISTS parachute_fk CASCADE;
ALTER TABLE public.jump ADD CONSTRAINT parachute_fk FOREIGN KEY (id_parachute)
REFERENCES public.parachute (id_parachute) MATCH FULL
ON DELETE SET NULL ON UPDATE CASCADE;
-- ddl-end --

-- object: public.altitude | type: TABLE --
DROP TABLE IF EXISTS public.altitude CASCADE;
CREATE TABLE public.altitude (
	id_altitude smallint NOT NULL GENERATED ALWAYS AS IDENTITY ,
	altitude smallint,
	CONSTRAINT altitude_pk PRIMARY KEY (id_altitude)
);
-- ddl-end --
ALTER TABLE public.altitude OWNER TO benjaminbatignani;
-- ddl-end --

-- object: altitude_fk | type: CONSTRAINT --
ALTER TABLE public.jump DROP CONSTRAINT IF EXISTS altitude_fk CASCADE;
ALTER TABLE public.jump ADD CONSTRAINT altitude_fk FOREIGN KEY (id_altitude)
REFERENCES public.altitude (id_altitude) MATCH FULL
ON DELETE SET NULL ON UPDATE CASCADE;
-- ddl-end --

-- object: public.location | type: TABLE --
DROP TABLE IF EXISTS public.location CASCADE;
CREATE TABLE public.location (
	id_location smallint NOT NULL GENERATED ALWAYS AS IDENTITY ,
	location varchar(200),
	CONSTRAINT location_pk PRIMARY KEY (id_location)
);
-- ddl-end --
ALTER TABLE public.location OWNER TO benjaminbatignani;
-- ddl-end --

-- object: location_fk | type: CONSTRAINT --
ALTER TABLE public.jump DROP CONSTRAINT IF EXISTS location_fk CASCADE;
ALTER TABLE public.jump ADD CONSTRAINT location_fk FOREIGN KEY (id_location)
REFERENCES public.location (id_location) MATCH FULL
ON DELETE SET NULL ON UPDATE CASCADE;
-- ddl-end --

-- object: public.aircraft | type: TABLE --
DROP TABLE IF EXISTS public.aircraft CASCADE;
CREATE TABLE public.aircraft (
	id_aircraft smallint NOT NULL GENERATED ALWAYS AS IDENTITY ,
	aircraft varchar(80),
	CONSTRAINT aircraft_pk PRIMARY KEY (id_aircraft)
);
-- ddl-end --
ALTER TABLE public.aircraft OWNER TO benjaminbatignani;
-- ddl-end --

-- object: aircraft_fk | type: CONSTRAINT --
ALTER TABLE public.jump DROP CONSTRAINT IF EXISTS aircraft_fk CASCADE;
ALTER TABLE public.jump ADD CONSTRAINT aircraft_fk FOREIGN KEY (id_aircraft)
REFERENCES public.aircraft (id_aircraft) MATCH FULL
ON DELETE SET NULL ON UPDATE CASCADE;
-- ddl-end --

-- object: public.jump_type | type: TABLE --
DROP TABLE IF EXISTS public.jump_type CASCADE;
CREATE TABLE public.jump_type (
	id_jump_type smallint NOT NULL GENERATED ALWAYS AS IDENTITY ,
	type varchar,
	CONSTRAINT jump_type_pk PRIMARY KEY (id_jump_type)
);
-- ddl-end --
ALTER TABLE public.jump_type OWNER TO benjaminbatignani;
-- ddl-end --

-- object: jump_type_fk | type: CONSTRAINT --
ALTER TABLE public.jump DROP CONSTRAINT IF EXISTS jump_type_fk CASCADE;
ALTER TABLE public.jump ADD CONSTRAINT jump_type_fk FOREIGN KEY (id_jump_type)
REFERENCES public.jump_type (id_jump_type) MATCH FULL
ON DELETE SET NULL ON UPDATE CASCADE;
-- ddl-end --
