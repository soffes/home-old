# Naming

So there are lots of names in Home Assistant. I was starting to get frustrated with the inconsistency, so this document aims to set some guidelines for myself so things can be consistent.

## Areas

Areas should map to logical areas of the house. Currently the areas are:

* Front Porch
* Entryway
* Living Room
* Dining Room
* Kitchen
* Hallway
* Guest Bedroom
* Guest Bathroom
* Office
* Master Bedroom
* Master Bathroom
* Bonus Room
* Garage

For stairs, they should be grouped with an area to disambiguate them.

## Entities

If an entity is phyiscally in an aera, it should be prefixed with its area. For example, `living_room_lamp` instead of just `lamp`.

### Multiples

When there are multiple entities that need to be disambiguated by their position, use cardinal directions before the suffix. For example: `master_bedroom_west_lamp`

If there are multiple entities that don’t have a definied position (i.e. multiple bulbs in the same light fixture) use a number at the end: `dining_room_overhead_1`

### Suffixes

#### Lights

Lights should be suffixed with their type:

* `overhead` — Lights attached to the ceiling (including shop lights)
* `lamp` — Lamps
* `lightstrip` — LED lightstrips

When there’s not an obvious type, use `light`.

#### Cover

* `garage_door`
* `shades`

#### Switches

* `plug`
