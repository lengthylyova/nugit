from ..actions import mount, remove, run
from ..argsparser import parser


def nugit():
    args = parser.parse_args()
    match args.action:
        case "mount":
            mount(args)
        case "run":
            run(args)
        case "remove":
            remove(args)
