import logging

logging.captureWarnings(True)
logging.basicConfig(
    format=" %(asctime)s %(levelname)s: %(message)s",
    level=logging.ERROR,
    datefmt="%Y-%m-%d %H:%M:%S",
)

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
