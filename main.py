import functions as f
import pandas as pd

def main():
    #refreshes list of sets
    f.getMostRecentSetsData()

    filename = "sets.json"
    sets_df = pd.read_json(filename)
    sets_df.sort_values(by = ["releaseDate"])
    print(sets_df)

if __name__ == "__main__":
    main()