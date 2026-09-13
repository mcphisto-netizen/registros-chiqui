# Registros Chiqui

Registros manuscritos escaneados de perra Chiqui: glucemia, medicación, comidas.
Período: 2026-03-20 a 2026-09-13. Total: 40 hojas.

## Estructura

- `scans/medicacion-glucosa/` — 26 hojas. Planilla semanal 3 bloques: Ayuno / Mediodía / Medianoche. Filas: Medición glucosa + medicamento/dosis. Marca X / ✓ / — / dosis. Esquema cambia en tiempo:
  - mar-abr: T4, Ursomarina, Trilostano, Dipirona, Gabapentina, Proteliv, Insulina 0,1 ml
  - may: sale Dipirona, entra Metronidazol, Tonanvit; Insulina 0,22 / 0,1
  - jun-sep: T4, Trilostano, Caninsulin 0,18-0,2, Fenofibrato, Silimarina, Biletan enzimático, Psyllium
- `scans/comidas/` — 13 hojas. Planilla semanal INGREDIENTE/Dosis: Mediodía + Medianoche. Pechuga 100, muslo 25, arroz 25, zapallito 25, jurel 25, Calcivet, taurina, F.M., + zanahoria / sopa moro / manzana / boniato según semana. Desde 2026-06-17. Cada semana partida en 2 hojas: comidas + medicación.
FM = fórmula magistral 1 cap (colina 400mg, carnitina 400mg, zinc 15mg, selenio 40mcg, vit D 8mcg). Desde 10/9 dieta antiinflamatoria: cerdo 125 + manzana 20 + boniato 25 + sopa moro (9/9 pechuga 125 sustituye cerdo).
- `scans/curvas-notas/` — 1 hoja. Nota libre 2026-08-08 a 2026-08-10: curva horaria (hora - glucosa - dosis insulina), ej 12:00-163-0,24, 18:00-52, 21:00-67. Miel / pollo 40g anotados.
- `lab/` — 15 informes originales (enero 2024 a agosto 2026): hemogramas, bioquímica, orina, cortisol, tiroideos, histopatología. Nombres `YYYYMMDD_descripcion_orig-labNN`.
- `datos/` — tablas OCR: `glucosa.csv` (fecha,momento,valor,origen, 359 filas), `medicacion.csv` (fecha,momento,farmaco,dosis,estado,origen, ~1666 filas), `comidas.csv` (fecha,momento,ingrediente,dosis,estado,origen, 1260 filas), `curvas.csv` (nota libre 8-10/8, 11 filas), `ambiguos.csv` (celdas dudosas + columna desambiguacion), `eventos_clinicos.csv` (hitos: cirugía, postoperatorio, crisis, dieta), `laboratorio.csv` (fecha,parametro,valor,unidad,ref_min,ref_max,origen, 274 filas; LAB02 duplica a LAB03, protocolo completo). Estados: dado (X/✓//), no_dado (—), vacio (celda vacía/diagonal), ambiguo (ver `ambiguos.csv`). Dosis literal de hoja (coma decimal original).

## Nombres

Formato: `YYYYMMDD_YYYYMMDD_<tipo>_origNN.jpg`
`NN` = número escaneo original, preserva trazabilidad. Orden alfabético = orden cronológico.

## Hitos clínicos

Ver `datos/eventos_clinicos.csv`: cirugía de vesícula biliar por mucocele fines de abril 2026 (explica días sin registro 23–26/4 y crisis de mayo), postoperatorio complicado, hipoglucemia de agosto con rescate, gastroenteritis y dieta antiinflamatoria de septiembre.

## Inventario

Ver `INVENTARIO.csv` para mapa completo origN → fecha → tipo.

## Próximo paso

OCR manuscrito → tablas en `datos/`: glucosa (fecha, momento, valor), medicación (fecha, momento, fármaco, dosis, dado sí/no), comidas (fecha, momento, ingrediente, dosis, dado sí/no). Validación manual obligatoria: caligrafía ambigua, X vs ✓ vs —.
