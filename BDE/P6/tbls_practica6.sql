-- TABLAS A EMPLEAR PARA LA PRACTICA 6
-- ING. FERNANDO ARREOLA
-- BASES DE DATOS ESTRUCTURADAS, IIMAS, 2025-1

-- SE RECOMIENDA DEDICAR UNOS MINUTOS A ENTENDER EL CONTENIDO Y TIPO DE DATO DE LAS TABLAS

--CREATE DATABASE practica6;

--\c practica6 -

CREATE TABLE partido(
  siglas varchar(10),
  nombre_Oficial varchar (80) not null,
  anio_fundacion smallint not null, -- para evitar problemas de codificacion no se escribe ñ
  constraint partido_pk primary key (siglas)
);

INSERT INTO partido VALUES ('PRI', 'PARTIDO REVOLUCIONARIO INSTITUCIONAL', 1930);
INSERT INTO partido VALUES ('PAN', 'PARTIDO ACCION NACIONAL',1980);
INSERT INTO partido VALUES ('PRD', 'PARTIDO DE LA REVOLUCION DEMOCRATICA', 1985);


CREATE TABLE candidato(
  rfc_candidato varchar(13),
  nombre varchar(50) not null,
  apellido_Pat varchar(50) not null,
  apellido_Mat varchar(50) null,
  fecha_Nacimiento date not null,
  trayectoria smallint not null, --años de trayectoria del candidato
  siglas varchar(10) null,
  constraint candidato_pk primary key (rfc_candidato),
  constraint candidato_partido_fk foreign key (siglas) REFERENCES partido(siglas) on delete set null on update cascade
);

INSERT INTO candidato VALUES('CAND-1','ENRIQUE','PENA','NIETO','1973-10-23',18,'PRI');
INSERT INTO candidato VALUES('CAND-2','RICARDO','ANAYA','CORTES','1969-01-13',22,'PAN');
INSERT INTO candidato VALUES('CAND-4','ANDRES','LOPEZ','OBRADOR','1956-05-12',28,'PRD');
INSERT INTO candidato VALUES('CAND-3','GABRIEL','QUADRI',null,'1961-12-16',3,null);


CREATE TABLE votante(
  id_Votante int,
  nombre varchar(50) not null,
  apellido_Pat varchar(50) not null,
  apellido_Mat varchar(50) null,
  fecha_Nacimiento date not null,
  estado varchar(40) not null,
  rfc_candidato varchar(13) null,
  constraint votante_pk primary key (id_Votante)
);
