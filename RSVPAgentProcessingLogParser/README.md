# RSVP Agent Processing Log Parser Lab

### Prerequisite 

* [DataEngineering.Labs.grep](https://github.com/Zipcoder/DataEngineering.Labs.grep)

### Reference

* [re module](https://docs.python.org/3/library/re.html#module-re)

### Part 1

The data directory contains a file named rsvp_agent_log.dat. Create a file called log_parser.py.
The log_parser script should iterate through the file and look for any instances where the log level is WARNING.
Anytime it encounters a WARNING entry, it should output the following:
* the date and time of the entry followed by a space, double dashes, and another space
* the error message. The error message should exclude the colons and everything between them.

Example output:

```none
WARNINGS:
03/22 08:51:06 -- setsockopt(MCAST_ADD) failed - EDC8116I Address not available.
03/22 08:51:06 -- setsockopt(MCAST_ADD) failed - EDC8116I Address not available.
03/22 08:51:06 -- setsockopt(MCAST_ADD) failed - EDC8116I Address not available.
03/22 08:51:06 -- setsockopt(MCAST_ADD) failed - EDC8116I Address not available.
```