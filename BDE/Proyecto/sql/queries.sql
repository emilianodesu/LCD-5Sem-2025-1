-- Generar una consulta que permita obtener por estado, el municipio con la
-- cuarta temperatura más alta.
WITH RankedPredictions AS (
    SELECT
        e.nombre_est,
        p.tmax,
        DENSE_RANK() OVER (PARTITION BY e.nombre_est ORDER BY p.tmax DESC) AS rank
    FROM
        estado e
    JOIN
        municipio m ON e.id_estado = m.id_estado
    JOIN
        prediccion p ON m.id_estado = p.id_estado AND m.id_municipio = p.id_municipio
)
SELECT DISTINCT
    nombre_est,
    tmax
FROM
    RankedPredictions
WHERE
    rank = 4;

-- Generar una consulta que muestre los 5 municipios donde se vayan a presentar descensos
-- de temperatura (tmin) mas marcados entre hoy y el siguiente día.
SELECT
    e.nombre_est,
    m.nombre_mun,
    p_hoy.tmin AS tmin_hoy,
    p_manana.tmin AS tmin_manana,
    p_hoy.tmin - p_manana.tmin AS descenso_temp
FROM
    estado e
JOIN
    municipio m ON e.id_estado = m.id_estado
JOIN
    prediccion p_hoy ON m.id_estado = p_hoy.id_estado AND m.id_municipio = p_hoy.id_municipio
JOIN
    prediccion p_manana ON m.id_estado = p_manana.id_estado AND m.id_municipio = p_manana.id_municipio
WHERE
    p_hoy.fecha = CURRENT_DATE
    AND p_manana.fecha = CURRENT_DATE + INTERVAL '1 day'
ORDER BY descenso_temp DESC LIMIT 5;

