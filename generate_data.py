import pandas as pd
import glob
from itertools import combinations
import time

path = "**/*.csv"
file_names = glob.glob(path)
dt = {"arr_et": "string", "arr_wet": "string", "dep_et": "string", "dep_wet": "string"}

def get_raw_data():
    li = []
    for file in file_names:
        li.append(pd.read_csv(file, dtype=dt, parse_dates=["ptd", "dep_at", "pta", "arr_at"], date_format="%H:%M"))
    return pd.concat(li)

def calc_time(start_id, end_id, group):
    planned_departure = group.loc[start_id, "ptd"]
    planned_arival = group.loc[end_id, "pta"]
    travel_time = midnight_adjustment((planned_arival   - planned_departure ).total_seconds()/60)
    return travel_time

def midnight_adjustment(time):
    return time + 1440 if time < -500 else time

def generate_row(grouped_data):
    for train_id, group in grouped_data:
        start = time.time()
        group = group.set_index("tpl")
        for start_id, end_id in combinations(group.index, 2):
            dep_delay = group.loc[start_id, "dep_delay"]
            arr_delay = group.loc[end_id, "arr_delay"]
            travel_time = calc_time(start_id, end_id, group)
            yield [train_id, start_id, end_id, dep_delay, travel_time, arr_delay]
        end = time.time()
        print(f"{train_id} complete in {end-start} seconds.")

raw_data = get_raw_data()

# must have arrival or departure data

raw_data["dep_delay"] = raw_data["dep_at"] - raw_data["ptd"]
raw_data["arr_delay"] = raw_data["arr_at"] - raw_data["pta"]

raw_data["dep_delay"] = (raw_data["dep_delay"].dt.total_seconds()/60).apply(midnight_adjustment)
raw_data["arr_delay"] = (raw_data["arr_delay"].dt.total_seconds()/60).apply(midnight_adjustment)

raw_data = raw_data[~(raw_data["dep_delay"].isna() & raw_data["arr_delay"].isna())]

grouped_data = raw_data.groupby(raw_data["rid"])

print(f"{grouped_data.ngroups} different train ID's")

new_data = pd.DataFrame(generate_row(grouped_data), columns=["train_id", "start_id", "End_id", "dep_delay", "travel_time", "arr_delay"])

new_data = new_data.dropna()

print(new_data)

new_data.to_csv("data.csv", index=False)






