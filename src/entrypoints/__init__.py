from src.actions import mount
from src.argsparser import parser


def prepy():
    args = parser.parse_args()
    match args.action:
        case "mount":
            mount()
        case "validate":
            raise NotImplementedError()
