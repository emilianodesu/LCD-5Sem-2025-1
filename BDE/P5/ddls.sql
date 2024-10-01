CREATE TABLE asesor(
id_Asesor varchar(4) not null
nombre varchar(100) not null,
constraint asesor_pk primary ky (id_Asesor)
);

CRETE TABLE alumno(
id_Alumno int not null,
nombre varchar(100) not null,
id_Asesor varchar(4) null,
CONSTRAINT alumno_pk primary key (id_Alumno)
CONSTRAINT asesor_fk foreign key (id_asesor) REFRENCES asesor(id_asesor) on delete set null on update cascade
);