__author__ = 'Andrew'
import time
import urllib.request
from functions import stdout
import workerpool


class DownloadJob(workerpool.Job):
    "Job for downloading a given URL."

    def __init__(self, url, poster_id):
        self.url = url  # The url we'll need to download when the job runs
        self.poster_id = poster_id #need a file name that is the actual id

    def run(self):
        save_to = "C:/posters/%s.jpg" % self.poster_id

        urllib.request.urlretrieve(self.url, save_to)

# Initialize a pool, 5 threads in this case
pool = workerpool.ShrinkWrapWorker(size=100)

# Loop over urls.txt and create a job to download the URL on each line


def download_posters(poster_file, size):
    for url in open("%s" % poster_file, encoding="utf8"):
        job = DownloadJob(url.split(":")[1].replace("\n", ""), url.split(":")[0].replace("\n", ""))
        pool.put(job)
        stdout.write("\r%s/%s" % (str(poster_file), str(size)))
        stdout.flush()
    # Send shutdown jobs to all threads, and wait until all the jobs have been completed
    pool.shutdown()
    pool.wait()
