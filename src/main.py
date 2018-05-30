#!/usr/bin/env python

from src.data.ETL.etl import Etl
from src.visualization.display import printGrapgh


def main():
    etl1 = Etl("hej")

    etl1.extract()
    df = etl1.transform()
    printGrapgh(df)


if __name__ == "__main__":
    main()

