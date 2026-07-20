def get_location_dict():
    location_dict  = {
    "src_film" : "/media/david/8TB_drive_2/BalintoreDataVol1/",
    "src_other" : "/media/david/8TB_drive_2/BalintoreDataVol2/",

    "film_1" : "/media/david/4TB_drive_1/BalintoreDataVol1/",
    "film_2" : "/media/david/4TB_drive_2/BalintoreDataVol1/",
    "other_1" : "/media/david/4TB_drive_3/BalintoreDataVol2/",
    "other_2" : "/media/david/4TB_drive_4/BalintoreDataVol2/"
    }
    return location_dict


def get_install_copies() -> list[tuple[str, str]]:
    d = get_location_dict()
    copies = [
        (d["src_other"], d["other_1"]),
        (d["src_other"], d["other_2"]),
        (d["src_film"], d["film_1"]),
        (d["src_film"], d["film_2"]),
    ]
    return copies

def get_export_copies() -> list[tuple[str, str]]:
    d = get_location_dict()
    copies = [
        ( d["other_1"], d["src_other"]),
        ( d["film_1"],  d["src_film"])
    ]
    return copies

def get_rsync_copies() -> list[tuple[str, str]]:
    d = get_location_dict()
    copies = [
        (d["other_2"], d["other_1"]),
        (d["other_1"], d["other_2"]),
        (d["film_2"], d["film_1"]),
        (d["film_1"], d["film_2"]),
    ]
    return copies
