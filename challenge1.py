import sys
from robot_parser import parse
from robot import Robot


def main():
    robot = Robot('', False, 0, 0)
    for line in sys.stdin:
        robot = parse(line, robot)


main()
