#!/usr/bin/env python

import rospy


def main():
    rospy.init_node('{{ cookiecutter.project_slug }}_node')

    rospy.spin()


if __name__ == '__main__':
    main()
