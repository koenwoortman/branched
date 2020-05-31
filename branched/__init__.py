import os
import sys

from simple_term_menu import TerminalMenu

name = 'branched'
version = '0.0.3'


def main():
    if os.path.isdir('.git') is False:
        print('{}: not in a git repo'.format(name))
        return

    branches = os.listdir('.git/refs/heads')
    terminal_menu = TerminalMenu(branches, 'Checkout branch')
    result = terminal_menu.show()
    os.system('git checkout {}'.format(branches[result]))


if __name__ == '__main__':
    rc = 1
    try:
        main()
        rc = 0
    except Exception as e:
        print('Error: %s' % e, file=sys.stderr)
    sys.exit(rc)
