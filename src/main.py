#!/usr/bin/env python

from src.data.ETL.etl import Etl


def main():
    etl1 = Etl("hej")

    etl1.extract()


if __name__ == "__main__":
    main()

