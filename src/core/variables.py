from pathlib import Path

ROOT = Path(__file__).parent.parent
ENV_FILE = ROOT.parent / '.env'

PASSWORD_LENGTH = 8
SPECIAL_CHARACTERS = '&*%$#@!'
