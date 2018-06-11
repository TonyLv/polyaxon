import auditor

from event_manager.events import build_job

auditor.subscribe(build_job.BuildJobCreatedEvent)
auditor.subscribe(build_job.BuildJobUpdatedEvent)
auditor.subscribe(build_job.BuildJobStartedEvent)
auditor.subscribe(build_job.BuildJobStartedTriggeredEvent)
auditor.subscribe(build_job.BuildJobSoppedEvent)
auditor.subscribe(build_job.BuildJobSoppedTriggeredEvent)
auditor.subscribe(build_job.BuildJobViewedEvent)
auditor.subscribe(build_job.BuildJobNewStatusEvent)
auditor.subscribe(build_job.BuildJobFailedEvent)
auditor.subscribe(build_job.BuildJobSucceededEvent)
auditor.subscribe(build_job.BuildJobDeletedEvent)
auditor.subscribe(build_job.BuildJobDeletedTriggeredEvent)
