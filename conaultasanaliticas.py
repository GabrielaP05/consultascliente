SELECT c.Nombre AS Categoria, AVG(p.Precio) AS PrecioPromedio
FROM Producto p
JOIN Categoria c ON p.Categoria_ID = c.ID_de_categoria
GROUP BY c.Nombre;
SELECT c.Nombre AS Categoria, SUM(p.CantidadEnStock) AS TotalEnStock
FROM Producto p
JOIN Categoria c ON p.Categoria_ID = c.ID_de_categoria
GROUP BY c.Nombre;
