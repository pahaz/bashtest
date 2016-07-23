import argparse
import doctest
import re
import shlex
import sys
import types


__version__ = '0.0.1'
NAME = 'bashtest'
CHECK_EXITCODE = False


def _fake_module_run(command):
    import subprocess
    import shlex
    command = 'bash -c %s' % (shlex.quote(command))
    r = subprocess.run(command, stdout=subprocess.PIPE,
                       stderr=subprocess.STDOUT, shell=True)
    print(r.stdout.decode())
    if CHECK_EXITCODE:
        print('<EXITCODE={}>'.format(r.returncode))


def parseargs():
    description = (
        "BashTest is a UNIX command-line tool for running text-based bash "
        "tests. "
    )

    parser = argparse.ArgumentParser(description=description)
    parser.add_argument('files', metavar='file', nargs='+',
                        help='Input file')
    parser.add_argument('--exitcode',
                        action='store_true',
                        help='Print exitcode after command end of output')
    parser.add_argument('--no-blankline-substitution',  # I do not use it
                        dest='no_blankline_substitution',
                        action='store_true',
                        help='Substitute `<BLANKLINE>` if an expected output '
                             'block contains a line containing only the `\\n`')
    parser.add_argument('--no-normalize-whitespace',
                        dest='no_normalize_whitespace',
                        action='store_true',
                        help='All sequences of whitespace '
                             '(blanks and newlines) are not equal')

    parser.add_argument('-v', '--verbose',
                        dest='verbose',
                        action='store_true')
    parser.add_argument('-q', '--quiet',
                        dest='quiet',
                        action='store_true')

    parser.add_argument('--version',
                        dest='version',
                        action='store_true',
                        help='Print the version string')

    return parser.parse_args()


def __re_repl(match):
    g1 = match.group(1)
    g2 = match.group(2)
    return '%s>>> run(%s)' % (g1, shlex.quote(g2.replace('\\', '\\\\')))


def main():
    global CHECK_EXITCODE

    args = parseargs()
    optionflags = 0

    if args.version:
        print(__version__)
        return 0

    if args.quiet:
        args.verbose = False

    if args.exitcode:
        CHECK_EXITCODE = True

    if args.no_blankline_substitution:
        optionflags |= doctest.DONT_ACCEPT_BLANKLINE

    if not args.no_normalize_whitespace:
        optionflags |= doctest.NORMALIZE_WHITESPACE

    finder = doctest.DocTestFinder()
    runner = doctest.DocTestRunner(
        verbose=args.verbose, optionflags=optionflags)

    ret = 0
    rgx = re.compile('^(\s*)\$ (.+)$')
    for file in args.files:
        with open(file) as f:
            res = []
            for line in f:
                if rgx.match(line):
                    line, _ = rgx.subn(__re_repl, line)
                res.append(line)

        res = ''.join(res)
        fake_module = types.ModuleType(file, res)
        fake_module.run = _fake_module_run
        for test in finder.find(fake_module, file):
            runner.run(test)

    runner.summarize(verbose=not args.quiet)

    if runner.failures:
        ret = 1
    return ret

if __name__ == '__main__':
    sys.exit(main())
