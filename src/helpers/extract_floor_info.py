def extract_floor_info(floor_str):
    floor_str = str(floor_str).strip()

    if "out of" in floor_str.lower():

        current, total = floor_str.split(" out of ")

        current = current.strip().lower()

        if current == "ground":
            current = 0
        elif current == "upper basement":
            current = 0
        elif current == "lower basement":
            current = -1
        else:
            current = int(current)

        total = int(total)

        return pd.Series([current, total])

    elif floor_str.lower() == "ground":
        return pd.Series([0, 0])

    elif floor_str.isdigit():
        floor_num = int(floor_str)
        return pd.Series([floor_num, floor_num])

    else:
        print("Unhandled:", floor_str)
        return pd.Series([np.nan, np.nan])