"""Compare paired systolic readings in the NHANES 2017–2018 examination sample."""
import sys
import pandas as pd

SOURCE = "https://wwwn.cdc.gov/Nchs/Data/Nhanes/Public/2017/DataFiles/BPX_J.xpt"


def main(source):
    readings = pd.read_sas(source, format="xport")[["BPXSY1", "BPXSY2"]]
    paired = readings.dropna()
    difference = paired["BPXSY2"] - paired["BPXSY1"]
    print(f"Examination records: {len(readings):,}")
    print(f"Complete pairs: {len(paired):,}")
    print(f"Mean second minus first: {difference.mean():.2f} mmHg")
    print(f"Median absolute difference: {difference.abs().median():.1f} mmHg")
    print(f"Second lower: {(difference < 0).sum():,}")
    print(f"Equal: {(difference == 0).sum():,}")
    print(f"Second higher: {(difference > 0).sum():,}")


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else SOURCE)
