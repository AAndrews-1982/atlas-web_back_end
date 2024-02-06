-- List all bands with 'Glam rock' as their main style, ranked by their longevity
SELECT 
    band_name,
    -- Calculate lifespan using the current year if 'split' is NULL
    IFNULL(split, YEAR(CURDATE())) - formed AS lifespan
FROM 
    metal_bands 
WHERE 
    style LIKE '%Glam rock%' -- Adjusted to ensure it captures any variations in style naming
ORDER BY 
    lifespan DESC;
