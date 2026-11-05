# Printer plant: Isaac Sim scene (static)

A 3D-printer factory built as a personal build-in-public experiment: production hall, lines, warehouse racks,
showroom, CCTV cameras, canteen kitchen, IT room, fire protection and an SMT line. Static geometry and materials
only (no physics, no animation).

`previews/` holds four CCTV views rendered from this package in Isaac Sim 6.2 (without the SimReady assets).

## Open it

1. Isaac Sim 6.x (or any Omniverse Kit app; built and tested with Isaac Sim 6.2).
2. Optional but recommended: fetch the SimReady props the kitchen and IT room use (about 5.9 GB):
   `pip install huggingface_hub`, set `HF_HUB_DISABLE_XET=1`, then `python fetch_simready_assets.py` in this folder.
   Without them the scene still opens; those props are just missing.
3. File > Open > `printer_plant_smt.usda`. Internet access is needed: 64 NVIDIA assets (warehouse props, forklift, racks,
   data-centre gear, furniture) are referenced by URL from NVIDIA's public content server and load on open.

Units: metres, Z up. About 71,000 prims in Isaac Sim 6.2 (online, before fetching the SimReady assets).

## Layers (each file sublayers the next)

| File | Adds |
|---|---|
| `printer_plant_smt.usda` | the SMT line (`smt_line/`) |
| `printer_plant_real.usda` | realism: kitchen, IT room, fire protection (`realism/`, `kitchen/`, `it_room/`) |
| `printer_plant_cctv.usda` | CCTV cameras (`cctv_cameras.usda`) |
| `printer_plant_showroom.usda` | showroom (`showroom.usda`) |
| `printer_plant.usd` | the plant: building, lines, racks, equipment |

Open a lower file to get a simpler scene (for example `printer_plant.usd` alone).

## Licences

- NVIDIA SimReady assets (fetched, not included): CC-BY-4.0, (c) NVIDIA, https://huggingface.co/datasets/nvidia/simready-assets
- NVIDIA assets referenced by URL: not included; loaded from NVIDIA's server under NVIDIA's terms.
- Everything else in this folder was made by the author for this experiment. Please ask the author before
  redistributing it.
