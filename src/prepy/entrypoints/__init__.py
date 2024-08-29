from ..actions import mount
from ..argsparser import parser


def prepy():
    args = parser.parse_args()
    match args.action:
        case "mount":
            mount()
        case "validate":
            raise NotImplementedError
        case "check":
            raise NotImplementedError
        case "remove":
            raise NotImplementedError
