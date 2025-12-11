"""logging module is used to record messages (logs) 
raised during program execution."""

"""
USE CASES:
- Debugging
- Tracking errors
- Monitoring code execution
- Understanding application flow in production
"""

import logging

"""NOTE : if level is set to WARNING, then only WARNING, ERROR, and CRITICAL messages show."""
# logging.basicConfig(level=logging.WARNING)

#logging.basicConfig(level=logging.WARNING,
#                    format = "%(asctime)s | %(levelname)s | %(name)s | %(message)s |")

logging.basicConfig(filename="app.log",
                    level=logging.DEBUG,
                    format = "%(asctime)s | %(levelname)s | %(name)s | %(message)s |")

logging.critical("This is a critical message")
logging.error("This is an error message")
logging.warning("This is a warning message")
logging.info("This is an info message")
logging.debug("This is a debug message")

"""
Logging Levels (Importance order high to low)
| Level        | Meaning                       | Typical Use                        |
| ------------ | ----------------------------- | ---------------------------------- |
| **CRITICAL** | Serious failure               | System crash, database failure     |
| **ERROR**    | Major problem                 | Exception caught, function failed  |
| **WARNING**  | Unexpected situation          | Low disk space, deprecated feature |
| **INFO**     | General info                  | Program started, user logged in    |
| **DEBUG**    | Detailed internal information | Debugging variables, flow tracking |
| **NOTSET**   | Internal use                  | Default level                      |
"""

