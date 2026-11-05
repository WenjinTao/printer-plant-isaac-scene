"""Download the NVIDIA SimReady assets this scene uses (Hugging Face dataset nvidia/simready-assets, CC-BY-4.0,
about 5.9 GB) into the folders the scene expects. Run once, from this folder:

    pip install huggingface_hub
    set HF_HUB_DISABLE_XET=1          (PowerShell: $env:HF_HUB_DISABLE_XET=1; bash: export HF_HUB_DISABLE_XET=1)
    python fetch_simready_assets.py

Re-running skips what is already complete (each asset's packaging json is downloaded last as the done marker).
"""
import os
from huggingface_hub import HfApi, hf_hub_download

REPO = "nvidia/simready-assets"
HERE = os.path.dirname(os.path.abspath(__file__))
NEED = {
    "it_room/assets_simready": [
        "detector_camera_a01",
        "detector_smoke_fire_a01",
        "fireProtection_suppressionCylinder_fixed_a01",
        "lamp_ceiling_1m_rectangle_a01",
        "tools_fireExtinguisher_CO2_a01",
        "warehouse_fireAlarm_wallSwitch_a01"
    ],
    "kitchen/assets_simready": [
        "appliance_dishwasher_a01",
        "appliance_refrigerator_a01",
        "bucket_mop_yellow_b01",
        "cleaning_caddy_a01",
        "cleaning_cloth_a01",
        "cleaning_dishSoap_a01",
        "cleaning_sponge_b01",
        "consumable_paperTowel_roll_a01",
        "detector_smoke_fire_a01",
        "dishware_plastic_bigPlate_a01",
        "dishware_plastic_cup_a01",
        "dishware_plastic_fork_a01",
        "dishware_plastic_spoon_a01",
        "dishware_plastic_tray_a01",
        "facilityEquipment_beverageFridge_display_a01",
        "fireProtection_extinguisher_portable_a01",
        "fixture_counter_a01",
        "fixture_faucet_singleLever_a01",
        "fixture_sink_basin_a01",
        "fixture_soapDispenser_wallMounted_a01",
        "fixture_trashBin_wallMounted_a01",
        "fixture_trashBin_withDispenser_a01",
        "food_beverage_can_b01",
        "food_produce_banana_a01",
        "lamp_ceiling_1m_rectangle_a01",
        "machine_coffee_vending_a01",
        "machine_vending_snacksDrinks_a01",
        "refrigerator_b01",
        "safety_firstAidCabinet_wallMounted_a01",
        "sanitary_sink_wallMounted_a01",
        "sign_wetFloor_a01",
        "storage_shelf_basic_b01",
        "table_metal_stainless_a03",
        "trashCan_wheeled_green_a01",
        "trolley_catering_a01",
        "trolley_cleaning_a01",
        "wasteManagement_recyclingBin_multiStream_a01",
        "wasteManagement_trashBin_wheeled_a01"
    ]
}

api = HfApi()
for folder, names in NEED.items():
    dest = os.path.join(HERE, folder)
    for n in names:
        if os.path.isfile(os.path.join(dest, n, "com.nvidia.simready.packaging.json")):
            continue
        # MDL shaders live in source_assets/, which also holds a second copy of every texture: skip the copies
        files = [f.path for f in api.list_repo_tree(REPO, path_in_repo=n, recursive=True, repo_type="dataset")
                 if hasattr(f, "size") and not ("/source_assets/" in f.path and not f.path.endswith(".mdl"))]
        for p in sorted(files, key=lambda p: p.endswith("packaging.json")):
            hf_hub_download(REPO, p, repo_type="dataset", local_dir=dest)
        print(f"{folder}/{n}: {len(files)} files", flush=True)
print("done")
