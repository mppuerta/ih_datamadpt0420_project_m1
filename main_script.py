import argparse
from p_acquisition import m_acquisition as mac
from p_wrangling import m_wrangling as mwr
from p_analysis import m_analysis as man
#from p_reporting import m_reporting as mre


def argument_parser():
    parser = argparse.ArgumentParser(description='specify inputs')
    parser.add_argument('-p', '--path', type=str, help='specify .db database path', required=True)
    args = parser.parse_args()
    return args


def main(arguments):
    rural = mac.acquire(arguments.path)
    rural_processed = mwr.wrangling(rural)
    print(man.analyze(rural_processed))


if __name__ == '__main__':
    arguments = argument_parser()
    main(arguments)