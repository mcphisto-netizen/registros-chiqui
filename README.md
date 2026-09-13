# Registros Chiqui

Registros manuscritos escaneados de perra Chiqui: glucemia, medicación, comidas.
Período: 2026-03-20 a 2026-09-13. Total: 40 hojas.

## Estructura

- `scans/medicacion-glucosa/` — 26 hojas. Planilla semanal 3 bloques: Ayuno / Mediodía / Medianoche. Filas: Medición glucosa + medicamento/dosis. Marca X / ✓ / — / dosis. Esquema cambia en tiempo:
  - mar-abr: T4, Ursomarina, Trilostano, Dipirona, Gabapentina, Proteliv, Insulina 0,1 ml
  - may: sale Dipirona, entra Metronidazol, Tonanvit; Insulina 0,22 / 0,1
  - jun-sep: T4, Trilostano, Caninsulin 0,18-0,2, Fenofibrato, Silimarina, Bilstan EZ, Psyllium
- `scans/comidas/` — 13 hojas. Planilla semanal INGREDIENTE/Dosis: Mediodía + Medianoche. Pechuga 100, muslo 25, arroz 25, zapallito 25, jurel 25, Calcivet, taurina, F.M., + zanahoria / sopa moro / manzana / boniato según semana. Desde 2026-06-17. Cada semana partida en 2 hojas: comidas + medicación.
- `scans/curvas-notas/` — 1 hoja. Nota libre 2026-08-08 a 2026-08-10: curva horaria (hora - glucosa - dosis insulina), ej 12:00-163-0,24, 18:00-52, 21:00-67. Miel / pollo 40g anotados.
- `datos/` — destino futuro: CSV/tablas OCR (vacío por ahora).

## Nombres

Formato: `YYYYMMDD_YYYYMMDD_<tipo>_origNN.jpg`
`NN` = número escaneo original, preserva trazabilidad. Orden alfabético = orden cronológico.

## Inventario

Ver `INVENTARIO.csv` para mapa completo origN → fecha → tipo.

## Próximo paso

OCR manuscrito → tablas en `datos/`: glucosa (fecha, momento, valor), medicación (fecha, momento, fármaco, dosis, dado sí/no), comidas (fecha, momento, ingrediente, dosis, dado sí/no). Validación manual obligatoria: caligrafía ambigua, X vs ✓ vs —.
