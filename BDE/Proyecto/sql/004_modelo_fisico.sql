CREATE TABLE estado (
    id_estado   INT,
    nombre_est  VARCHAR(100) NOT NULL,
    CONSTRAINT pk_estado PRIMARY KEY (id_estado)
);
COMMENT ON TABLE estado IS 'Estados de la República Mexicana';

CREATE TABLE municipio (
    id_estado     INT,
    id_municipio  INT,
    nombre_mun    VARCHAR(150)  NOT NULL,
    lat           DECIMAL(9, 6) NOT NULL,
    lon           DECIMAL(9, 6) NOT NULL,
    dh            INT           NOT NULL,
    CONSTRAINT pk_municipio PRIMARY KEY (id_estado, id_municipio),
    CONSTRAINT fk_municipio_estado FOREIGN KEY (id_estado) REFERENCES estado(id_estado)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);
COMMENT ON TABLE municipio IS 'Municipios de la República Mexicana, con sus respectivas coordenadas';
COMMENT ON COLUMN municipio.nombre_mun IS 'nombre municipio';
COMMENT ON COLUMN municipio.lat IS 'Latitud';
COMMENT ON COLUMN municipio.lon IS 'Longitud';
COMMENT ON COLUMN municipio.dh IS 'Diferencia respecto a hora UTC';

CREATE TABLE prediccion (
    id_estado     INT,
    id_municipio  INT,
    fecha         DATE,
    cc            DECIMAL(5, 2) NOT NULL,
    desciel       VARCHAR(255)  NOT NULL,
    dirvienc      VARCHAR(60)   NOT NULL,
    dirvieng      INT           NOT NULL,
    ndia          VARCHAR(10)   NOT NULL,
    prec          DECIMAL(6, 2) NOT NULL,
    probprec      INT           NOT NULL,
    tmax          DECIMAL(5, 2) NOT NULL,
    tmin          DECIMAL(5, 2) NOT NULL,
    velvien       DECIMAL(5, 2) NOT NULL,
    CONSTRAINT pk_prediccion PRIMARY KEY (id_estado, id_municipio, fecha),
    CONSTRAINT fk_prediccion_municipio FOREIGN KEY (id_estado, id_municipio) REFERENCES municipio(id_estado, id_municipio)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    CONSTRAINT chk_cc_positive CHECK (cc >= 0),
    CONSTRAINT chk_ndia_valid CHECK (
        ndia IN ('lunes', 'martes', 'miércoles', 'jueves', 'viernes', 'sábado', 'domingo')
    ),
    CONSTRAINT chk_prec_positive CHECK (prec >= 0),
    CONSTRAINT chk_probprec_positive CHECK (probprec >= 0),
    CONSTRAINT chk_velvien_positive CHECK (velvien >= 0)
);
COMMENT ON TABLE prediccion IS 'Predicción del clima para los municipios de la República Mexicana según la CONAGUA';
COMMENT ON COLUMN prediccion.cc IS 'Cobertura de nubes (%)';
COMMENT ON COLUMN prediccion.desciel IS 'Descripción del cielo';
COMMENT ON COLUMN prediccion.dirvienc IS 'Dirección del viento (Cardinal)';
COMMENT ON COLUMN prediccion.dirvieng IS 'Dirección del viento (Grados)';
COMMENT ON COLUMN prediccion.ndia IS 'número de día';
COMMENT ON COLUMN prediccion.tmax IS 'Temperatura máxima (°C)';
COMMENT ON COLUMN prediccion.tmin IS 'Temperatura mínima (°C)';
COMMENT ON COLUMN prediccion.prec IS 'Precipitación (litros/m2)';
COMMENT ON COLUMN prediccion.probprec IS 'Probabilidad de precipitación (%)';
COMMENT ON COLUMN prediccion.velvien IS 'Velocidad del viento (km/h)';