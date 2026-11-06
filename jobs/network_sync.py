from nautobot.apps.jobs import Job, register_jobs

class NetworkSyncJob(Job):
    # This metadata tells Nautobot how to display your job in the UI
    class Meta:
        name = "Network Sync Job"
        description = "Syncs live network states into the Nautobot SSoT"
        has_sensitive_variables = False

    def run(self, *args, **kwargs):
        self.logger.info("Starting network sync job in the lab environment...")
        
        # Your execution code goes here
        
        self.logger.info("Network sync complete!")

# This registration block is REQUIRED for Nautobot to discover the job
register_jobs(NetworkSyncJob)

