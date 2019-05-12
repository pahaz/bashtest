import argparse
import doctest
import re
import sys
import types
import subprocess
import glob

__version__ = '0.0.8'
NAME = 'bashtest'
CHECK_EXITCODE = False

_find_unsafe = re.compile(r'[^\w@%+=:,./-]').search


def quote(s):
    """Return a shell-escaped version of the string *s*."""
    if not s:
        return "''"
    if _find_unsafe(s) is None:
        return "'" + s + "'"

    # use single quotes, and put single quotes into double quotes
    # the string $'b is then quoted as '$'"'"'b'
    return "'" + s.replace("'", "'\"'\"'") + "'"


def _fake_module_run(command):
    command = 'bash -c %s' % (quote(command))
    kwargs = dict(stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
    process = subprocess.Popen(command, **kwargs)
    stdout, _ = process.communicate()
    exitcode = process.poll()

    print(stdout.decode())
    if CHECK_EXITCODE:
        print('<EXITCODE={}>'.format(exitcode))


def parseargs():
    description = (
        "BashTest is a UNIX command-line tool for running text-based bash "
        "tests. "
    )

    parser = argparse.ArgumentParser(description=description)
    parser.add_argument('files', metavar='file', nargs='*',
                        help='Input file (by default uses *.bashtest)')
    parser.add_argument('--exitcode',
                        action='store_true',
                        help='Print exitcode after command end of output')

    parser.add_argument('-v', '--verbose',
                        dest='verbose',
                        action='store_true',
                        help='Verbose output mode')
    parser.add_argument('-q', '--quiet',
                        dest='quiet',
                        action='store_true',
                        help='Silent output mode')
    parser.add_argument('--debug',
                        dest='debug',
                        action='store_true',
                        help='Print the debug information')

    parser.add_argument('--version',
                        dest='version',
                        action='store_true',
                        help='Print the version string')

    return parser.parse_args()


def __re_repl(match):
    g1 = match.group(1)
    g2 = match.group(2)
    g2 = quote(g2.replace('\\', '\\\\'))
    if re.search(r'#skipbashtest', g2):
        return 'skip! %r %r' % (g1, g2)
    return '%s>>> run(%s)' % (g1, g2)


def main():
    global CHECK_EXITCODE

    args = parseargs()
    optionflags = doctest.NORMALIZE_WHITESPACE

    if not args.files:
        args.files = glob.glob('*.bashtest')

    if args.version:
        print(__version__)
        return 0

    if args.quiet:
        args.verbose = False
        args.debug = False

    if args.exitcode:
        CHECK_EXITCODE = True

    finder = doctest.DocTestFinder()
    runner = doctest.DocTestRunner(
        verbose=args.verbose, optionflags=optionflags)

    ret = 0
    rgx = re.compile('^(\s*)\$ (.+)$')
    margin = ''
    in_block = False
    for file in args.files:
        with open(file) as f:
            res = []
            for line in f:
                line = line.rstrip('\r\n')
                match = rgx.match(line)
                if match:
                    if in_block:
                        res.append('')
                    margin = match.group(1)
                    in_block = True
                    line, _ = rgx.subn(__re_repl, line)
                else:
                    if not line and in_block:
                        line = margin + '<BLANKLINE>'
                    if line and in_block:
                        if not line.startswith(margin):
                            in_block = False
                            res.append('')
                res.append(line)

        res = '\n'.join(res)

        if args.debug:
            print('**** %s ****\n%s\n**** /%s ****\n\n' % (file, res, file))

        fake_module = types.ModuleType(file, res)
        fake_module.run = _fake_module_run
        for test in finder.find(fake_module, file):
            runner.run(test)

    runner.summarize(verbose=not args.quiet)

    if runner.failures:
        ret = 1

    sys.exit(ret)

if __name__ == '__main__':
    main()
