# 🚚 Cotizador Logístico Flask + OpenRouteService
Este proyecto es un backend modular en Flask que permite calcular el costo de una ruta entre dos puntos, integrando OpenRouteService para obtener distancias reales por carretera y aplicando un tabulador de tarifas.

## 🧩 Características
* Cálculo de distancia entre coordenadas usando OpenRouteService.
* Lógica de cotización basada en rangos y km adicional.
* Configuración vía **.env** para claves y parámetros.
* Listo para pruebas con Postman

  ### Requiere de una ORS Key para funcionar
  ```
  #.env 
  ORS_API_KEY=tu_clave_aqui
  ```
  ### 📮 Endpoint /cotizar

  POST **http://localhost:5000/cotizar**
 <img width="1487" height="695" alt="Captura" src="https://github.com/user-attachments/assets/6fea76fd-ce5b-469f-8505-13bc241f619d" />

 ### 📐 Tabulador aplicado
 * 0–1 km → $1.50
 * 1.1–3 km → $2.00
 * 3.1–7 km → $3.00
 * 7.1–10 km → $4.00
 * 10.1–12 km → $5.00
 * 12.1–16 km → $6.00
 * Km adicional → $0.40 por km extra

### Futuras mejoras
* Validación de puntos ruteables
* Fallback con Haversine si ORS falla
* Tipos de servicio (moto, camión, pickup)
* Logs y métricas de uso
* Analiticas que se muestren en PowerBi
