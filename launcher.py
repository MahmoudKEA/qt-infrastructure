#!/bin/bash

import packages
import packages.header
import packages.utility
import ui
import src


def run():
    while True:
        src.launch()

        if not packages.header.appConfig.developmentMode:
            return


if __name__ == '__main__':
    run()
