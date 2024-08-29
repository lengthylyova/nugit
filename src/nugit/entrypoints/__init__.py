from ..actions import mount, remove, run
from ..argsparser import parser


def nugit():
    args = parser.parse_args()
    match args.action:
        case "mount":
            mount()
        case "validate":
            raise NotImplementedError
        case "run":
            run()
        case "remove":
            remove()
