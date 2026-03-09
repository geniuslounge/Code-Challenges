---
title: Temperature Converter
difficulty: Easy
---

Write a set of functions to convert temperatures between Fahrenheit, Celsius, and Kelvin.

Formulas:
- °C = (°F − 32) × 5/9
- °F = (°C × 9/5) + 32
- K = °C + 273.15

```
to_celsius(32, "F")     →  0.0
to_fahrenheit(100, "C") →  212.0
to_kelvin(0, "C")       →  273.15
to_kelvin(32, "F")      →  273.15
```

**Part 2** — Write a single `convert(value, from_unit, to_unit)` function that handles all six conversion directions.
