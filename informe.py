#!/usr/bin/env python3
"""Genera informe-veterinaria-chiqui.pdf con weasyprint."""
import weasyprint

SEM = [
    ["2026-03-16", 242, 313], ["2026-03-23", 209, 214], ["2026-03-30", 193, 198],
    ["2026-04-06", 183, 207], ["2026-04-13", 234, 307], ["2026-04-20", 214, 226],
    ["2026-04-27", 441, 424], ["2026-05-04", 377, 411], ["2026-05-11", 260, 317],
    ["2026-05-18", 191, 296], ["2026-05-25", 219, 253], ["2026-06-01", 230, 292],
    ["2026-06-08", 249, 316], ["2026-06-15", 273, 274], ["2026-06-22", 245, 258],
    ["2026-06-29", 214, 223], ["2026-07-06", 244, 301], ["2026-07-13", 161, 237],
    ["2026-07-20", 158, 282], ["2026-07-27", 170, 245], ["2026-08-03", 176, 239],
    ["2026-08-10", 141, 241], ["2026-08-17", 161, 212], ["2026-08-24", 173, 226],
    ["2026-08-31", 215, 265], ["2026-09-07", 222, 291]]

def bar_chart(data, unit, cmax, color_fn, label_w=300):
    rows = []
    for lbl, val in data:
        w = max(2, round(val / cmax * 100, 1))
        rows.append(f'<tr><td class="tcell">{lbl}</td><td class="barcell"><div class="bar" style="width:{w}%;background:{color_fn(lbl,val)}"><span class="bv">&nbsp;{val}{unit}</span></div></td></tr>')
    return f'<table class="barchart"><colgroup><col style="width:{label_w}px"><col></colgroup>{"".join(rows)}</table>'

def glu_bars(label, series):
    return '<div class="twocol"><p class="note"><b>'+label+'</b> · media mensual (mg/dL)</p>'+bar_chart(
        series, "", 560, lambda l, v: "#1f7a8c", 120)+'</div>'

glu_m = glu_bars("Mediodía", [
    ("Mar", 214), ("Abr", 241), ("May", 281), ("Jun", 249), ("Jul", 187), ("Ago", 165), ("Sep*", 220)]) + \
        '<div class="twocol"><p class="note"><b>Medianoche</b> · media mensual (mg/dL)</p>'+bar_chart([
    ("Mar", 236), ("Abr", 262), ("May", 331), ("Jun", 285), ("Jul", 259), ("Ago", 225), ("Sep*", 287)], "",
    560, lambda l, v: "#4b2e83", 120)+'</div>'

enz = bar_chart([
    ("18–20/2/26", 1626), ("4/5/26", 386), ("2/6/26", 136), ("3/8/26", 283)], " UI/l",
    1700, lambda l, v: "#8e2c2c" if v > 300 else "#b9770e", 120)

hct = [bar_chart([
    ("DIC 25", 36), ("18/2/26", 37), ("4/5/26", 12.9), ("7/5/26", 23.5),
    ("2/6/26", 40.5), ("3/8/26", 44.1)], " %", 50,
    lambda l, v: "#8e2c2c" if v < 30 else "#1e8449", 110)]

