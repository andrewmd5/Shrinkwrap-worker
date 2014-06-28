"""
Shrinkwrap-worker module provides a threading framework for managing a constant pool
of worker threads that perform arbitrary jobs. It is based on the 2.7 workerpool release

Tips:

* Workers can be terminated using a SuicideJob which raises a TerminationNotice
exception.

* Performing a del on a pool object will cause the pool to terminate all of its
workers.

* WorkerPool implements a simple map method which allows distributing work in a
similar fashion as using a normal map operation.

* EquippedWorkers can be used to maintain an active resource which is required
for performing a specialized type of job.

"""

from .exceptions import *
from .jobs import *
from .pools import *
from .workers import *
