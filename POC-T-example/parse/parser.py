"""
Usage:
  POC-T.py [-T|-C] [-m NAME] [-f|-i|-n VALUE] [options]
  POC-T.py [-h|-v|--show|--update]

Example:
  python POC-T.py -T -m test -f ./data/wooyun_domain -t 20
  python POC-T.py -C -m spider -n 192.168.0.0/24 -o ./ans.txt

Engine:
  -T              load Multi-Threaded engine
  -C              load Coroutine engine (single-threaded with asynchronous)
  -t NUM          set num of threads/concurrent [default: 10]

Module:
  -m NAME         select Module/POC name in ./module/ (e.g. jboss-poc)

Target mode:
  -f FILE         load targets from TargetFile (e.g. ./data/wooyun_domain)
  -i START-END    generate payloads from int(START) to int(END) (e.g. 1-100)
  -n IP/MASK      load target IPs from IP/MASK (e.g. 127.0.0.0/24)

Options:
  -o FILE         output file path&name. default in ./output/ (e.g. /tmp/a.txt)
  --single        exit after finding the first victim/password
  --nF            disable file output
  --nS            disable screen output
  --show          show available module/POC names and exit
  --browser       open notepad or web browser to view report after finished
  --debug         show more details while running
  --update        update POC-T from github automatically
  -v --version    show version and quit
  -h --help       show this help page and quit
"""
import sys
from lib.core.settings import VERSION
from thirdparty.docopt.docopt import docopt


def docParser():
    _argv = sys.argv[1:] if len(sys.argv) > 1 else ['--help']
    args = docopt(__doc__, argv=_argv, help=True, version=VERSION, options_first=True)
    if '--debug' in sys.argv:
        print args
    return args