html = f"""<!DOCTYPE html>
<html lang="es"><head><meta charset="utf-8"><style>
@page {{ size: A4; margin: 16mm 15mm; @bottom-center {{ content: "Registros Chiqui · página " counter(page) " de " counter(pages); font-size:8pt; color:#6b7d88; }} }}
* {{ box-sizing: border-box; }}
body {{ font-family: "DejaVu Sans", sans-serif; font-size: 9.5pt; color:#212a30; line-height:1.45; margin:0; }}
h1 {{ font-size:17pt; color:#123240; margin:0 0 2mm; }}
h2 {{ font-size:12pt; color:#123240; border-bottom:2px solid #1f7a8c; padding-bottom:1mm; margin:6mm 0 3mm; }}
h3 {{ font-size:10.5pt; color:#1f5a66; margin:4mm 0 2mm; }}
.head {{ background:#eef5f7; border-bottom:4px solid #1f7a8c; padding:5mm 6mm; border-radius:3mm; }}
.head p {{ margin:1mm 0; }}
.var {{ color:#48606c; }}
table {{ border-collapse:collapse; width:100%; font-size:8.8pt; }}
th, td {{ border:0.5pt solid #cbd8de; padding:1.6mm 2mm; text-align:left; vertical-align:top; }}
th {{ background:#eaf2f5; }}
.r {{ text-align:right; }} .c {{ text-align:center; }}
hr {{ border:0; border-top:0.5pt solid #d8e2e7; margin:4mm 0; }}
.bad {{ color:#a02622; font-weight:bold; }} .ok {{ color:#1e7d3c; font-weight:bold; }} .warn {{ color:#92600a; font-weight:bold; }}
ul {{ margin:1mm 0 2mm 5mm; padding:0; }} li {{ margin:0.8mm 0; }}
.note {{ font-size:8.2pt; color:#48606c; }}
.barchart {{ margin:1mm 0; border:0; page-break-inside:avoid; break-inside:avoid; }}
.kchart {{ page-break-inside:avoid; break-inside:avoid; margin:2mm 0; }}
.barchart td {{ border:0; padding:0.6mm; }}
.barcell {{ width:100%; }}
.bar {{ background:#1f7a8c; border-radius:1mm; min-height:5mm; color:#fff; font-size:7.5pt; }}
.bv {{ display:block; padding:0.8mm 2mm; }}
.tcell {{ white-space:nowrap; font-weight:bold; color:#123240; }}
.twocol {{ width:48%; display:inline-block; vertical-align:top; margin-right:2%; }}
.tag {{ display:inline-block; background:#123240; color:#fff; border-radius:1mm; padding:0.5mm 2mm; font-size:7.5pt; }}
</style></head><body>

<div class="head">
<h1>Informe clínico resumido — canina “Chiqui”</h1>
<p><b>Período analizado:</b> 20/3/2026 – 13/9/2026 &nbsp;·&nbsp; <b>Fuente:</b> 40 planillas caseras diarias (glucemia, insulina, fármacos, comida) + 15 informes de laboratorio (1/2024 – 8/2026).</p>
<p><b>Referencia:</b> github.com/mcphisto-netizen/registros-chiqui · Panel interactivo: <span class="var">panel-chiqui.html</span> · Documento generado 13/9/2026.</p>
</div>

<h2>1 · Diagnósticos y contexto</h2>
<table>
<tr><th>Diagnósticos</th><td>Diabetes mellitus insulinodependiente (posición 20/3/2026) · Hiperadrenocorticismo (Cushing) · Hipotiroidismo · Hepatopatía mixta (lipidosis difusa moderada + colangiohepatitis linfoplasmocítica, biopsia 26/5/2026) · Colecistectomía por mucocele biliar (24–26/4/2026) · Gastroenteritis aguda 17–23/8/2026</td></tr>
<tr><th>Esquema actual (7–13/9)</th><td>Ayuno: T4 ¼ + Dipirona ¼. Mediodía y noche: Trilostano ½, Silimarina ¼, Fenofibrato ¼, Caninsulin 0,18–0,2 U (ajuste por lectura; omitida 12/9 mediodía por peso). Desde 12/9: Biletan enzimático ½ + Psyllium. Dieta antiinflamatoria desde 10/9: cerdo 125 g + manzana 20 g + boniato 25 g + sopa de moro (3 cucharadas).</td></tr>
</table>

<h2>2 · Glucemia de las planillas</h2>
<p class="note">Valores domiciliarios; ante mediciones múltiples del mismo momento se registra la más baja (criterio acordado con el responsable, dos medidores: Maverick y Accucheck, con diferencia sistemática de ~16–20 mg/dL).</p>
<table>
<tr><th>Mes</th><th class="c">n</th><th class="c">Media</th><th class="c">Mín</th><th class="c">Máx</th><th class="c">n</th><th class="c">Media</th><th class="c">Mín</th><th class="c">Máx</th></tr>
<tr><td class="tcell">MEDIODÍA</td><td class="c" colspan="4">(franja azul)</td><td class="tcell">MEDIANOCHE</td><td class="c" colspan="4">(franja violeta)</td></tr>
<tr><td>Marzo (22–31)</td><td class="c">11</td><td class="c">214</td><td class="c">164</td><td class="c">267</td><td class="c">12</td><td class="c">236</td><td class="c">129</td><td class="c">441</td></tr>
<tr><td>Abril</td><td class="c">27</td><td class="c">241</td><td class="c">140</td><td class="c">514</td><td class="c">28</td><td class="c">262</td><td class="c">150</td><td class="c">495</td></tr>
<tr><td>Mayo</td><td class="c">30</td><td class="c">281</td><td class="c">120</td><td class="c">498</td><td class="c">31</td><td class="c">331</td><td class="c">192</td><td class="c">548</td></tr>
<tr><td>Junio</td><td class="c">30</td><td class="c">249</td><td class="c">129</td><td class="c">357</td><td class="c">30</td><td class="c">285</td><td class="c">166</td><td class="c">370</td></tr>
<tr><td>Julio</td><td class="c">31</td><td class="c">187</td><td class="c">55</td><td class="c">428</td><td class="c">32</td><td class="c">259</td><td class="c">50</td><td class="c">433</td></tr>
<tr><td>Agosto</td><td class="c">31</td><td class="c">165</td><td class="c">40</td><td class="c">260</td><td class="c">31</td><td class="c">225</td><td class="c">62</td><td class="c">341</td></tr>
<tr><td>Sept (1–13)</td><td class="c">13</td><td class="c">220</td><td class="c">80</td><td class="c">305</td><td class="c">12</td><td class="c">287</td><td class="c">163</td><td class="c">368</td></tr>
</table>
<p class="note">Media general del período: mediodía ~214 · medianoche ~264. Hipoglucemias &lt;70 registradas: <b>7</b> (18/7, 19/7 ×2, 24/7, 13/8, 21/8, 24/8), mínima 40 (24/8) — corregidas con miel/pollo; curva documentada 8–10/8 (52 → 41 → rescate → rebote 341). Eventos: cirugía 24–26/4 y postoperatorio 27/4–10/5 (pico), gastroenteritis 17–23/8.</p>

{glu_m}

<h2>3 · Laboratorio relevante</h2>
<table>
<tr><th>Fecha</th><th>Hallazgo</th><th>Lectura</th></tr>
<tr><td>18–20/2/26</td><td>Glucosa 487–508 · FAL 1626 · UCCR 4620/40,39 (alta) · T4 libre 0,17 + TSH 0,65 · plaquetas 934000</td><td class="bad">Debut triple: diabetes + Cushing + hipotiroidismo + colestasis marcada</td></tr>
<tr><td>4/5/26</td><td>Hto 12,9 · Hb 4,9 · ALT 160 · FAL 386 · glucosa 212 · amilasa 1163 · calcio 11,3 (corr 12,2)</td><td class="bad">Anemia severa postquirúrgica; laboratorio hepático ya en descenso</td></tr>
<tr><td>7/5/26</td><td>Hto 23,5 · leucocitos 14400 · reticulocitos 5%</td><td class="warn">Recuperación con respuesta regenerativa</td></tr>
<tr><td>26/5/26</td><td>Biopsia: lipidosis difusa moderada + colangiohepatitis linfoplasmocítica</td><td class="warn">Hepatopatía mixta</td></tr>
<tr><td>2/6/26</td><td>ALT 149 · FAL 136 · triglicéridos 819 · colesterol 309 · UPC 1,7 · cetonuria · suero lipémico</td><td class="warn">Mejoría hepática; proteinuria + hiperlipidemia franca</td></tr>
<tr><td>3/8/26</td><td><b>UCCR 22,8 (normal)</b> · ALT 344 · FAL 283 · UPC 0,05 (normal) · T4 libre 0,70 (baja) · urea 95 · TG 277 · colesterol 281 · glucosuria 232</td><td class="warn">Cushing controlado; rebrote hepático; tiroides aún baja; riñón recuperado</td></tr>
</table>
<p class="note">LAB04 y LAB05 provienen de laboratorio humano: valores orientativos, rangos de referencia no aplicables. LAB02 = LAB03 (mismo protocolo del 3/8, completo en LAB03). Bilirrubina siempre normal; ácidos biliares 43 (LAB14). Densidad orina conservada (1010–1035).</p>
<div class="kchart">
<p><b>Hígado — FAL (UI/l):</b></p>{enz}
</div>
<div class="kchart">
<p><b>Hematocrito en evolución:</b></p>{hct[0]}
<p class="note">ALT (UI/l): feb 533 → 4/5 160 → 2/6 149 → 3/8 344. Urea 95 con creatinina normal (3/8) y urea 77,5 (4/5): control renal recomendable.</p>
</div>

<h2>4 · Observaciones derivadas de los datos</h2>
<ul>
<li><b>El debut respondió rápido:</b> glucosa ~500 (feb) → ~214–236 en planillas (finales de marzo), –50% con insulina + Trilostano + T4.</li>
<li><b>Mayo = postoperatorio + anemia, no falla del esquema.</b> Hto 12,9 (4/5) y pico de hiperglucemias 400–548. Sin corticoides (por Cushing): estrés quirúrgico + inflamación + anemia. La serie roja se recuperó sola: 12,9 → 23,5 → 40,5 → 44,1 (ago).</li>
<li><b>Hígado independiente de la glucosa.</b> Mejoró tras cirugía (FAL 1626→136) pero <b>rebrotó en agosto (ALT 344, FAL 283)</b>, cuando la glucemia promediaba su mejor valor (165). La biopsia nombra la causa (lipidosis + colangiohepatitis).</li>
<li><b>Cushing controlado:</b> UCCR de 4620/40,39 (feb) → 22,8 (ago, &lt;40) bajo Trilostano ½ sostenido.</li>
<li><b>Tiroides posiblemente infratratada:</b> T4 libre 0,17 → 0,70, aún bajo rango (0,8–2,5) con ¼; aumento a ½ en agosto. Requiere control T4/TSH para confirmar dosis.</li>
<li><b>Riñón recuperado:</b> proteinuria jun (UPC 1,7) → ago (UPC 0,05). Creatinina siempre normal.</li>
<li><b>Lípidos rebeldes:</b> triglicéridos 819 → 277; colesterol clavado ~281–310 todo el año (fenofibrato justificado).</li>
<li><b>Brecha noche/mes continúa</b> (+20 a +70 sobre el mediodía): presenta picos nocturnos a pesar del descenso del promedio (dosis diseñada para franja diurna).</li>
<li><b>Glucosuria persiste (357 → 232)</b> coherente con la brecha nocturna.</li>
<li><b>Trombocitopenia dic-2025 (56.000) y amilasa 1652 sin diagnóstico</b> (atención veterinaria deficiente en ese período; sin evidencia de pancreatitis posterior a la fecha: ver roadmap).</li>
</ul>

<h2>5 · Roadmap sugerido</h2>
<h3>A · Estudios en el próximo control</h3>
<table>
<tr><th>#</th><th>Estudio</th><th>Justificación</th><th>Prioridad</th></tr>
<tr><td>1</td><td><b>Fructosamina</b></td><td>Sin ninguna en 2 años. Arbitra entre medidores/estrés de consulta, valida promedios y define ajuste de insulina. Interpretable hoy (albúmina 3,39). Bien para ello.</td><td class="bad">Alta</td></tr>
<tr><td>2</td><td><b>Lipasa pancreática específica canina (cPLI)</b></td><td>Amilasa 1652 (12/25) y 1163 (4/5/26) con antecedente de trombocitopenia: descarta/enfoca pancreatitis.</td><td class="bad">Alta</td></tr>
<tr><td>3</td><td><b>T4 libre + TSH</b></td><td>Validar si la dosis de ½ alcanza (T4l 0,70 con ¼).</td><td class="warn">Media</td></tr>
<tr><td>4</td><td><b>Bioquímica hepática + ácidos biliares</b></td><td>Control post-colecistectomía y post-Biletan/Psyllium (rebrote ago).</td><td class="warn">Media</td></tr>
<tr><td>5</td><td><b>UCCR de seguimiento</b></td><td>Consolidar control de Cushing.</td><td class="warn">Media</td></tr>
<tr><td>6</td><td><b>Rasme renal: urea/creatinina/albúmina</b></td><td>Urea 95 con creat normal (3/8); urea 77,5 (4/5).</td><td class="ok">Baja</td></tr>
</table>
<h3>B · Ajustes terapéuticos y de manejo</h3>
<ul>
<li><b>Apuntar a la brecha nocturna:</b> considerar fraccionar/redistribuir insulina (o evaluar con fructosamina/curva si el pico vespertino es real) — la secuencia actual deja la noche cubierta por encima del objetivo.</li>
<li><b>Manejo de hipos:</b> 7 episodios &lt;70 desde julio. Mantener protocolo de rescate (miel + pollo, como en 8–10/8) y revisar si el ½ de Trilostano en horarios del día coincide con caídas.</li>
<li><b>Seguimiento hepático:</b> repetir ALT/FAL ~1–2 meses tras inicio de Biletan/Psyllium (12/9/26) para evaluar respuesta al rebrote de agosto.</li>
<li><b>Dieta antiinflamatoria (10/9):</b> evaluar tolerancia y efecto sobre glucemia tras 4–6 semanas; documentar si mantiene el repunte de septiembre (&gt; agosto).</li>
<li><b>Si cPLI positiva:</b> dieta baja en grasas y ajuste de fenofibrato/asesoría; si negativa, se descarta el foco pancreático y se refuerza el manejo metabólico.</li>
</ul>

<h3>Preguntas abiertas para el próximo control</h3>
<ul>
<li>Fructosamina y cPLI: <i>nunca</i> realizadas.</li>
<li>Etiología de la trombocitopenia de dic-2025 y de las plaquetas 934000 de feb-2026 (estrés/reactivo vs enfermedad primaria de médula).</li>
<li>Posible sangrado gastrointestinal en dic-2025 o perioperatorio (no documentado).</li>
<li>Correlación entre laboratorio (212, 4/5/26) y planillas caseras (400+) de la misma semana: suscita validación de medidores.</li>
</ul>

<p class="note" style="margin-top:6mm">Documento generado automáticamente a partir de los registros digitalizados. Los valores domiciliarios son autoresportados por el responsable; los datos de laboratorio provienen de 15 informes originales (LAB01–LAB15) incluidos en el repositorio.</p>
</body></html>"""

weasyprint.HTML(string=html, base_url=".").write_pdf("informe-veterinaria-chiqui.pdf")
print("OK informe-veterinaria-chiqui.pdf")