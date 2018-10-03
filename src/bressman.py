"""
  Capstone Project.  Code written by Joshua Bressman.
  Fall term, 2018-2019.
"""

import rosebotics as rb
import time


def main():
    """ Runs tests. """
    n=5
    run_tests(n)


def run_tests(n):
    """ Runs various tests. """
    run_test_go_stop(n)


def run_test_go_stop(n):
    """ Tests the   go   and   stop   Snatch3rRobot methods. """
    robot = rb.Snatch3rRobot()
    while True:
        robot.go(50, -50)
        if time.time(n):
            break

    print(robot.right_wheel.get_degrees_spun())
    print(robot.left_wheel.get_degrees_spun())
    robot.left_wheel.reset_degrees_spun(0)


    time.sleep(2)

    robot.go(100, 100)
    time.sleep(3)
    robot.stop(rb.StopAction.COAST.value)

    print(robot.right_wheel.get_degrees_spun())
    print(robot.left_wheel.get_degrees_spun())


main()
