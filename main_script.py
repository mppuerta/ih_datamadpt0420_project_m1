import argparse
from p_acquisition import m_acquisition as mac
from p_wrangling import m_wrangling as mwr
from p_analysis import m_analysis as man
#from p_reporting import m_reporting as mre


def argument_parser():
    parser = argparse.ArgumentParser(description='specify inputs')
    parser.add_argument('-c', '--country', type=str, help='filter by country')
    args = parser.parse_args()
    return args


def main(arguments):
    rural = mac.acquire()
    rural_processed = mwr.wrangling(rural)
    rural_analysed = man.analyze(rural_processed)
    return rural_analysed


if __name__ == '__main__':
    arguments = argument_parser()
    main_rural = main(arguments)
    if arguments.country is None:
        print(main_rural)
        print('No country filter. Exported results to csv')
        main_rural.to_csv('data/results/analysed_rural_info.csv', index=False)
    elif arguments.country is not None:
        filtered_rural = main_rural[main_rural['Country'] == arguments.country]
        print(filtered_rural)
        print(f'Filtered by {arguments.country} and exported to csv')
        filtered_rural.to_csv(f'data/results/{arguments.country}_analysed_rural_info.csv', index=False)
