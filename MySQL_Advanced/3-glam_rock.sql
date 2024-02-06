-- List all bands with 'Glam rock' as their main style, ranked by their longevity
SELECT 
    band_name, 
    CASE 
        -- Handle cases where a band is still active or split year is given
        WHEN split = '0' OR split = '9999' OR split IS NULL THEN YEAR(CURDATE()) - formed
        ELSE split - formed 
    END AS lifespan
FROM 
    metal_bands
WHERE 
    main_style = 'Glam rock'
ORDER BY 
    lifespan DESC;
