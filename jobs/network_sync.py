from nautobot.apps.jobs import Job, register_jobs

class NetworkSyncJob(Job):
    class Meta:
        name = "Network Sync Job"

    def run(self, *args, **kwargs):
        self.logger.info("Syncing...")

# Make sure this is outside the class indentation block!
register_jobs(NetworkSyncJob)
