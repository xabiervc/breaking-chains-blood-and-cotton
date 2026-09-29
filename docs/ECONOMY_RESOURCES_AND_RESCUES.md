# Bloque 2 — Economía, recursos, reputación y rescates

Los rescates se enlazan con `data/persons.json` mediante `person_id` y con `data/locations.json` mediante `destination_location_id`. La validación global comprueba ambas referencias junto con recursos, operaciones, facciones y rutas.

Las personas rescatadas nunca son recursos de inventario. Conservan identidad, estado y origen; los recursos solo expresan suministros, capacidad y consumibles.

Todas las transiciones y consumos son deterministas y declarados en datos.
