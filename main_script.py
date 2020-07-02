import argparse
from p_acquisition import m_acquisition as mac
from p_wrangling import m_wrangling as mwr
from p_analysis import m_analysis as man


def argument_parser():
    parser = argparse.ArgumentParser(description='specify inputs')
    parser.add_argument('-c', '--country', type=str, nargs='+', help='filter by country')
    args = parser.parse_args()
    return args


def main(arguments):
    rural = mac.acquire()
    rural_processed = mwr.wrangling(rural)
    rural_analysed = man.analyze(rural_processed, arguments.country)
    return rural_analysed


if __name__ == '__main__':
    arguments = argument_parser()
    main_rural = main(arguments)
    print(main_rural)
